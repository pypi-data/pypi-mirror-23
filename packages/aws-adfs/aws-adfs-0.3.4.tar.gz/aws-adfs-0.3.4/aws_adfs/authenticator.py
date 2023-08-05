import logging
import lxml.etree as ET

from . import _duo_authenticator as duo_auth
from . import html_roles_fetcher
from . import roles_assertion_extractor


def authenticate(config, username=None, password=None):

    response, session = html_roles_fetcher.fetch_html_encoded_roles(
        adfs_host=config.adfs_host,
        adfs_cookie_location=config.adfs_cookie_location,
        ssl_verification_enabled=config.ssl_verification,
        provider_id=config.provider_id,
        username=username,
        password=password,
    )

    assertion = None
    aws_session_duration = None

    aggregated_principal_roles = None
    if response.status_code == 200:
        extract_strategy = _strategy(response, config, session)

        principal_roles, assertion, aws_session_duration = extract_strategy()

        if assertion is None:
            logging.error(u'Cannot extract saml assertion. Second factor authentication failed?')
        else:
            aggregated_principal_roles = _aggregate_roles_by_account_alias(session,
                                                                           config,
                                                                           username,
                                                                           password,
                                                                           assertion,
                                                                           principal_roles)

    else:
        logging.error(u'Cannot extract roles from response')

    return aggregated_principal_roles, assertion, aws_session_duration


def _aggregate_roles_by_account_alias(session,
                                      config,
                                      username,
                                      password,
                                      assertion,
                                      principal_roles):
    alias_response = session.post(
        'https://signin.aws.amazon.com/saml',
        verify=config.ssl_verification,
        headers={
            'Accept-Language': 'en',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'text/plain, */*; q=0.01',
        },
        auth=None,
        data={
            'UserName': username,
            'Password': password,
            'AuthMethod': config.provider_id,
            'SAMLResponse': assertion,
        }
    )
    return {}


def _strategy(response, config, session):

    html_response = ET.fromstring(response.text, ET.HTMLParser())

    def _plain_extractor():
        def extract():
            return roles_assertion_extractor.extract(html_response)
        return extract

    def _duo_extractor():
        def extract():
            return duo_auth.extract(html_response, config.ssl_verification, session)
        return extract

    chosen_strategy = _plain_extractor

    if _is_duo_authentication(html_response):
        chosen_strategy = _duo_extractor

    return chosen_strategy()


def _is_duo_authentication(html_response):
    duo_auth_method = './/input[@id="authMethod"]'
    element = html_response.find(duo_auth_method)
    duo = element is not None
    duo = duo and element.get('value') == 'DuoAdfsAdapter'
    return duo
