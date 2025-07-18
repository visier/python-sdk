# coding: utf-8

"""
    API Reference

    Detailed API reference documentation for Visier APIs. Includes all endpoints, headers, path parameters, query parameters, request body schema, response schema, JSON request samples, and JSON response samples.

    The version of the OpenAPI document: 22222222.99201.2050
    Contact: alpine@visier.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictStr
from typing import Optional
from typing_extensions import Annotated
from visier_platform_sdk.models.user_v3_api_request_dto import UserV3ApiRequestDTO
from visier_platform_sdk.models.user_v3_api_response_dto import UserV3ApiResponseDTO

from visier_platform_sdk.api_client import ApiClient, RequestSerialized
from visier_platform_sdk.api_response import ApiResponse
from visier_platform_sdk.rest import RESTResponseType


class UsersV3Api:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def update_users(
        self,
        username: Annotated[StrictStr, Field(description="The username of the user to update if the user exists, otherwise creates a new user.")],
        user_v3_api_request_dto: UserV3ApiRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        non_versioned: Annotated[Optional[StrictBool], Field(description="If `true`, the API call executes on non-versioned artifacts and create/update actions take effect without a new production version. If `false`, the API call executes on versioned artifacts and create/update actions release a new production version. Default is `false`.<br>**Note:** <em>This header is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> UserV3ApiResponseDTO:
        """Update or insert (upsert) a user

        Update a user if the user exists, otherwise create a new user. Use the user's `username` to specify the user to update or create.   In `PUT` requests, the definition in your API call replaces the prior definition. You must provide the entire definition in the `PUT` call. If you omit values from the request, those values are removed from the user if the user exists.   <br>Note: <em>This API is in alpha. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param username: The username of the user to update if the user exists, otherwise creates a new user. (required)
        :type username: str
        :param user_v3_api_request_dto: (required)
        :type user_v3_api_request_dto: UserV3ApiRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param non_versioned: If `true`, the API call executes on non-versioned artifacts and create/update actions take effect without a new production version. If `false`, the API call executes on versioned artifacts and create/update actions release a new production version. Default is `false`.<br>**Note:** <em>This header is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>
        :type non_versioned: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._update_users_serialize(
            username=username,
            user_v3_api_request_dto=user_v3_api_request_dto,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserV3ApiResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def update_users_with_http_info(
        self,
        username: Annotated[StrictStr, Field(description="The username of the user to update if the user exists, otherwise creates a new user.")],
        user_v3_api_request_dto: UserV3ApiRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        non_versioned: Annotated[Optional[StrictBool], Field(description="If `true`, the API call executes on non-versioned artifacts and create/update actions take effect without a new production version. If `false`, the API call executes on versioned artifacts and create/update actions release a new production version. Default is `false`.<br>**Note:** <em>This header is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[UserV3ApiResponseDTO]:
        """Update or insert (upsert) a user

        Update a user if the user exists, otherwise create a new user. Use the user's `username` to specify the user to update or create.   In `PUT` requests, the definition in your API call replaces the prior definition. You must provide the entire definition in the `PUT` call. If you omit values from the request, those values are removed from the user if the user exists.   <br>Note: <em>This API is in alpha. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param username: The username of the user to update if the user exists, otherwise creates a new user. (required)
        :type username: str
        :param user_v3_api_request_dto: (required)
        :type user_v3_api_request_dto: UserV3ApiRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param non_versioned: If `true`, the API call executes on non-versioned artifacts and create/update actions take effect without a new production version. If `false`, the API call executes on versioned artifacts and create/update actions release a new production version. Default is `false`.<br>**Note:** <em>This header is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>
        :type non_versioned: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._update_users_serialize(
            username=username,
            user_v3_api_request_dto=user_v3_api_request_dto,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserV3ApiResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def update_users_without_preload_content(
        self,
        username: Annotated[StrictStr, Field(description="The username of the user to update if the user exists, otherwise creates a new user.")],
        user_v3_api_request_dto: UserV3ApiRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        non_versioned: Annotated[Optional[StrictBool], Field(description="If `true`, the API call executes on non-versioned artifacts and create/update actions take effect without a new production version. If `false`, the API call executes on versioned artifacts and create/update actions release a new production version. Default is `false`.<br>**Note:** <em>This header is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update or insert (upsert) a user

        Update a user if the user exists, otherwise create a new user. Use the user's `username` to specify the user to update or create.   In `PUT` requests, the definition in your API call replaces the prior definition. You must provide the entire definition in the `PUT` call. If you omit values from the request, those values are removed from the user if the user exists.   <br>Note: <em>This API is in alpha. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param username: The username of the user to update if the user exists, otherwise creates a new user. (required)
        :type username: str
        :param user_v3_api_request_dto: (required)
        :type user_v3_api_request_dto: UserV3ApiRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param non_versioned: If `true`, the API call executes on non-versioned artifacts and create/update actions take effect without a new production version. If `false`, the API call executes on versioned artifacts and create/update actions release a new production version. Default is `false`.<br>**Note:** <em>This header is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>
        :type non_versioned: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._update_users_serialize(
            username=username,
            user_v3_api_request_dto=user_v3_api_request_dto,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserV3ApiResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _update_users_serialize(
        self,
        username,
        user_v3_api_request_dto,
        target_tenant_id,
        non_versioned,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if username is not None:
            _path_params['username'] = username
        # process the query parameters
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        if non_versioned is not None:
            _header_params['NonVersioned'] = non_versioned
        # process the form parameters
        # process the body parameter
        if user_v3_api_request_dto is not None:
            _body_params = user_v3_api_request_dto


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'CookieAuth', 
            'ApiKeyAuth', 
            'OAuth2Auth', 
            'OAuth2Auth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/v3alpha/admin/users/{username}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


