# coding: utf-8

"""
    Visier Authentication APIs

    Visier APIs for authenticating with Visier. To use Visier's public APIs, you must first authenticate yourself as a Visier user who is allowed to use Visier APIs.

    The version of the OpenAPI document: 22222222.99201.1614
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import base64
import copy
import hashlib
import http.client as httplib
import logging
import multiprocessing
import os
import secrets
import sys
import threading
import time
import webbrowser
from http import HTTPStatus
from logging import FileHandler
from queue import Queue, Empty
from typing import Optional
from urllib.parse import urljoin, quote, urlparse, urlencode
from wsgiref.simple_server import make_server

import urllib3
from flask import Flask, request
from pydantic import BaseModel

from visier_api_core.exceptions import ApiException

import multiprocessing
import urllib3

VISIER_USERNAME='VISIER_USERNAME'
VISIER_PASSWORD='VISIER_PASSWORD'
VISIER_APIKEY='VISIER_APIKEY'
VISIER_HOST='VISIER_HOST'
VISIER_VANITY='VISIER_VANITY'
VISIER_CLIENT_ID='VISIER_CLIENT_ID'
VISIER_CLIENT_SECRET='VISIER_CLIENT_SECRET'
VISIER_REDIRECT_URI='VISIER_REDIRECT_URI'
VISIER_TARGET_TENANT_ID='VISIER_TARGET_TENANT_ID'
VISIER_OAUTH_CALLBACK_URL='VISIER_OAUTH_CALLBACK_URL'

JSON_SCHEMA_VALIDATION_KEYWORDS = {
    'multipleOf', 'maximum', 'exclusiveMaximum',
    'minimum', 'exclusiveMinimum', 'maxLength',
    'minLength', 'pattern', 'maxItems', 'minItems'
}

class Configuration:
    """This class contains various settings of the API client.

    :param host: Base url.
    :param api_key: API key is necessary for all types of authentication.
    :param username: Username for HTTP basic authentication.
    :param password: Password for HTTP basic authentication.
    :param client_id: Client ID for OAuth2 authentication.
    :param client_secret: Client secret for OAuth2 authentication.
    :param redirect_uri: Redirect URI for OAuth2 authentication.
    :param vanity: Vanity name for Visier.
    :param scope: Scope for OAuth2 authentication.
    :param asid_token: ASID token for Visier.
    :param access_token: Access token.
    :param refresh_token: Refresh token.
    :param token_expiration_secs: Token expiration time in seconds.
    :param server_index: Index to servers configuration.
    :param server_variables: Mapping with string values to replace variables in
      templated server configuration. The validation of enums is performed for
      variables with defined enum values before.
    :param server_operation_index: Mapping from operation ID to an index to server
      configuration.
    :param server_operation_variables: Mapping from operation ID to a mapping with
      string values to replace variables in templated server configuration.
      The validation of enums is performed for variables with defined enum
      values before.
    :param ignore_operation_servers: Boolean to ignore operation servers.
    :param ssl_ca_cert: Path to a file of concatenated CA certificates in PEM format.
    :param retries: Number of retries for API requests.
    :param debug: Boolean to enable or disable debug mode.
    """

    _default = None

    def __init__(self,
                 host=None,
                 api_key=None,
                 username=None,
                 password=None,
                 client_id=None,
                 client_secret=None,
                 redirect_uri=None,
                 vanity=None,
                 scope=None,
                 asid_token=None,
                 access_token=None,
                 refresh_token=None,
                 token_expiration_secs=3600,
                 server_index=None,
                 server_variables=None,
                 server_operation_index=None,
                 server_operation_variables=None,
                 ignore_operation_servers=False,
                 ssl_ca_cert=None,
                 retries=None,
                 *,
                 debug: Optional[bool] = None
                 ) -> None:
        """Constructor
        """
        self._base_path = "http://localhost" if host is None else host
        """Default Base url
        """
        # Authentication Settings
        self.api_key = api_key
        """API key is necessary for all types of authentication."""
        self.refresh_config = default_refresh_config
        """function hook to refresh config (e.g. asid_token, access_token, refresh_token)
        """
        self.username = username
        """Username for HTTP basic authentication
        """
        self.password = password
        """Password for HTTP basic authentication
        """
        self.client_id = client_id
        """Client ID for OAuth2 authentication
        """
        self.client_secret = client_secret
        """Client Secret for OAuth2 authentication
        """
        self.redirect_uri = redirect_uri
        """Redirect URI for OAuth2 authentication
        """
        self.vanity = vanity
        """Vanity name for Visier
        """
        self.scope = scope if scope else 'read'
        """Scope for OAuth2 authentication
        """
        self.asid_token = asid_token
        """ASID token for Visier
        """
        self.access_token = access_token
        """Access token
        """
        self.refresh_token = refresh_token
        """Refresh token
        """
        self.token_expiration_secs = token_expiration_secs
        """Token expiration time in seconds
        """
        self._token_acquired_at = None
        """The time when the token was acquired last time
        """
        self.server_index = 0 if server_index is None and host is None else server_index
        self.server_operation_index = server_operation_index or {}
        """Default server index
        """
        self.server_variables = server_variables or {}
        self.server_operation_variables = server_operation_variables or {}
        """Default server variables
        """
        self.ignore_operation_servers = ignore_operation_servers
        """Ignore operation servers
        """
        self.temp_folder_path = None
        """Temp file folder for downloading files
        """


        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("visier_api_core")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler: Optional[FileHandler] = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        if debug is not None:
            self.debug = debug
        else:
            self.__debug = False
        """Debug switch
        """

        self.verify_ssl = True
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = ssl_ca_cert
        """Set this to customize the certificate file to verify the peer.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """
        self.tls_server_name = None
        """SSL/TLS Server Name Indication (SNI)
           Set this to the SNI value expected by the server.
        """

        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        """urllib3 connection pool's maximum number of connections saved
           per pool. urllib3 uses 1 connection as default value, but this is
           not the best value when you are making a lot of possibly parallel
           requests to the same host, which is often the case here.
           cpu_count * 5 is used as default value to increase performance.
        """

        self.proxy: Optional[str] = None
        """Proxy URL
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ''
        """Safe chars for path_param
        """
        self.retries = retries
        """Adding retries to override urllib3 default value 3
        """
        # Enable client side validation
        self.client_side_validation = True

        self.socket_options = None
        """Options to pass down to the underlying urllib3 socket
        """

        self.datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
        """datetime format
        """

        self.date_format = "%Y-%m-%d"
        """date format
        """

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ('logger', 'logger_file_handler'):
                setattr(result, k, copy.deepcopy(v, memo))
        # shallow copy of loggers
        result.logger = copy.copy(self.logger)
        # use setters to configure loggers
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    @classmethod
    def set_default(cls, default):
        """Set default instance of configuration.

        It stores default configuration, which can be
        returned by get_default_copy method.

        :param default: object of Configuration
        """
        cls._default = default

    @classmethod
    def get_default(cls):
        """Return the _default configuration.
        If it is not set, it will be created using from_env method.

        :return: The configuration object.
        """
        if cls._default is None:
            cls._default = Configuration.from_env()
        return cls._default

    @staticmethod
    def from_dict(config_dict):
        """Construct a new Configuration object from a dict.

        :param config_dict: A dictionary of parameters to construct a Configuration object.
        :return: The configuration object.
        """

        return Configuration(
            host=config_dict.get(VISIER_HOST),
            api_key=config_dict.get(VISIER_APIKEY),
            username=config_dict.get(VISIER_USERNAME),
            password=config_dict.get(VISIER_PASSWORD),
            client_id=config_dict.get(VISIER_CLIENT_ID),
            client_secret=config_dict.get(VISIER_CLIENT_SECRET),
            redirect_uri=config_dict.get(VISIER_REDIRECT_URI),
            vanity=config_dict.get(VISIER_VANITY)
        )

    @staticmethod
    def from_env():
        """Construct a new Configuration object from environment variables.

        :return: The configuration object.
        """
        return Configuration(
            host=os.getenv(VISIER_HOST),
            api_key=os.getenv(VISIER_APIKEY),
            username=os.getenv(VISIER_USERNAME),
            password=os.getenv(VISIER_PASSWORD),
            client_id=os.getenv(VISIER_CLIENT_ID),
            client_secret=os.getenv(VISIER_CLIENT_SECRET),
            redirect_uri=os.getenv(VISIER_REDIRECT_URI),
            vanity=os.getenv(VISIER_VANITY)
        )

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        username = ""
        if self.username is not None:
            username = self.username
        password = ""
        if self.password is not None:
            password = self.password
        return urllib3.util.make_headers(
            basic_auth=username + ':' + password
        ).get('authorization')

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """

        if self.refresh_config:
            self.refresh_config(self, False)

        # Necessary apiKey for all auth types
        auth = {'ApiKeyAuth': {
            'type': 'api_key',
            'in': 'header',
            'key': 'apikey',
            'value': self.api_key
        }}

        if self.asid_token:
            auth['CookieAuth'] = {
                'type': 'api_key',
                'in': 'cookie',
                'key': 'VisierASIDToken',
                'value': f'VisierASIDToken={self.asid_token}'
            }

        if self.access_token:
            auth['OAuth2Auth'] = {
                'type': 'bearer',
                'in': 'header',
                'key': 'Authorization',
                'value': 'Bearer ' + self.access_token
            }
        return auth

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 22222222.99201.1614\n"\
               "SDK Package Version: 0.99201.1614".\
               format(env=sys.platform, pyversion=sys.version)

    def get_host_settings(self):
        """Gets an array of host settings

        :return: An array of host settings
        """
        return [
            {
                'url': "",
                'description': "No description provided",
            }
        ]

    def get_host_from_settings(self, index, variables=None, servers=None):
        """Gets host URL based on the index and variables
        :param index: array index of the host settings
        :param variables: hash of variable and the corresponding value
        :param servers: an array of host settings or None
        :return: URL based on host settings
        """
        if index is None:
            return self._base_path

        variables = {} if variables is None else variables
        servers = self.get_host_settings() if servers is None else servers

        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers)))

        url = server['url']

        # go through variables and replace placeholders
        for variable_name, variable in server.get('variables', {}).items():
            used_value = variables.get(
                variable_name, variable['default_value'])

            if 'enum_values' in variable \
                    and used_value not in variable['enum_values']:
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value "
                    "{1}. Must be {2}.".format(
                        variable_name, variables[variable_name],
                        variable['enum_values']))

            url = url.replace("{" + variable_name + "}", used_value)

        return url

    @property
    def host(self):
        """Return generated host."""
        return self.get_host_from_settings(self.server_index, variables=self.server_variables)

    @host.setter
    def host(self, value):
        """Fix base path."""
        self._base_path = value
        self.server_index = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
        self._token_acquired_at = time.time()

    @property
    def asid_token(self):
        return self._asid_token

    @asid_token.setter
    def asid_token(self, value):
        self._asid_token = value
        self._token_acquired_at = time.time()

    def is_token_expired(self):
        # Not using token expiration logic
        if self.token_expiration_secs is None:
            return False

        # Token has not been acquired yet
        if not self._token_acquired_at:
            return True

        return time.time() - self._token_acquired_at > self.token_expiration_secs

# Additional logic to handle authentication
########################################################################################################################
ACCESS_TOKEN = 'access_token'
API_KEY = "apikey"
AUTHORIZATION_CODE = "authorization_code"
CLIENT_ID = "client_id"
CODE = "code"
CODE_CHALLENGE = "code_challenge"
CODE_CHALLENGE_METHOD = "code_challenge_method"
CODE_VERIFIER = "code_verifier"
GRANT_TYPE = "grant_type"
PASSWORD = "password"
REDIRECT_URI = "redirect_uri"
REFRESH_TOKEN = "refresh_token"
RESPONSE_TYPE = "response_type"
SCOPE = "scope"
USERNAME = "username"

# Disable werkzeug logging for the callback server
logging.getLogger('werkzeug').disabled = True

class CallbackServer:
    """Callback server that listens for the OAuth2 authorization code"""

    def __init__(self, provided_url: str) -> None:
        parsed_uri = urlparse(provided_url)
        self.host = parsed_uri.hostname or "localhost"
        self.port = parsed_uri.port or 5000
        self.path = parsed_uri.path or "/oauth2/callback"

        self.server = None
        self.flask_thread = None
        self.app = Flask(__name__)
        self.app.route(self.path, methods=["GET"])(self.callback)
        self.queue = Queue()

    def callback(self):
        """The handler for the OAuth2 callback providing the auth code"""
        code = request.args.get(CODE)
        self.queue.put(code)
        return "<p>You can now close this window</p>"

    def start(self):
        """Starts the callback server"""
        self.server = make_server(self.host, self.port, self.app)
        self.flask_thread = threading.Thread(target=self.server.serve_forever)
        self.flask_thread.start()

    def stop(self):
        """Stops the callback server"""
        if self.server:
            self.server.shutdown()
            self.flask_thread.join()
            self.server = None
            self.flask_thread = None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, ex_type, ex_value, trace_back):
        self.stop()


class TokenRequestDTO(BaseModel):
    grant_type: str
    client_id: str
    scope: str
    username: str = None
    password: str = None
    code: str = None
    code_verifier: str = None
    redirect_uri: str = None
    refresh_token: str = None


class TokenResponseDTO(BaseModel):
    access_token: str
    refresh_token: str
    id_token: str
    token_type: str
    expires_in: int


http = urllib3.PoolManager()


def _post_request(url: str, data: dict, additional_headers: dict = None, auth=None):
    headers = {
        'Accept': 'application/jsonlines, application/json',
        'User-Agent': 'OpenAPI-python',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    if additional_headers:
        headers.update(additional_headers)

    if auth:
        username, password = auth
        auth_header = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('ascii')
        headers['Authorization'] = f'Basic {auth_header}'

    response = http.request(
        'POST',
        url,
        body=urlencode(data),
        headers=headers,
        retries=False
    )
    if response.status != HTTPStatus.OK:
        raise ApiException.from_response(
            http_resp=response,
            body=None,
            data=None
        )

    return response


def _connect_asid(config):
    url = urljoin(config.host, '/v1/admin/visierSecureToken')
    data = {
        USERNAME: config.username,
        PASSWORD: config.password
    }
    if config.vanity:
        data["vanityName"] = config.vanity
    response = _post_request(url=url, data=data)
    config.asid_token = response.data.decode(('utf-8'))


def _update_access_token(config, token_request: TokenRequestDTO):
    url = config.host + "/v1/auth/oauth2/token"
    body = token_request.dict()
    if config.redirect_uri:
        body[REDIRECT_URI] = config.redirect_uri
    auth = (config.client_id, quote(config.client_secret, safe=''))
    headers = {
        API_KEY: config.api_key,
    }

    response = _post_request(url=url, data=body, additional_headers=headers, auth=auth)
    tokenResponse = TokenResponseDTO(**response.json())
    config.access_token = tokenResponse.access_token
    config.refresh_token = tokenResponse.refresh_token
    config.token_expiration_secs = tokenResponse.expires_in


def _refresh_token(config):
    token_request = TokenRequestDTO(
        grant_type=REFRESH_TOKEN,
        client_id=config.client_id,
        scope=config.scope,
        refresh_token=config.refresh_token
    )
    _update_access_token(config, token_request)


def _connect_oauth_password(config):
    token_request = TokenRequestDTO(
        grant_type=PASSWORD,
        client_id=config.client_id,
        scope=config.scope,
        username=config.username,
        password=config.password
    )
    _update_access_token(config, token_request)


def _connect_oauth_code(config):
    """Connect to Visier using (three-legged) OAuth2."""
    code_verifier = secrets.token_urlsafe(64)
    code_challenge_digest = hashlib.sha256(code_verifier.encode()).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge_digest).decode().rstrip("=")

    url_prefix = config.host + "/v1/auth/oauth2"
    svr = CallbackServer(config.redirect_uri)
    query_args = {
        API_KEY: config.api_key,
        RESPONSE_TYPE: CODE,
        CLIENT_ID: config.client_id,
        CODE_CHALLENGE_METHOD: "S256",
        CODE_CHALLENGE: code_challenge
    }
    if config.redirect_uri:
        query_args[REDIRECT_URI] = config.redirect_uri

    browser_url = f'{url_prefix}/authorize?{urlencode(query_args)}'
    webbrowser.open(browser_url)
    try:
        svr.start()
        code = svr.queue.get(block=True, timeout=120)
        token_request = TokenRequestDTO(
            grant_type=AUTHORIZATION_CODE,
            client_id=config.client_id,
            scope=config.scope,
            code=code,
            code_verifier=code_verifier
        )
        _update_access_token(config, token_request)
    except Empty as empty:
        raise ApiException("Timed out waiting for OAuth2 auth code") from empty
    finally:
        svr.stop()


def _connect_oauth(config):
    if config.refresh_token:
        _refresh_token(config)
    elif config.username and config.password:
        _connect_oauth_password(config)
    else:
        _connect_oauth_code(config)


def _need_to_connect(config):
    if config.client_id and config.client_secret:
        return not config.access_token or config.is_token_expired()

    if config.username and config.password:
        return not config.asid_token or config.is_token_expired()

    raise ValueError("No valid authentication method found")


def default_refresh_config(config, force_refresh: bool = False):
    if not force_refresh and not _need_to_connect(config):
        return

    if config.client_id and config.client_secret:
        _connect_oauth(config)
    elif config.username and config.password:
        _connect_asid(config)
