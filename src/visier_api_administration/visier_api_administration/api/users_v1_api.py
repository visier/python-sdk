# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from visier_api_core import ApiClient, ApiResponse, RequestSerialized, RESTResponseType

from pydantic import Field, StrictBool, StrictBytes, StrictInt, StrictStr
from typing import Any, Dict, Optional, Tuple, Union
from typing_extensions import Annotated
from visier_api_administration.models.admin_transfers_permissions_to_user_group_for_tenant_dto import AdminTransfersPermissionsToUserGroupForTenantDTO
from visier_api_administration.models.admin_transfers_permissions_to_user_groups_request_dto import AdminTransfersPermissionsToUserGroupsRequestDTO
from visier_api_administration.models.admin_transfers_security_assignment_response_dto import AdminTransfersSecurityAssignmentResponseDTO
from visier_api_administration.models.admin_transfers_user_groups_get_api_response_dto import AdminTransfersUserGroupsGetAPIResponseDTO
from visier_api_administration.models.admin_transfers_user_groups_users_dto import AdminTransfersUserGroupsUsersDTO
from visier_api_administration.models.admin_transfers_users_to_user_groups_request_dto import AdminTransfersUsersToUserGroupsRequestDTO
from visier_api_administration.models.servicing_publicapi_transfers_all_users_get_api_response_dto import ServicingPublicapiTransfersAllUsersGetAPIResponseDTO
from visier_api_administration.models.servicing_publicapi_transfers_assign_revoke_permissions_request_dto import ServicingPublicapiTransfersAssignRevokePermissionsRequestDTO
from visier_api_administration.models.servicing_publicapi_transfers_assign_revoke_permissions_response_dto import ServicingPublicapiTransfersAssignRevokePermissionsResponseDTO
from visier_api_administration.models.servicing_publicapi_transfers_permission_assigned_users_dto import ServicingPublicapiTransfersPermissionAssignedUsersDTO
from visier_api_administration.models.servicing_publicapi_transfers_user_creation_api_request_dto import ServicingPublicapiTransfersUserCreationAPIRequestDTO
from visier_api_administration.models.servicing_publicapi_transfers_user_get_api_response_dto import ServicingPublicapiTransfersUserGetAPIResponseDTO
from visier_api_administration.models.servicing_publicapi_transfers_user_update_api_request_dto import ServicingPublicapiTransfersUserUpdateAPIRequestDTO
from visier_api_administration.models.user_creation_api_response_dto import UserCreationAPIResponseDTO
import visier_api_administration.models


