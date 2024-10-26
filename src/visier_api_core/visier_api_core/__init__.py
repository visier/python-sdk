# coding: utf-8

# flake8: noqa

"""
    Visier Authentication APIs

    Visier APIs for authenticating with Visier. To use Visier's public APIs, you must first authenticate yourself as a Visier user who is allowed to use Visier APIs.

    The version of the OpenAPI document: 22222222.99201.1547
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


__version__ = "0.99201.1547"

# import ApiClient
from visier_api_core.api_response import ApiResponse
from visier_api_core.api_client import ApiClient, RequestSerialized
from visier_api_core.configuration import Configuration
from visier_api_core.rest import RESTClientObject, RESTResponseType
from visier_api_core.exceptions import OpenApiException, ApiTypeError, ApiValueError, ApiKeyError, ApiAttributeError, ApiException