class UsersV1Api:
    """
    This class provides methods to make requests to the Visier API.
    It uses the ApiClient to handle the HTTP requests and responses.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def add_user(
        self,
        servicing_publicapi_transfers_user_creation_api_request_dto: ServicingPublicapiTransfersUserCreationAPIRequestDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to create a user in.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> UserCreationAPIResponseDTO:
        """Add a user

        Create a new user. Administrating tenant users can specify the tenant in which to add a user.

        :param servicing_publicapi_transfers_user_creation_api_request_dto: (required)
        :type servicing_publicapi_transfers_user_creation_api_request_dto: ServicingPublicapiTransfersUserCreationAPIRequestDTO
        :param tenant_code: Specify the tenant to create a user in.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._add_user_serialize(
            servicing_publicapi_transfers_user_creation_api_request_dto=servicing_publicapi_transfers_user_creation_api_request_dto,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "UserCreationAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def add_user_with_http_info(
        self,
        servicing_publicapi_transfers_user_creation_api_request_dto: ServicingPublicapiTransfersUserCreationAPIRequestDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to create a user in.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ApiResponse[UserCreationAPIResponseDTO]:
        """Add a user

        Create a new user. Administrating tenant users can specify the tenant in which to add a user.

        :param servicing_publicapi_transfers_user_creation_api_request_dto: (required)
        :type servicing_publicapi_transfers_user_creation_api_request_dto: ServicingPublicapiTransfersUserCreationAPIRequestDTO
        :param tenant_code: Specify the tenant to create a user in.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._add_user_serialize(
            servicing_publicapi_transfers_user_creation_api_request_dto=servicing_publicapi_transfers_user_creation_api_request_dto,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "UserCreationAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def add_user_without_preload_content(
        self,
        servicing_publicapi_transfers_user_creation_api_request_dto: ServicingPublicapiTransfersUserCreationAPIRequestDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to create a user in.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
        """Add a user

        Create a new user. Administrating tenant users can specify the tenant in which to add a user.

        :param servicing_publicapi_transfers_user_creation_api_request_dto: (required)
        :type servicing_publicapi_transfers_user_creation_api_request_dto: ServicingPublicapiTransfersUserCreationAPIRequestDTO
        :param tenant_code: Specify the tenant to create a user in.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._add_user_serialize(
            servicing_publicapi_transfers_user_creation_api_request_dto=servicing_publicapi_transfers_user_creation_api_request_dto,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "UserCreationAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _add_user_serialize(
        self,
        servicing_publicapi_transfers_user_creation_api_request_dto,
        tenant_code,
        target_tenant_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter
        if servicing_publicapi_transfers_user_creation_api_request_dto is not None:
            _body_params = servicing_publicapi_transfers_user_creation_api_request_dto


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
            method='POST',
            resource_path='/v1/admin/users',
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




    @validate_call
    def add_users_to_user_group(
        self,
        admin_transfers_users_to_user_groups_request_dto: AdminTransfersUsersToUserGroupsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
    ) -> AdminTransfersSecurityAssignmentResponseDTO:
        """Assign users to user groups

        This API allows you to assign users to specific user groups.   To assign users to user groups in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can assign users to user groups in multiple analytic tenants by providing a tenant code and project ID in the request body.   We recommend that administrating tenants set the analytic tenant in which to execute the API call using the `TargetTenantID` request header.

        :param admin_transfers_users_to_user_groups_request_dto: (required)
        :type admin_transfers_users_to_user_groups_request_dto: AdminTransfersUsersToUserGroupsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._add_users_to_user_group_serialize(
            admin_transfers_users_to_user_groups_request_dto=admin_transfers_users_to_user_groups_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersSecurityAssignmentResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def add_users_to_user_group_with_http_info(
        self,
        admin_transfers_users_to_user_groups_request_dto: AdminTransfersUsersToUserGroupsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
    ) -> ApiResponse[AdminTransfersSecurityAssignmentResponseDTO]:
        """Assign users to user groups

        This API allows you to assign users to specific user groups.   To assign users to user groups in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can assign users to user groups in multiple analytic tenants by providing a tenant code and project ID in the request body.   We recommend that administrating tenants set the analytic tenant in which to execute the API call using the `TargetTenantID` request header.

        :param admin_transfers_users_to_user_groups_request_dto: (required)
        :type admin_transfers_users_to_user_groups_request_dto: AdminTransfersUsersToUserGroupsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._add_users_to_user_group_serialize(
            admin_transfers_users_to_user_groups_request_dto=admin_transfers_users_to_user_groups_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersSecurityAssignmentResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def add_users_to_user_group_without_preload_content(
        self,
        admin_transfers_users_to_user_groups_request_dto: AdminTransfersUsersToUserGroupsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
        """Assign users to user groups

        This API allows you to assign users to specific user groups.   To assign users to user groups in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can assign users to user groups in multiple analytic tenants by providing a tenant code and project ID in the request body.   We recommend that administrating tenants set the analytic tenant in which to execute the API call using the `TargetTenantID` request header.

        :param admin_transfers_users_to_user_groups_request_dto: (required)
        :type admin_transfers_users_to_user_groups_request_dto: AdminTransfersUsersToUserGroupsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._add_users_to_user_group_serialize(
            admin_transfers_users_to_user_groups_request_dto=admin_transfers_users_to_user_groups_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersSecurityAssignmentResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _add_users_to_user_group_serialize(
        self,
        admin_transfers_users_to_user_groups_request_dto,
        project_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        if non_versioned is not None:
            _header_params['NonVersioned'] = non_versioned
        # process the form parameters
        # process the body parameter
        if admin_transfers_users_to_user_groups_request_dto is not None:
            _body_params = admin_transfers_users_to_user_groups_request_dto


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
            resource_path='/v1/admin/user-groups/users',
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




    @validate_call
    def assign_permissions(
        self,
        servicing_publicapi_transfers_assign_revoke_permissions_request_dto: ServicingPublicapiTransfersAssignRevokePermissionsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
    ) -> ServicingPublicapiTransfersAssignRevokePermissionsResponseDTO:
        """Assign permissions to users

        This API allows you to assign a permission to specific users. Administrating tenant users can assign permissions  to users in the administrating tenant and in the analytic tenants those users belong to.   To assign permissions to users in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can assign permissions to users in analytic tenants by providing a tenant code and project ID in the request body.

        :param servicing_publicapi_transfers_assign_revoke_permissions_request_dto: (required)
        :type servicing_publicapi_transfers_assign_revoke_permissions_request_dto: ServicingPublicapiTransfersAssignRevokePermissionsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._assign_permissions_serialize(
            servicing_publicapi_transfers_assign_revoke_permissions_request_dto=servicing_publicapi_transfers_assign_revoke_permissions_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersAssignRevokePermissionsResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def assign_permissions_with_http_info(
        self,
        servicing_publicapi_transfers_assign_revoke_permissions_request_dto: ServicingPublicapiTransfersAssignRevokePermissionsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
    ) -> ApiResponse[ServicingPublicapiTransfersAssignRevokePermissionsResponseDTO]:
        """Assign permissions to users

        This API allows you to assign a permission to specific users. Administrating tenant users can assign permissions  to users in the administrating tenant and in the analytic tenants those users belong to.   To assign permissions to users in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can assign permissions to users in analytic tenants by providing a tenant code and project ID in the request body.

        :param servicing_publicapi_transfers_assign_revoke_permissions_request_dto: (required)
        :type servicing_publicapi_transfers_assign_revoke_permissions_request_dto: ServicingPublicapiTransfersAssignRevokePermissionsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._assign_permissions_serialize(
            servicing_publicapi_transfers_assign_revoke_permissions_request_dto=servicing_publicapi_transfers_assign_revoke_permissions_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersAssignRevokePermissionsResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def assign_permissions_without_preload_content(
        self,
        servicing_publicapi_transfers_assign_revoke_permissions_request_dto: ServicingPublicapiTransfersAssignRevokePermissionsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
        """Assign permissions to users

        This API allows you to assign a permission to specific users. Administrating tenant users can assign permissions  to users in the administrating tenant and in the analytic tenants those users belong to.   To assign permissions to users in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can assign permissions to users in analytic tenants by providing a tenant code and project ID in the request body.

        :param servicing_publicapi_transfers_assign_revoke_permissions_request_dto: (required)
        :type servicing_publicapi_transfers_assign_revoke_permissions_request_dto: ServicingPublicapiTransfersAssignRevokePermissionsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._assign_permissions_serialize(
            servicing_publicapi_transfers_assign_revoke_permissions_request_dto=servicing_publicapi_transfers_assign_revoke_permissions_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersAssignRevokePermissionsResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _assign_permissions_serialize(
        self,
        servicing_publicapi_transfers_assign_revoke_permissions_request_dto,
        project_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        if non_versioned is not None:
            _header_params['NonVersioned'] = non_versioned
        # process the form parameters
        # process the body parameter
        if servicing_publicapi_transfers_assign_revoke_permissions_request_dto is not None:
            _body_params = servicing_publicapi_transfers_assign_revoke_permissions_request_dto


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
            resource_path='/v1/admin/permissions/users',
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




    @validate_call
    def assign_permissions_to_user_groups(
        self,
        admin_transfers_permissions_to_user_groups_request_dto: AdminTransfersPermissionsToUserGroupsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> AdminTransfersPermissionsToUserGroupForTenantDTO:
        """Assign permissions to user groups

        This API allows you to assign a permission to specific user groups. This assigns the permission to all users in the user group.   To assign permissions to user groups in a project, provide a project UUID in the `ProjectID` request header.

        :param admin_transfers_permissions_to_user_groups_request_dto: (required)
        :type admin_transfers_permissions_to_user_groups_request_dto: AdminTransfersPermissionsToUserGroupsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._assign_permissions_to_user_groups_serialize(
            admin_transfers_permissions_to_user_groups_request_dto=admin_transfers_permissions_to_user_groups_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersPermissionsToUserGroupForTenantDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def assign_permissions_to_user_groups_with_http_info(
        self,
        admin_transfers_permissions_to_user_groups_request_dto: AdminTransfersPermissionsToUserGroupsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ApiResponse[AdminTransfersPermissionsToUserGroupForTenantDTO]:
        """Assign permissions to user groups

        This API allows you to assign a permission to specific user groups. This assigns the permission to all users in the user group.   To assign permissions to user groups in a project, provide a project UUID in the `ProjectID` request header.

        :param admin_transfers_permissions_to_user_groups_request_dto: (required)
        :type admin_transfers_permissions_to_user_groups_request_dto: AdminTransfersPermissionsToUserGroupsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._assign_permissions_to_user_groups_serialize(
            admin_transfers_permissions_to_user_groups_request_dto=admin_transfers_permissions_to_user_groups_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersPermissionsToUserGroupForTenantDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def assign_permissions_to_user_groups_without_preload_content(
        self,
        admin_transfers_permissions_to_user_groups_request_dto: AdminTransfersPermissionsToUserGroupsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
        """Assign permissions to user groups

        This API allows you to assign a permission to specific user groups. This assigns the permission to all users in the user group.   To assign permissions to user groups in a project, provide a project UUID in the `ProjectID` request header.

        :param admin_transfers_permissions_to_user_groups_request_dto: (required)
        :type admin_transfers_permissions_to_user_groups_request_dto: AdminTransfersPermissionsToUserGroupsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._assign_permissions_to_user_groups_serialize(
            admin_transfers_permissions_to_user_groups_request_dto=admin_transfers_permissions_to_user_groups_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersPermissionsToUserGroupForTenantDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _assign_permissions_to_user_groups_serialize(
        self,
        admin_transfers_permissions_to_user_groups_request_dto,
        project_id,
        target_tenant_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter
        if admin_transfers_permissions_to_user_groups_request_dto is not None:
            _body_params = admin_transfers_permissions_to_user_groups_request_dto


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
            resource_path='/v1/admin/user-groups/permissions',
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




    @validate_call
    def delete_user(
        self,
        user_id: Annotated[StrictStr, Field(description="The ID of the user you want to delete.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to delete a user in.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> object:
        """Delete a user

        Delete an existing user. Administrating tenant users can specify the tenant from which to delete a user.

        :param user_id: The ID of the user you want to delete. (required)
        :type user_id: str
        :param tenant_code: Specify the tenant to delete a user in.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._delete_user_serialize(
            user_id=user_id,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def delete_user_with_http_info(
        self,
        user_id: Annotated[StrictStr, Field(description="The ID of the user you want to delete.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to delete a user in.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ApiResponse[object]:
        """Delete a user

        Delete an existing user. Administrating tenant users can specify the tenant from which to delete a user.

        :param user_id: The ID of the user you want to delete. (required)
        :type user_id: str
        :param tenant_code: Specify the tenant to delete a user in.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._delete_user_serialize(
            user_id=user_id,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def delete_user_without_preload_content(
        self,
        user_id: Annotated[StrictStr, Field(description="The ID of the user you want to delete.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to delete a user in.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
        """Delete a user

        Delete an existing user. Administrating tenant users can specify the tenant from which to delete a user.

        :param user_id: The ID of the user you want to delete. (required)
        :type user_id: str
        :param tenant_code: Specify the tenant to delete a user in.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._delete_user_serialize(
            user_id=user_id,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_user_serialize(
        self,
        user_id,
        tenant_code,
        target_tenant_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if user_id is not None:
            _path_params['userId'] = user_id
        # process the query parameters
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'CookieAuth', 
            'ApiKeyAuth', 
            'OAuth2Auth', 
            'OAuth2Auth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/v1/admin/users/{userId}',
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




    @validate_call
    def get_all_permissions_xlsx(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve permissions from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> bytearray:
        """Retrieve a list of all permissions in XLSX format

        This API allows you to export the list of permissions in a tenant. This report includes the permission name,  permission description, and permission ID for all permissions in the tenant.   Administrating tenant users can export permissions lists for the administrating tenant and the analytic tenants  those users belong to.

        :param tenant_code: Specify the tenant to retrieve permissions from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_all_permissions_xlsx_serialize(
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_all_permissions_xlsx_with_http_info(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve permissions from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ApiResponse[bytearray]:
        """Retrieve a list of all permissions in XLSX format

        This API allows you to export the list of permissions in a tenant. This report includes the permission name,  permission description, and permission ID for all permissions in the tenant.   Administrating tenant users can export permissions lists for the administrating tenant and the analytic tenants  those users belong to.

        :param tenant_code: Specify the tenant to retrieve permissions from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_all_permissions_xlsx_serialize(
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_all_permissions_xlsx_without_preload_content(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve permissions from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
        """Retrieve a list of all permissions in XLSX format

        This API allows you to export the list of permissions in a tenant. This report includes the permission name,  permission description, and permission ID for all permissions in the tenant.   Administrating tenant users can export permissions lists for the administrating tenant and the analytic tenants  those users belong to.

        :param tenant_code: Specify the tenant to retrieve permissions from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_all_permissions_xlsx_serialize(
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_all_permissions_xlsx_serialize(
        self,
        tenant_code,
        target_tenant_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.ms-excel', 
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'CookieAuth', 
            'ApiKeyAuth', 
            'OAuth2Auth', 
            'OAuth2Auth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/users/reports/permissions-list',
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




    @validate_call
    def get_all_user_groups(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the list of user groups from.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The number of results to return. The maximum number of users to retrieve is 1000.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="The index to start retrieving results from, also known as offset.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> AdminTransfersUserGroupsGetAPIResponseDTO:
        """Retrieve a list of all user groups

        This API allows you to retrieve the full list of user groups in a tenant.   To specify the project in which to retrieve user groups for a tenant, provide a project UUID in the `ProjectID` request header. If omitted, the request retrieves user information from production.

        :param tenant_code: Specify the tenant to retrieve the list of user groups from.
        :type tenant_code: str
        :param limit: The number of results to return. The maximum number of users to retrieve is 1000.
        :type limit: int
        :param start: The index to start retrieving results from, also known as offset.
        :type start: int
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_all_user_groups_serialize(
            tenant_code=tenant_code,
            limit=limit,
            start=start,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersUserGroupsGetAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_all_user_groups_with_http_info(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the list of user groups from.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The number of results to return. The maximum number of users to retrieve is 1000.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="The index to start retrieving results from, also known as offset.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ApiResponse[AdminTransfersUserGroupsGetAPIResponseDTO]:
        """Retrieve a list of all user groups

        This API allows you to retrieve the full list of user groups in a tenant.   To specify the project in which to retrieve user groups for a tenant, provide a project UUID in the `ProjectID` request header. If omitted, the request retrieves user information from production.

        :param tenant_code: Specify the tenant to retrieve the list of user groups from.
        :type tenant_code: str
        :param limit: The number of results to return. The maximum number of users to retrieve is 1000.
        :type limit: int
        :param start: The index to start retrieving results from, also known as offset.
        :type start: int
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_all_user_groups_serialize(
            tenant_code=tenant_code,
            limit=limit,
            start=start,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersUserGroupsGetAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_all_user_groups_without_preload_content(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the list of user groups from.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The number of results to return. The maximum number of users to retrieve is 1000.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="The index to start retrieving results from, also known as offset.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
        """Retrieve a list of all user groups

        This API allows you to retrieve the full list of user groups in a tenant.   To specify the project in which to retrieve user groups for a tenant, provide a project UUID in the `ProjectID` request header. If omitted, the request retrieves user information from production.

        :param tenant_code: Specify the tenant to retrieve the list of user groups from.
        :type tenant_code: str
        :param limit: The number of results to return. The maximum number of users to retrieve is 1000.
        :type limit: int
        :param start: The index to start retrieving results from, also known as offset.
        :type start: int
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_all_user_groups_serialize(
            tenant_code=tenant_code,
            limit=limit,
            start=start,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersUserGroupsGetAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_all_user_groups_serialize(
        self,
        tenant_code,
        limit,
        start,
        project_id,
        target_tenant_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if start is not None:
            
            _query_params.append(('start', start))
            
        # process the header parameters
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'CookieAuth', 
            'ApiKeyAuth', 
            'OAuth2Auth', 
            'OAuth2Auth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/user-groups',
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




    @validate_call
    def get_all_users(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a list of users from.")] = None,
        assigned_profiles: Annotated[Optional[StrictBool], Field(description="If true, the response returns a list of the user's assigned profiles.")] = None,
        assigned_permissions: Annotated[Optional[StrictBool], Field(description="If true, the response returns the user's assigned permissions.")] = None,
        assigned_user_groups: Annotated[Optional[StrictBool], Field(description="If true, the response returns the user's assigned user groups.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The number of results to return. The maximum number of users to retrieve is 1000.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="The index to start retrieving results from, also known as offset. The index begins at 0.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ServicingPublicapiTransfersAllUsersGetAPIResponseDTO:
        """Retrieve a list of all users

        This API allows you to retrieve the full list of users and their current states.   To specify the project in which to retrieve user information, provide a project UUID in the `ProjectID` request header. If omitted, the request retrieves user information from production.

        :param tenant_code: Specify the tenant to retrieve a list of users from.
        :type tenant_code: str
        :param assigned_profiles: If true, the response returns a list of the user's assigned profiles.
        :type assigned_profiles: bool
        :param assigned_permissions: If true, the response returns the user's assigned permissions.
        :type assigned_permissions: bool
        :param assigned_user_groups: If true, the response returns the user's assigned user groups.
        :type assigned_user_groups: bool
        :param limit: The number of results to return. The maximum number of users to retrieve is 1000.
        :type limit: int
        :param start: The index to start retrieving results from, also known as offset. The index begins at 0.
        :type start: int
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_all_users_serialize(
            tenant_code=tenant_code,
            assigned_profiles=assigned_profiles,
            assigned_permissions=assigned_permissions,
            assigned_user_groups=assigned_user_groups,
            limit=limit,
            start=start,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersAllUsersGetAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_all_users_with_http_info(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a list of users from.")] = None,
        assigned_profiles: Annotated[Optional[StrictBool], Field(description="If true, the response returns a list of the user's assigned profiles.")] = None,
        assigned_permissions: Annotated[Optional[StrictBool], Field(description="If true, the response returns the user's assigned permissions.")] = None,
        assigned_user_groups: Annotated[Optional[StrictBool], Field(description="If true, the response returns the user's assigned user groups.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The number of results to return. The maximum number of users to retrieve is 1000.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="The index to start retrieving results from, also known as offset. The index begins at 0.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ApiResponse[ServicingPublicapiTransfersAllUsersGetAPIResponseDTO]:
        """Retrieve a list of all users

        This API allows you to retrieve the full list of users and their current states.   To specify the project in which to retrieve user information, provide a project UUID in the `ProjectID` request header. If omitted, the request retrieves user information from production.

        :param tenant_code: Specify the tenant to retrieve a list of users from.
        :type tenant_code: str
        :param assigned_profiles: If true, the response returns a list of the user's assigned profiles.
        :type assigned_profiles: bool
        :param assigned_permissions: If true, the response returns the user's assigned permissions.
        :type assigned_permissions: bool
        :param assigned_user_groups: If true, the response returns the user's assigned user groups.
        :type assigned_user_groups: bool
        :param limit: The number of results to return. The maximum number of users to retrieve is 1000.
        :type limit: int
        :param start: The index to start retrieving results from, also known as offset. The index begins at 0.
        :type start: int
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_all_users_serialize(
            tenant_code=tenant_code,
            assigned_profiles=assigned_profiles,
            assigned_permissions=assigned_permissions,
            assigned_user_groups=assigned_user_groups,
            limit=limit,
            start=start,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersAllUsersGetAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_all_users_without_preload_content(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a list of users from.")] = None,
        assigned_profiles: Annotated[Optional[StrictBool], Field(description="If true, the response returns a list of the user's assigned profiles.")] = None,
        assigned_permissions: Annotated[Optional[StrictBool], Field(description="If true, the response returns the user's assigned permissions.")] = None,
        assigned_user_groups: Annotated[Optional[StrictBool], Field(description="If true, the response returns the user's assigned user groups.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The number of results to return. The maximum number of users to retrieve is 1000.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="The index to start retrieving results from, also known as offset. The index begins at 0.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
        """Retrieve a list of all users

        This API allows you to retrieve the full list of users and their current states.   To specify the project in which to retrieve user information, provide a project UUID in the `ProjectID` request header. If omitted, the request retrieves user information from production.

        :param tenant_code: Specify the tenant to retrieve a list of users from.
        :type tenant_code: str
        :param assigned_profiles: If true, the response returns a list of the user's assigned profiles.
        :type assigned_profiles: bool
        :param assigned_permissions: If true, the response returns the user's assigned permissions.
        :type assigned_permissions: bool
        :param assigned_user_groups: If true, the response returns the user's assigned user groups.
        :type assigned_user_groups: bool
        :param limit: The number of results to return. The maximum number of users to retrieve is 1000.
        :type limit: int
        :param start: The index to start retrieving results from, also known as offset. The index begins at 0.
        :type start: int
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_all_users_serialize(
            tenant_code=tenant_code,
            assigned_profiles=assigned_profiles,
            assigned_permissions=assigned_permissions,
            assigned_user_groups=assigned_user_groups,
            limit=limit,
            start=start,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersAllUsersGetAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_all_users_serialize(
        self,
        tenant_code,
        assigned_profiles,
        assigned_permissions,
        assigned_user_groups,
        limit,
        start,
        project_id,
        target_tenant_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        if assigned_profiles is not None:
            
            _query_params.append(('assignedProfiles', assigned_profiles))
            
        if assigned_permissions is not None:
            
            _query_params.append(('assignedPermissions', assigned_permissions))
            
        if assigned_user_groups is not None:
            
            _query_params.append(('assignedUserGroups', assigned_user_groups))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if start is not None:
            
            _query_params.append(('start', start))
            
        # process the header parameters
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'CookieAuth', 
            'ApiKeyAuth', 
            'OAuth2Auth', 
            'OAuth2Auth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/users',
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




    @validate_call
    def get_application_logs_xlsx(
        self,
        start_time: Annotated[Optional[StrictStr], Field(description="An inclusive date-time to start retrieving Application Logs from.")] = None,
        end_time: Annotated[Optional[StrictStr], Field(description="An exclusive date-time to stop retrieving Application Logs from.")] = None,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve Application Logs from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> bytearray:
        """Retrieve the Application Logs

        This API allows you to export the Application Logs for a tenant. The Application Logs track information about your  users and how they are using the application. Performing regular audits will help you identify potential security  issues and keep your data safe. As part of user management, download the Application Logs to monitor user activity  and logon events to ensure your users are performing authorized activities.   Administrating tenant users can export application logs for the administrating tenant and the analytic tenants  those users belong to.

        :param start_time: An inclusive date-time to start retrieving Application Logs from.
        :type start_time: str
        :param end_time: An exclusive date-time to stop retrieving Application Logs from.
        :type end_time: str
        :param tenant_code: Specify the tenant to retrieve Application Logs from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_application_logs_xlsx_serialize(
            start_time=start_time,
            end_time=end_time,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_application_logs_xlsx_with_http_info(
        self,
        start_time: Annotated[Optional[StrictStr], Field(description="An inclusive date-time to start retrieving Application Logs from.")] = None,
        end_time: Annotated[Optional[StrictStr], Field(description="An exclusive date-time to stop retrieving Application Logs from.")] = None,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve Application Logs from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ApiResponse[bytearray]:
        """Retrieve the Application Logs

        This API allows you to export the Application Logs for a tenant. The Application Logs track information about your  users and how they are using the application. Performing regular audits will help you identify potential security  issues and keep your data safe. As part of user management, download the Application Logs to monitor user activity  and logon events to ensure your users are performing authorized activities.   Administrating tenant users can export application logs for the administrating tenant and the analytic tenants  those users belong to.

        :param start_time: An inclusive date-time to start retrieving Application Logs from.
        :type start_time: str
        :param end_time: An exclusive date-time to stop retrieving Application Logs from.
        :type end_time: str
        :param tenant_code: Specify the tenant to retrieve Application Logs from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_application_logs_xlsx_serialize(
            start_time=start_time,
            end_time=end_time,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_application_logs_xlsx_without_preload_content(
        self,
        start_time: Annotated[Optional[StrictStr], Field(description="An inclusive date-time to start retrieving Application Logs from.")] = None,
        end_time: Annotated[Optional[StrictStr], Field(description="An exclusive date-time to stop retrieving Application Logs from.")] = None,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve Application Logs from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
        """Retrieve the Application Logs

        This API allows you to export the Application Logs for a tenant. The Application Logs track information about your  users and how they are using the application. Performing regular audits will help you identify potential security  issues and keep your data safe. As part of user management, download the Application Logs to monitor user activity  and logon events to ensure your users are performing authorized activities.   Administrating tenant users can export application logs for the administrating tenant and the analytic tenants  those users belong to.

        :param start_time: An inclusive date-time to start retrieving Application Logs from.
        :type start_time: str
        :param end_time: An exclusive date-time to stop retrieving Application Logs from.
        :type end_time: str
        :param tenant_code: Specify the tenant to retrieve Application Logs from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_application_logs_xlsx_serialize(
            start_time=start_time,
            end_time=end_time,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_application_logs_xlsx_serialize(
        self,
        start_time,
        end_time,
        tenant_code,
        target_tenant_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if start_time is not None:
            
            _query_params.append(('startTime', start_time))
            
        if end_time is not None:
            
            _query_params.append(('endTime', end_time))
            
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.ms-excel', 
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'CookieAuth', 
            'ApiKeyAuth', 
            'OAuth2Auth', 
            'OAuth2Auth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/users/reports/application-logs',
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




    @validate_call
    def get_data_security_report_xlsx(
        self,
        user_id: Annotated[StrictStr, Field(description="The ID of the user to retrieve the report for.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the Data Security Report from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> bytearray:
        """Retrieve the Data Security Report

        This API allows you to export the data security report of a user. The Data Security Report provides information  about a specific user to see which populations and properties that user has access to as a result of the  permissions assigned to them.   Administrating tenant users can export the report for users in the administrating tenant and the analytic  tenants those users belong to.

        :param user_id: The ID of the user to retrieve the report for. (required)
        :type user_id: str
        :param tenant_code: Specify the tenant to retrieve the Data Security Report from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_data_security_report_xlsx_serialize(
            user_id=user_id,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_data_security_report_xlsx_with_http_info(
        self,
        user_id: Annotated[StrictStr, Field(description="The ID of the user to retrieve the report for.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the Data Security Report from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ApiResponse[bytearray]:
        """Retrieve the Data Security Report

        This API allows you to export the data security report of a user. The Data Security Report provides information  about a specific user to see which populations and properties that user has access to as a result of the  permissions assigned to them.   Administrating tenant users can export the report for users in the administrating tenant and the analytic  tenants those users belong to.

        :param user_id: The ID of the user to retrieve the report for. (required)
        :type user_id: str
        :param tenant_code: Specify the tenant to retrieve the Data Security Report from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_data_security_report_xlsx_serialize(
            user_id=user_id,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_data_security_report_xlsx_without_preload_content(
        self,
        user_id: Annotated[StrictStr, Field(description="The ID of the user to retrieve the report for.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the Data Security Report from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
        """Retrieve the Data Security Report

        This API allows you to export the data security report of a user. The Data Security Report provides information  about a specific user to see which populations and properties that user has access to as a result of the  permissions assigned to them.   Administrating tenant users can export the report for users in the administrating tenant and the analytic  tenants those users belong to.

        :param user_id: The ID of the user to retrieve the report for. (required)
        :type user_id: str
        :param tenant_code: Specify the tenant to retrieve the Data Security Report from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_data_security_report_xlsx_serialize(
            user_id=user_id,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_data_security_report_xlsx_serialize(
        self,
        user_id,
        tenant_code,
        target_tenant_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if user_id is not None:
            _path_params['userId'] = user_id
        # process the query parameters
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.ms-excel', 
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'CookieAuth', 
            'ApiKeyAuth', 
            'OAuth2Auth', 
            'OAuth2Auth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/users/{userId}/reports/data-security',
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




    @validate_call
    def get_permission_assigned_users(
        self,
        permission_id: Annotated[StrictStr, Field(description="The unique identifier of the permission you want to retrieve users for.")],
        include_user_groups: Annotated[Optional[StrictBool], Field(description="If `true`, the response returns a list of all users that are assigned the permission, including users that are  assigned the permission through a user group.  If `false`, the response returns a list of the users that are directly assigned the permission.")] = None,
        tenant_filter: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the list of users from.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The number of results to return. The maximum number of tenants to retrieve is 100.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="The index to start retrieving results from, also known as offset. The index begins at 0.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
    ) -> ServicingPublicapiTransfersPermissionAssignedUsersDTO:
        """Retrieve users that are assigned a specific permission

        This API allows you to retrieve all the users that are assigned a specified permission. You must know the ID  of the permission you want to retrieve users for.   To specify the project in which to retrieve users assigned to a specific permission for the login tenant, provide  a project UUID in the `ProjectID` request header. If omitted, the request retrieves users assigned to a specific permission from production.

        :param permission_id: The unique identifier of the permission you want to retrieve users for. (required)
        :type permission_id: str
        :param include_user_groups: If `true`, the response returns a list of all users that are assigned the permission, including users that are  assigned the permission through a user group.  If `false`, the response returns a list of the users that are directly assigned the permission.
        :type include_user_groups: bool
        :param tenant_filter: Specify the tenant to retrieve the list of users from.
        :type tenant_filter: str
        :param limit: The number of results to return. The maximum number of tenants to retrieve is 100.
        :type limit: int
        :param start: The index to start retrieving results from, also known as offset. The index begins at 0.
        :type start: int
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._get_permission_assigned_users_serialize(
            permission_id=permission_id,
            include_user_groups=include_user_groups,
            tenant_filter=tenant_filter,
            limit=limit,
            start=start,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersPermissionAssignedUsersDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_permission_assigned_users_with_http_info(
        self,
        permission_id: Annotated[StrictStr, Field(description="The unique identifier of the permission you want to retrieve users for.")],
        include_user_groups: Annotated[Optional[StrictBool], Field(description="If `true`, the response returns a list of all users that are assigned the permission, including users that are  assigned the permission through a user group.  If `false`, the response returns a list of the users that are directly assigned the permission.")] = None,
        tenant_filter: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the list of users from.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The number of results to return. The maximum number of tenants to retrieve is 100.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="The index to start retrieving results from, also known as offset. The index begins at 0.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
    ) -> ApiResponse[ServicingPublicapiTransfersPermissionAssignedUsersDTO]:
        """Retrieve users that are assigned a specific permission

        This API allows you to retrieve all the users that are assigned a specified permission. You must know the ID  of the permission you want to retrieve users for.   To specify the project in which to retrieve users assigned to a specific permission for the login tenant, provide  a project UUID in the `ProjectID` request header. If omitted, the request retrieves users assigned to a specific permission from production.

        :param permission_id: The unique identifier of the permission you want to retrieve users for. (required)
        :type permission_id: str
        :param include_user_groups: If `true`, the response returns a list of all users that are assigned the permission, including users that are  assigned the permission through a user group.  If `false`, the response returns a list of the users that are directly assigned the permission.
        :type include_user_groups: bool
        :param tenant_filter: Specify the tenant to retrieve the list of users from.
        :type tenant_filter: str
        :param limit: The number of results to return. The maximum number of tenants to retrieve is 100.
        :type limit: int
        :param start: The index to start retrieving results from, also known as offset. The index begins at 0.
        :type start: int
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._get_permission_assigned_users_serialize(
            permission_id=permission_id,
            include_user_groups=include_user_groups,
            tenant_filter=tenant_filter,
            limit=limit,
            start=start,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersPermissionAssignedUsersDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_permission_assigned_users_without_preload_content(
        self,
        permission_id: Annotated[StrictStr, Field(description="The unique identifier of the permission you want to retrieve users for.")],
        include_user_groups: Annotated[Optional[StrictBool], Field(description="If `true`, the response returns a list of all users that are assigned the permission, including users that are  assigned the permission through a user group.  If `false`, the response returns a list of the users that are directly assigned the permission.")] = None,
        tenant_filter: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the list of users from.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The number of results to return. The maximum number of tenants to retrieve is 100.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="The index to start retrieving results from, also known as offset. The index begins at 0.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
        """Retrieve users that are assigned a specific permission

        This API allows you to retrieve all the users that are assigned a specified permission. You must know the ID  of the permission you want to retrieve users for.   To specify the project in which to retrieve users assigned to a specific permission for the login tenant, provide  a project UUID in the `ProjectID` request header. If omitted, the request retrieves users assigned to a specific permission from production.

        :param permission_id: The unique identifier of the permission you want to retrieve users for. (required)
        :type permission_id: str
        :param include_user_groups: If `true`, the response returns a list of all users that are assigned the permission, including users that are  assigned the permission through a user group.  If `false`, the response returns a list of the users that are directly assigned the permission.
        :type include_user_groups: bool
        :param tenant_filter: Specify the tenant to retrieve the list of users from.
        :type tenant_filter: str
        :param limit: The number of results to return. The maximum number of tenants to retrieve is 100.
        :type limit: int
        :param start: The index to start retrieving results from, also known as offset. The index begins at 0.
        :type start: int
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._get_permission_assigned_users_serialize(
            permission_id=permission_id,
            include_user_groups=include_user_groups,
            tenant_filter=tenant_filter,
            limit=limit,
            start=start,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersPermissionAssignedUsersDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_permission_assigned_users_serialize(
        self,
        permission_id,
        include_user_groups,
        tenant_filter,
        limit,
        start,
        project_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if permission_id is not None:
            _path_params['permissionId'] = permission_id
        # process the query parameters
        if include_user_groups is not None:
            
            _query_params.append(('includeUserGroups', include_user_groups))
            
        if tenant_filter is not None:
            
            _query_params.append(('tenantFilter', tenant_filter))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if start is not None:
            
            _query_params.append(('start', start))
            
        # process the header parameters
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        if non_versioned is not None:
            _header_params['NonVersioned'] = non_versioned
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'CookieAuth', 
            'ApiKeyAuth', 
            'OAuth2Auth', 
            'OAuth2Auth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/permissions/{permissionId}/users',
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




    @validate_call
    def get_profile_assignments_xlsx(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve profile assignments from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> bytearray:
        """Retrieve user profile assignments in XLSX format

        This API allows you to export the profiles assigned to each user. This report details the profiles assigned to  each user and the profile validity period.   Administrating tenant users can export profile assignments for the administrating tenant and the analytic tenants  those users belong to.

        :param tenant_code: Specify the tenant to retrieve profile assignments from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_profile_assignments_xlsx_serialize(
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_profile_assignments_xlsx_with_http_info(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve profile assignments from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ApiResponse[bytearray]:
        """Retrieve user profile assignments in XLSX format

        This API allows you to export the profiles assigned to each user. This report details the profiles assigned to  each user and the profile validity period.   Administrating tenant users can export profile assignments for the administrating tenant and the analytic tenants  those users belong to.

        :param tenant_code: Specify the tenant to retrieve profile assignments from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_profile_assignments_xlsx_serialize(
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_profile_assignments_xlsx_without_preload_content(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve profile assignments from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
        """Retrieve user profile assignments in XLSX format

        This API allows you to export the profiles assigned to each user. This report details the profiles assigned to  each user and the profile validity period.   Administrating tenant users can export profile assignments for the administrating tenant and the analytic tenants  those users belong to.

        :param tenant_code: Specify the tenant to retrieve profile assignments from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_profile_assignments_xlsx_serialize(
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_profile_assignments_xlsx_serialize(
        self,
        tenant_code,
        target_tenant_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.ms-excel', 
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'CookieAuth', 
            'ApiKeyAuth', 
            'OAuth2Auth', 
            'OAuth2Auth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/users/reports/profile-assignments',
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




    @validate_call
    def get_user_detail(
        self,
        user_id: Annotated[StrictStr, Field(description="The ID of the user you want to retrieve.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a user from.")] = None,
        assigned_profiles: Annotated[Optional[StrictBool], Field(description="If true, the response returns a list of the user's assigned profiles.")] = None,
        assigned_permissions: Annotated[Optional[StrictBool], Field(description="If true, the response returns the user's assigned permissions.")] = None,
        assigned_user_groups: Annotated[Optional[StrictBool], Field(description="If true, the response returns the user's assigned user groups.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ServicingPublicapiTransfersUserGetAPIResponseDTO:
        """Retrieve a user's details

        This API allows you to retrieve all details for a specified user.   To specify the project in which to retrieve user information, provide a project UUID in the `ProjectID` request header. If omitted, the request retrieves user information from production.

        :param user_id: The ID of the user you want to retrieve. (required)
        :type user_id: str
        :param tenant_code: Specify the tenant to retrieve a user from.
        :type tenant_code: str
        :param assigned_profiles: If true, the response returns a list of the user's assigned profiles.
        :type assigned_profiles: bool
        :param assigned_permissions: If true, the response returns the user's assigned permissions.
        :type assigned_permissions: bool
        :param assigned_user_groups: If true, the response returns the user's assigned user groups.
        :type assigned_user_groups: bool
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_user_detail_serialize(
            user_id=user_id,
            tenant_code=tenant_code,
            assigned_profiles=assigned_profiles,
            assigned_permissions=assigned_permissions,
            assigned_user_groups=assigned_user_groups,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersUserGetAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_user_detail_with_http_info(
        self,
        user_id: Annotated[StrictStr, Field(description="The ID of the user you want to retrieve.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a user from.")] = None,
        assigned_profiles: Annotated[Optional[StrictBool], Field(description="If true, the response returns a list of the user's assigned profiles.")] = None,
        assigned_permissions: Annotated[Optional[StrictBool], Field(description="If true, the response returns the user's assigned permissions.")] = None,
        assigned_user_groups: Annotated[Optional[StrictBool], Field(description="If true, the response returns the user's assigned user groups.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ApiResponse[ServicingPublicapiTransfersUserGetAPIResponseDTO]:
        """Retrieve a user's details

        This API allows you to retrieve all details for a specified user.   To specify the project in which to retrieve user information, provide a project UUID in the `ProjectID` request header. If omitted, the request retrieves user information from production.

        :param user_id: The ID of the user you want to retrieve. (required)
        :type user_id: str
        :param tenant_code: Specify the tenant to retrieve a user from.
        :type tenant_code: str
        :param assigned_profiles: If true, the response returns a list of the user's assigned profiles.
        :type assigned_profiles: bool
        :param assigned_permissions: If true, the response returns the user's assigned permissions.
        :type assigned_permissions: bool
        :param assigned_user_groups: If true, the response returns the user's assigned user groups.
        :type assigned_user_groups: bool
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_user_detail_serialize(
            user_id=user_id,
            tenant_code=tenant_code,
            assigned_profiles=assigned_profiles,
            assigned_permissions=assigned_permissions,
            assigned_user_groups=assigned_user_groups,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersUserGetAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_user_detail_without_preload_content(
        self,
        user_id: Annotated[StrictStr, Field(description="The ID of the user you want to retrieve.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a user from.")] = None,
        assigned_profiles: Annotated[Optional[StrictBool], Field(description="If true, the response returns a list of the user's assigned profiles.")] = None,
        assigned_permissions: Annotated[Optional[StrictBool], Field(description="If true, the response returns the user's assigned permissions.")] = None,
        assigned_user_groups: Annotated[Optional[StrictBool], Field(description="If true, the response returns the user's assigned user groups.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
        """Retrieve a user's details

        This API allows you to retrieve all details for a specified user.   To specify the project in which to retrieve user information, provide a project UUID in the `ProjectID` request header. If omitted, the request retrieves user information from production.

        :param user_id: The ID of the user you want to retrieve. (required)
        :type user_id: str
        :param tenant_code: Specify the tenant to retrieve a user from.
        :type tenant_code: str
        :param assigned_profiles: If true, the response returns a list of the user's assigned profiles.
        :type assigned_profiles: bool
        :param assigned_permissions: If true, the response returns the user's assigned permissions.
        :type assigned_permissions: bool
        :param assigned_user_groups: If true, the response returns the user's assigned user groups.
        :type assigned_user_groups: bool
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_user_detail_serialize(
            user_id=user_id,
            tenant_code=tenant_code,
            assigned_profiles=assigned_profiles,
            assigned_permissions=assigned_permissions,
            assigned_user_groups=assigned_user_groups,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersUserGetAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_user_detail_serialize(
        self,
        user_id,
        tenant_code,
        assigned_profiles,
        assigned_permissions,
        assigned_user_groups,
        project_id,
        target_tenant_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if user_id is not None:
            _path_params['userId'] = user_id
        # process the query parameters
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        if assigned_profiles is not None:
            
            _query_params.append(('assignedProfiles', assigned_profiles))
            
        if assigned_permissions is not None:
            
            _query_params.append(('assignedPermissions', assigned_permissions))
            
        if assigned_user_groups is not None:
            
            _query_params.append(('assignedUserGroups', assigned_user_groups))
            
        # process the header parameters
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'CookieAuth', 
            'ApiKeyAuth', 
            'OAuth2Auth', 
            'OAuth2Auth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/users/{userId}',
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




    @validate_call
    def get_user_group_users(
        self,
        user_group_id: Annotated[StrictStr, Field(description="The ID of user group.")],
        tenant_filter: Annotated[Optional[StrictStr], Field(description="Specifies the tenant to retrieve the list of users from.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The number of results to return. The maximum number of tenants to retrieve is 100.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="The index to start retrieving results from, also known as offset. The index begins at 0.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> AdminTransfersUserGroupsUsersDTO:
        """Retrieve a list of user group users

        This API allows you to retrieve the list of users explicitly assigned to a user group. Users that are implicitly  included in the user group through the user group's dynamic filters are not returned by this endpoint.   To specify the project in which to retrieve user group users for the login tenant, provide  a project UUID in the `ProjectID` request header. If omitted, the request retrieves user group users from production.

        :param user_group_id: The ID of user group. (required)
        :type user_group_id: str
        :param tenant_filter: Specifies the tenant to retrieve the list of users from.
        :type tenant_filter: str
        :param limit: The number of results to return. The maximum number of tenants to retrieve is 100.
        :type limit: int
        :param start: The index to start retrieving results from, also known as offset. The index begins at 0.
        :type start: int
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_user_group_users_serialize(
            user_group_id=user_group_id,
            tenant_filter=tenant_filter,
            limit=limit,
            start=start,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersUserGroupsUsersDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_user_group_users_with_http_info(
        self,
        user_group_id: Annotated[StrictStr, Field(description="The ID of user group.")],
        tenant_filter: Annotated[Optional[StrictStr], Field(description="Specifies the tenant to retrieve the list of users from.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The number of results to return. The maximum number of tenants to retrieve is 100.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="The index to start retrieving results from, also known as offset. The index begins at 0.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ApiResponse[AdminTransfersUserGroupsUsersDTO]:
        """Retrieve a list of user group users

        This API allows you to retrieve the list of users explicitly assigned to a user group. Users that are implicitly  included in the user group through the user group's dynamic filters are not returned by this endpoint.   To specify the project in which to retrieve user group users for the login tenant, provide  a project UUID in the `ProjectID` request header. If omitted, the request retrieves user group users from production.

        :param user_group_id: The ID of user group. (required)
        :type user_group_id: str
        :param tenant_filter: Specifies the tenant to retrieve the list of users from.
        :type tenant_filter: str
        :param limit: The number of results to return. The maximum number of tenants to retrieve is 100.
        :type limit: int
        :param start: The index to start retrieving results from, also known as offset. The index begins at 0.
        :type start: int
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_user_group_users_serialize(
            user_group_id=user_group_id,
            tenant_filter=tenant_filter,
            limit=limit,
            start=start,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersUserGroupsUsersDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_user_group_users_without_preload_content(
        self,
        user_group_id: Annotated[StrictStr, Field(description="The ID of user group.")],
        tenant_filter: Annotated[Optional[StrictStr], Field(description="Specifies the tenant to retrieve the list of users from.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The number of results to return. The maximum number of tenants to retrieve is 100.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="The index to start retrieving results from, also known as offset. The index begins at 0.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
        """Retrieve a list of user group users

        This API allows you to retrieve the list of users explicitly assigned to a user group. Users that are implicitly  included in the user group through the user group's dynamic filters are not returned by this endpoint.   To specify the project in which to retrieve user group users for the login tenant, provide  a project UUID in the `ProjectID` request header. If omitted, the request retrieves user group users from production.

        :param user_group_id: The ID of user group. (required)
        :type user_group_id: str
        :param tenant_filter: Specifies the tenant to retrieve the list of users from.
        :type tenant_filter: str
        :param limit: The number of results to return. The maximum number of tenants to retrieve is 100.
        :type limit: int
        :param start: The index to start retrieving results from, also known as offset. The index begins at 0.
        :type start: int
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_user_group_users_serialize(
            user_group_id=user_group_id,
            tenant_filter=tenant_filter,
            limit=limit,
            start=start,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersUserGroupsUsersDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_user_group_users_serialize(
        self,
        user_group_id,
        tenant_filter,
        limit,
        start,
        project_id,
        target_tenant_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if user_group_id is not None:
            _path_params['userGroupId'] = user_group_id
        # process the query parameters
        if tenant_filter is not None:
            
            _query_params.append(('tenantFilter', tenant_filter))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if start is not None:
            
            _query_params.append(('start', start))
            
        # process the header parameters
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'CookieAuth', 
            'ApiKeyAuth', 
            'OAuth2Auth', 
            'OAuth2Auth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/user-groups/{userGroupId}/users',
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




    @validate_call
    def get_user_permissions_xlsx(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the permission assignments report from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> bytearray:
        """Retrieve user permissions in XLSX format

        This API allows you to export the user permission assignments for a tenant. The permission assignments report  provides a summary of the permissions your users have been assigned and how each permission is being used across  your user base, as well as the users that do not have any permissions assigned to them.   Administrating tenant users can export permission assignments for the administrating tenant and the analytic  tenants those users belong to.

        :param tenant_code: Specify the tenant to retrieve the permission assignments report from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_user_permissions_xlsx_serialize(
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_user_permissions_xlsx_with_http_info(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the permission assignments report from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ApiResponse[bytearray]:
        """Retrieve user permissions in XLSX format

        This API allows you to export the user permission assignments for a tenant. The permission assignments report  provides a summary of the permissions your users have been assigned and how each permission is being used across  your user base, as well as the users that do not have any permissions assigned to them.   Administrating tenant users can export permission assignments for the administrating tenant and the analytic  tenants those users belong to.

        :param tenant_code: Specify the tenant to retrieve the permission assignments report from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_user_permissions_xlsx_serialize(
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_user_permissions_xlsx_without_preload_content(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the permission assignments report from.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
        """Retrieve user permissions in XLSX format

        This API allows you to export the user permission assignments for a tenant. The permission assignments report  provides a summary of the permissions your users have been assigned and how each permission is being used across  your user base, as well as the users that do not have any permissions assigned to them.   Administrating tenant users can export permission assignments for the administrating tenant and the analytic  tenants those users belong to.

        :param tenant_code: Specify the tenant to retrieve the permission assignments report from.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._get_user_permissions_xlsx_serialize(
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_user_permissions_xlsx_serialize(
        self,
        tenant_code,
        target_tenant_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/vnd.ms-excel', 
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'CookieAuth', 
            'ApiKeyAuth', 
            'OAuth2Auth', 
            'OAuth2Auth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/users/reports/permission-assignments',
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




    @validate_call
    def remove_permissions(
        self,
        servicing_publicapi_transfers_assign_revoke_permissions_request_dto: ServicingPublicapiTransfersAssignRevokePermissionsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
    ) -> ServicingPublicapiTransfersAssignRevokePermissionsResponseDTO:
        """Remove permissions from users

        This API allows you to remove a permission from specific users. Administrating tenant users can remove permissions  from users in the administrating tenant and in the analytic tenants those users belong to.   To remove permission from users in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can remove permissions from users in analytic tenants by providing a tenant code and project ID in the request body.

        :param servicing_publicapi_transfers_assign_revoke_permissions_request_dto: (required)
        :type servicing_publicapi_transfers_assign_revoke_permissions_request_dto: ServicingPublicapiTransfersAssignRevokePermissionsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._remove_permissions_serialize(
            servicing_publicapi_transfers_assign_revoke_permissions_request_dto=servicing_publicapi_transfers_assign_revoke_permissions_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersAssignRevokePermissionsResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def remove_permissions_with_http_info(
        self,
        servicing_publicapi_transfers_assign_revoke_permissions_request_dto: ServicingPublicapiTransfersAssignRevokePermissionsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
    ) -> ApiResponse[ServicingPublicapiTransfersAssignRevokePermissionsResponseDTO]:
        """Remove permissions from users

        This API allows you to remove a permission from specific users. Administrating tenant users can remove permissions  from users in the administrating tenant and in the analytic tenants those users belong to.   To remove permission from users in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can remove permissions from users in analytic tenants by providing a tenant code and project ID in the request body.

        :param servicing_publicapi_transfers_assign_revoke_permissions_request_dto: (required)
        :type servicing_publicapi_transfers_assign_revoke_permissions_request_dto: ServicingPublicapiTransfersAssignRevokePermissionsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._remove_permissions_serialize(
            servicing_publicapi_transfers_assign_revoke_permissions_request_dto=servicing_publicapi_transfers_assign_revoke_permissions_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersAssignRevokePermissionsResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def remove_permissions_without_preload_content(
        self,
        servicing_publicapi_transfers_assign_revoke_permissions_request_dto: ServicingPublicapiTransfersAssignRevokePermissionsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
        """Remove permissions from users

        This API allows you to remove a permission from specific users. Administrating tenant users can remove permissions  from users in the administrating tenant and in the analytic tenants those users belong to.   To remove permission from users in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can remove permissions from users in analytic tenants by providing a tenant code and project ID in the request body.

        :param servicing_publicapi_transfers_assign_revoke_permissions_request_dto: (required)
        :type servicing_publicapi_transfers_assign_revoke_permissions_request_dto: ServicingPublicapiTransfersAssignRevokePermissionsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._remove_permissions_serialize(
            servicing_publicapi_transfers_assign_revoke_permissions_request_dto=servicing_publicapi_transfers_assign_revoke_permissions_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersAssignRevokePermissionsResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _remove_permissions_serialize(
        self,
        servicing_publicapi_transfers_assign_revoke_permissions_request_dto,
        project_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        if non_versioned is not None:
            _header_params['NonVersioned'] = non_versioned
        # process the form parameters
        # process the body parameter
        if servicing_publicapi_transfers_assign_revoke_permissions_request_dto is not None:
            _body_params = servicing_publicapi_transfers_assign_revoke_permissions_request_dto


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
            method='DELETE',
            resource_path='/v1/admin/permissions/users',
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




    @validate_call
    def remove_users_from_user_group(
        self,
        admin_transfers_users_to_user_groups_request_dto: AdminTransfersUsersToUserGroupsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
    ) -> AdminTransfersSecurityAssignmentResponseDTO:
        """Remove users from user groups

        This API allows you to remove users from specific user groups.   To remove users from user groups in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can remove users to user groups in multiple analytic tenants by providing a tenant code and project ID in the request body.   We recommend that administrating tenants set the analytic tenant in which to execute the API call using the `TargetTenantID` request header.

        :param admin_transfers_users_to_user_groups_request_dto: (required)
        :type admin_transfers_users_to_user_groups_request_dto: AdminTransfersUsersToUserGroupsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._remove_users_from_user_group_serialize(
            admin_transfers_users_to_user_groups_request_dto=admin_transfers_users_to_user_groups_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersSecurityAssignmentResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def remove_users_from_user_group_with_http_info(
        self,
        admin_transfers_users_to_user_groups_request_dto: AdminTransfersUsersToUserGroupsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
    ) -> ApiResponse[AdminTransfersSecurityAssignmentResponseDTO]:
        """Remove users from user groups

        This API allows you to remove users from specific user groups.   To remove users from user groups in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can remove users to user groups in multiple analytic tenants by providing a tenant code and project ID in the request body.   We recommend that administrating tenants set the analytic tenant in which to execute the API call using the `TargetTenantID` request header.

        :param admin_transfers_users_to_user_groups_request_dto: (required)
        :type admin_transfers_users_to_user_groups_request_dto: AdminTransfersUsersToUserGroupsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._remove_users_from_user_group_serialize(
            admin_transfers_users_to_user_groups_request_dto=admin_transfers_users_to_user_groups_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersSecurityAssignmentResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def remove_users_from_user_group_without_preload_content(
        self,
        admin_transfers_users_to_user_groups_request_dto: AdminTransfersUsersToUserGroupsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
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
        """Remove users from user groups

        This API allows you to remove users from specific user groups.   To remove users from user groups in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can remove users to user groups in multiple analytic tenants by providing a tenant code and project ID in the request body.   We recommend that administrating tenants set the analytic tenant in which to execute the API call using the `TargetTenantID` request header.

        :param admin_transfers_users_to_user_groups_request_dto: (required)
        :type admin_transfers_users_to_user_groups_request_dto: AdminTransfersUsersToUserGroupsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
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

        _param = self._remove_users_from_user_group_serialize(
            admin_transfers_users_to_user_groups_request_dto=admin_transfers_users_to_user_groups_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            non_versioned=non_versioned,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersSecurityAssignmentResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _remove_users_from_user_group_serialize(
        self,
        admin_transfers_users_to_user_groups_request_dto,
        project_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        if non_versioned is not None:
            _header_params['NonVersioned'] = non_versioned
        # process the form parameters
        # process the body parameter
        if admin_transfers_users_to_user_groups_request_dto is not None:
            _body_params = admin_transfers_users_to_user_groups_request_dto


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
            method='DELETE',
            resource_path='/v1/admin/user-groups/users',
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




    @validate_call
    def revoke_permissions_from_user_groups(
        self,
        admin_transfers_permissions_to_user_groups_request_dto: AdminTransfersPermissionsToUserGroupsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> AdminTransfersPermissionsToUserGroupForTenantDTO:
        """Remove permissions from user groups

        This API allows you to remove a permission from specific user groups.   To remove permissions from user groups in a project, provide a project UUID in the `ProjectID` request header.

        :param admin_transfers_permissions_to_user_groups_request_dto: (required)
        :type admin_transfers_permissions_to_user_groups_request_dto: AdminTransfersPermissionsToUserGroupsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._revoke_permissions_from_user_groups_serialize(
            admin_transfers_permissions_to_user_groups_request_dto=admin_transfers_permissions_to_user_groups_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersPermissionsToUserGroupForTenantDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def revoke_permissions_from_user_groups_with_http_info(
        self,
        admin_transfers_permissions_to_user_groups_request_dto: AdminTransfersPermissionsToUserGroupsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ApiResponse[AdminTransfersPermissionsToUserGroupForTenantDTO]:
        """Remove permissions from user groups

        This API allows you to remove a permission from specific user groups.   To remove permissions from user groups in a project, provide a project UUID in the `ProjectID` request header.

        :param admin_transfers_permissions_to_user_groups_request_dto: (required)
        :type admin_transfers_permissions_to_user_groups_request_dto: AdminTransfersPermissionsToUserGroupsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._revoke_permissions_from_user_groups_serialize(
            admin_transfers_permissions_to_user_groups_request_dto=admin_transfers_permissions_to_user_groups_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersPermissionsToUserGroupForTenantDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def revoke_permissions_from_user_groups_without_preload_content(
        self,
        admin_transfers_permissions_to_user_groups_request_dto: AdminTransfersPermissionsToUserGroupsRequestDTO,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request. If omitted, the request uses the production version.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
        """Remove permissions from user groups

        This API allows you to remove a permission from specific user groups.   To remove permissions from user groups in a project, provide a project UUID in the `ProjectID` request header.

        :param admin_transfers_permissions_to_user_groups_request_dto: (required)
        :type admin_transfers_permissions_to_user_groups_request_dto: AdminTransfersPermissionsToUserGroupsRequestDTO
        :param project_id: Optionally, specify a project in which to make the request. If omitted, the request uses the production version.
        :type project_id: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._revoke_permissions_from_user_groups_serialize(
            admin_transfers_permissions_to_user_groups_request_dto=admin_transfers_permissions_to_user_groups_request_dto,
            project_id=project_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AdminTransfersPermissionsToUserGroupForTenantDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _revoke_permissions_from_user_groups_serialize(
        self,
        admin_transfers_permissions_to_user_groups_request_dto,
        project_id,
        target_tenant_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter
        if admin_transfers_permissions_to_user_groups_request_dto is not None:
            _body_params = admin_transfers_permissions_to_user_groups_request_dto


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
            method='DELETE',
            resource_path='/v1/admin/user-groups/permissions',
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




    @validate_call
    def update_user(
        self,
        user_id: Annotated[StrictStr, Field(description="The ID of the user you want to update.")],
        servicing_publicapi_transfers_user_update_api_request_dto: ServicingPublicapiTransfersUserUpdateAPIRequestDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to update a user in.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ServicingPublicapiTransfersUserUpdateAPIRequestDTO:
        """Update a user

        Update an existing user's information, such as their display name or if the user is enabled in Visier.

        :param user_id: The ID of the user you want to update. (required)
        :type user_id: str
        :param servicing_publicapi_transfers_user_update_api_request_dto: (required)
        :type servicing_publicapi_transfers_user_update_api_request_dto: ServicingPublicapiTransfersUserUpdateAPIRequestDTO
        :param tenant_code: Specify the tenant to update a user in.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._update_user_serialize(
            user_id=user_id,
            servicing_publicapi_transfers_user_update_api_request_dto=servicing_publicapi_transfers_user_update_api_request_dto,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersUserUpdateAPIRequestDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def update_user_with_http_info(
        self,
        user_id: Annotated[StrictStr, Field(description="The ID of the user you want to update.")],
        servicing_publicapi_transfers_user_update_api_request_dto: ServicingPublicapiTransfersUserUpdateAPIRequestDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to update a user in.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
    ) -> ApiResponse[ServicingPublicapiTransfersUserUpdateAPIRequestDTO]:
        """Update a user

        Update an existing user's information, such as their display name or if the user is enabled in Visier.

        :param user_id: The ID of the user you want to update. (required)
        :type user_id: str
        :param servicing_publicapi_transfers_user_update_api_request_dto: (required)
        :type servicing_publicapi_transfers_user_update_api_request_dto: ServicingPublicapiTransfersUserUpdateAPIRequestDTO
        :param tenant_code: Specify the tenant to update a user in.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._update_user_serialize(
            user_id=user_id,
            servicing_publicapi_transfers_user_update_api_request_dto=servicing_publicapi_transfers_user_update_api_request_dto,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersUserUpdateAPIRequestDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_administration.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def update_user_without_preload_content(
        self,
        user_id: Annotated[StrictStr, Field(description="The ID of the user you want to update.")],
        servicing_publicapi_transfers_user_update_api_request_dto: ServicingPublicapiTransfersUserUpdateAPIRequestDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to update a user in.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
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
        """Update a user

        Update an existing user's information, such as their display name or if the user is enabled in Visier.

        :param user_id: The ID of the user you want to update. (required)
        :type user_id: str
        :param servicing_publicapi_transfers_user_update_api_request_dto: (required)
        :type servicing_publicapi_transfers_user_update_api_request_dto: ServicingPublicapiTransfersUserUpdateAPIRequestDTO
        :param tenant_code: Specify the tenant to update a user in.
        :type tenant_code: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
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

        _param = self._update_user_serialize(
            user_id=user_id,
            servicing_publicapi_transfers_user_update_api_request_dto=servicing_publicapi_transfers_user_update_api_request_dto,
            tenant_code=tenant_code,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingPublicapiTransfersUserUpdateAPIRequestDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _update_user_serialize(
        self,
        user_id,
        servicing_publicapi_transfers_user_update_api_request_dto,
        tenant_code,
        target_tenant_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if user_id is not None:
            _path_params['userId'] = user_id
        # process the query parameters
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter
        if servicing_publicapi_transfers_user_update_api_request_dto is not None:
            _body_params = servicing_publicapi_transfers_user_update_api_request_dto


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
            resource_path='/v1/admin/users/{userId}',
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


