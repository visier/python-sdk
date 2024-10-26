# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1547
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

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import List, Optional
from typing_extensions import Annotated
from visier_api_administration.models.bulk_data_access_set_response_dto import BulkDataAccessSetResponseDTO
from visier_api_administration.models.capability_dto import CapabilityDTO
from visier_api_administration.models.content_package_dto import ContentPackageDTO
from visier_api_administration.models.create_data_access_set_request_dto import CreateDataAccessSetRequestDTO
from visier_api_administration.models.data_access_set_dto import DataAccessSetDTO
from visier_api_administration.models.delete_permissions_request_dto import DeletePermissionsRequestDTO
from visier_api_administration.models.get_capabilities_api_response_dto import GetCapabilitiesAPIResponseDTO
from visier_api_administration.models.get_content_packages_api_response_dto import GetContentPackagesAPIResponseDTO
from visier_api_administration.models.get_data_access_sets_api_response_dto import GetDataAccessSetsAPIResponseDTO
from visier_api_administration.models.get_data_security_objects_api_response_dto import GetDataSecurityObjectsAPIResponseDTO
from visier_api_administration.models.get_permissions_api_response_dto import GetPermissionsAPIResponseDTO
from visier_api_administration.models.permission_bulk_operation_response_dto import PermissionBulkOperationResponseDTO
from visier_api_administration.models.permission_dto import PermissionDTO
from visier_api_administration.models.permissions_list_dto import PermissionsListDTO
import visier_api_administration.models


class PermissionsApi:
    """
    This class provides methods to make requests to the Visier API.
    It uses the ApiClient to handle the HTTP requests and responses.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def create_data_access_sets(
        self,
        create_data_access_set_request_dto: CreateDataAccessSetRequestDTO,
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
    ) -> BulkDataAccessSetResponseDTO:
        """Create shareable data access sets

        Create shareable data access sets. Shareable data access sets let you reuse common data access configurations in multiple permissions.   To specify the project in which to create shareable data access sets, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param create_data_access_set_request_dto: (required)
        :type create_data_access_set_request_dto: CreateDataAccessSetRequestDTO
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

        _param = self._create_data_access_sets_serialize(
            create_data_access_set_request_dto=create_data_access_set_request_dto,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BulkDataAccessSetResponseDTO",
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
    def create_data_access_sets_with_http_info(
        self,
        create_data_access_set_request_dto: CreateDataAccessSetRequestDTO,
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
    ) -> ApiResponse[BulkDataAccessSetResponseDTO]:
        """Create shareable data access sets

        Create shareable data access sets. Shareable data access sets let you reuse common data access configurations in multiple permissions.   To specify the project in which to create shareable data access sets, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param create_data_access_set_request_dto: (required)
        :type create_data_access_set_request_dto: CreateDataAccessSetRequestDTO
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

        _param = self._create_data_access_sets_serialize(
            create_data_access_set_request_dto=create_data_access_set_request_dto,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BulkDataAccessSetResponseDTO",
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
    def create_data_access_sets_without_preload_content(
        self,
        create_data_access_set_request_dto: CreateDataAccessSetRequestDTO,
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
        """Create shareable data access sets

        Create shareable data access sets. Shareable data access sets let you reuse common data access configurations in multiple permissions.   To specify the project in which to create shareable data access sets, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param create_data_access_set_request_dto: (required)
        :type create_data_access_set_request_dto: CreateDataAccessSetRequestDTO
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

        _param = self._create_data_access_sets_serialize(
            create_data_access_set_request_dto=create_data_access_set_request_dto,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BulkDataAccessSetResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_data_access_sets_serialize(
        self,
        create_data_access_set_request_dto,
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
        # process the form parameters
        # process the body parameter
        if create_data_access_set_request_dto is not None:
            _body_params = create_data_access_set_request_dto


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
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/v1/admin/data-access-sets',
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
    def create_permissions(
        self,
        permissions_list_dto: PermissionsListDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to create permissions in.")] = None,
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
    ) -> PermissionBulkOperationResponseDTO:
        """Create permissions

        Create new permissions. Administrating tenant users can specify the tenant in which to add these permissions.   To specify the project in which to create permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param permissions_list_dto: (required)
        :type permissions_list_dto: PermissionsListDTO
        :param tenant_code: Specify the tenant to create permissions in.
        :type tenant_code: str
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

        _param = self._create_permissions_serialize(
            permissions_list_dto=permissions_list_dto,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PermissionBulkOperationResponseDTO",
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
    def create_permissions_with_http_info(
        self,
        permissions_list_dto: PermissionsListDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to create permissions in.")] = None,
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
    ) -> ApiResponse[PermissionBulkOperationResponseDTO]:
        """Create permissions

        Create new permissions. Administrating tenant users can specify the tenant in which to add these permissions.   To specify the project in which to create permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param permissions_list_dto: (required)
        :type permissions_list_dto: PermissionsListDTO
        :param tenant_code: Specify the tenant to create permissions in.
        :type tenant_code: str
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

        _param = self._create_permissions_serialize(
            permissions_list_dto=permissions_list_dto,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PermissionBulkOperationResponseDTO",
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
    def create_permissions_without_preload_content(
        self,
        permissions_list_dto: PermissionsListDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to create permissions in.")] = None,
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
        """Create permissions

        Create new permissions. Administrating tenant users can specify the tenant in which to add these permissions.   To specify the project in which to create permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param permissions_list_dto: (required)
        :type permissions_list_dto: PermissionsListDTO
        :param tenant_code: Specify the tenant to create permissions in.
        :type tenant_code: str
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

        _param = self._create_permissions_serialize(
            permissions_list_dto=permissions_list_dto,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PermissionBulkOperationResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_permissions_serialize(
        self,
        permissions_list_dto,
        tenant_code,
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
        # process the form parameters
        # process the body parameter
        if permissions_list_dto is not None:
            _body_params = permissions_list_dto


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
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/v1/admin/permissions',
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
    def delete_permissions(
        self,
        delete_permissions_request_dto: DeletePermissionsRequestDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to delete permissions from.")] = None,
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
    ) -> PermissionBulkOperationResponseDTO:
        """Delete permissions

        Delete existing permissions.   To specify the project in which to delete permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param delete_permissions_request_dto: (required)
        :type delete_permissions_request_dto: DeletePermissionsRequestDTO
        :param tenant_code: Specify the tenant to delete permissions from.
        :type tenant_code: str
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

        _param = self._delete_permissions_serialize(
            delete_permissions_request_dto=delete_permissions_request_dto,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PermissionBulkOperationResponseDTO",
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
    def delete_permissions_with_http_info(
        self,
        delete_permissions_request_dto: DeletePermissionsRequestDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to delete permissions from.")] = None,
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
    ) -> ApiResponse[PermissionBulkOperationResponseDTO]:
        """Delete permissions

        Delete existing permissions.   To specify the project in which to delete permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param delete_permissions_request_dto: (required)
        :type delete_permissions_request_dto: DeletePermissionsRequestDTO
        :param tenant_code: Specify the tenant to delete permissions from.
        :type tenant_code: str
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

        _param = self._delete_permissions_serialize(
            delete_permissions_request_dto=delete_permissions_request_dto,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PermissionBulkOperationResponseDTO",
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
    def delete_permissions_without_preload_content(
        self,
        delete_permissions_request_dto: DeletePermissionsRequestDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to delete permissions from.")] = None,
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
        """Delete permissions

        Delete existing permissions.   To specify the project in which to delete permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param delete_permissions_request_dto: (required)
        :type delete_permissions_request_dto: DeletePermissionsRequestDTO
        :param tenant_code: Specify the tenant to delete permissions from.
        :type tenant_code: str
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

        _param = self._delete_permissions_serialize(
            delete_permissions_request_dto=delete_permissions_request_dto,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PermissionBulkOperationResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_permissions_serialize(
        self,
        delete_permissions_request_dto,
        tenant_code,
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
        # process the form parameters
        # process the body parameter
        if delete_permissions_request_dto is not None:
            _body_params = delete_permissions_request_dto


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
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/v1/admin/permissions',
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
    def get_capabilities(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the capabilities from.")] = None,
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
    ) -> GetCapabilitiesAPIResponseDTO:
        """Retrieve a list of all permission capabilities

        Retrieve all the permission capabilities in your tenant.  You can use the returned capabilities in other API calls when creating or updating permissions to assign the capability to the permission.   To specify the project in which to retrieve the permission capabilities, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param tenant_code: Specify the tenant to retrieve the capabilities from.
        :type tenant_code: str
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

        _param = self._get_capabilities_serialize(
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetCapabilitiesAPIResponseDTO",
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
    def get_capabilities_with_http_info(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the capabilities from.")] = None,
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
    ) -> ApiResponse[GetCapabilitiesAPIResponseDTO]:
        """Retrieve a list of all permission capabilities

        Retrieve all the permission capabilities in your tenant.  You can use the returned capabilities in other API calls when creating or updating permissions to assign the capability to the permission.   To specify the project in which to retrieve the permission capabilities, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param tenant_code: Specify the tenant to retrieve the capabilities from.
        :type tenant_code: str
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

        _param = self._get_capabilities_serialize(
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetCapabilitiesAPIResponseDTO",
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
    def get_capabilities_without_preload_content(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the capabilities from.")] = None,
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
        """Retrieve a list of all permission capabilities

        Retrieve all the permission capabilities in your tenant.  You can use the returned capabilities in other API calls when creating or updating permissions to assign the capability to the permission.   To specify the project in which to retrieve the permission capabilities, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param tenant_code: Specify the tenant to retrieve the capabilities from.
        :type tenant_code: str
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

        _param = self._get_capabilities_serialize(
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetCapabilitiesAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_capabilities_serialize(
        self,
        tenant_code,
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
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/capabilities',
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
    def get_capability(
        self,
        capability_id: Annotated[StrictStr, Field(description="The unique identifier of the capability you want to retrieve.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a capability from.")] = None,
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
    ) -> CapabilityDTO:
        """Retrieve a permission capability's details

        Retrieve the details of a specific capability.   To specify the project in which to retrieve the permission capability, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param capability_id: The unique identifier of the capability you want to retrieve. (required)
        :type capability_id: str
        :param tenant_code: Specify the tenant to retrieve a capability from.
        :type tenant_code: str
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

        _param = self._get_capability_serialize(
            capability_id=capability_id,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CapabilityDTO",
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
    def get_capability_with_http_info(
        self,
        capability_id: Annotated[StrictStr, Field(description="The unique identifier of the capability you want to retrieve.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a capability from.")] = None,
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
    ) -> ApiResponse[CapabilityDTO]:
        """Retrieve a permission capability's details

        Retrieve the details of a specific capability.   To specify the project in which to retrieve the permission capability, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param capability_id: The unique identifier of the capability you want to retrieve. (required)
        :type capability_id: str
        :param tenant_code: Specify the tenant to retrieve a capability from.
        :type tenant_code: str
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

        _param = self._get_capability_serialize(
            capability_id=capability_id,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CapabilityDTO",
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
    def get_capability_without_preload_content(
        self,
        capability_id: Annotated[StrictStr, Field(description="The unique identifier of the capability you want to retrieve.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a capability from.")] = None,
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
        """Retrieve a permission capability's details

        Retrieve the details of a specific capability.   To specify the project in which to retrieve the permission capability, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param capability_id: The unique identifier of the capability you want to retrieve. (required)
        :type capability_id: str
        :param tenant_code: Specify the tenant to retrieve a capability from.
        :type tenant_code: str
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

        _param = self._get_capability_serialize(
            capability_id=capability_id,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "CapabilityDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_capability_serialize(
        self,
        capability_id,
        tenant_code,
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
        if capability_id is not None:
            _path_params['capabilityId'] = capability_id
        # process the query parameters
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        # process the header parameters
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
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/capabilities/{capabilityId}',
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
    def get_content_package(
        self,
        content_package_id: Annotated[StrictStr, Field(description="The unique identifier of the content package you want to retrieve.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a content package from.")] = None,
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
    ) -> ContentPackageDTO:
        """Retrieve a content package's details

        Retrieve the details of a specific content package.   To specify the project in which to retrieve a content package, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param content_package_id: The unique identifier of the content package you want to retrieve. (required)
        :type content_package_id: str
        :param tenant_code: Specify the tenant to retrieve a content package from.
        :type tenant_code: str
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

        _param = self._get_content_package_serialize(
            content_package_id=content_package_id,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContentPackageDTO",
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
    def get_content_package_with_http_info(
        self,
        content_package_id: Annotated[StrictStr, Field(description="The unique identifier of the content package you want to retrieve.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a content package from.")] = None,
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
    ) -> ApiResponse[ContentPackageDTO]:
        """Retrieve a content package's details

        Retrieve the details of a specific content package.   To specify the project in which to retrieve a content package, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param content_package_id: The unique identifier of the content package you want to retrieve. (required)
        :type content_package_id: str
        :param tenant_code: Specify the tenant to retrieve a content package from.
        :type tenant_code: str
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

        _param = self._get_content_package_serialize(
            content_package_id=content_package_id,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContentPackageDTO",
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
    def get_content_package_without_preload_content(
        self,
        content_package_id: Annotated[StrictStr, Field(description="The unique identifier of the content package you want to retrieve.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a content package from.")] = None,
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
        """Retrieve a content package's details

        Retrieve the details of a specific content package.   To specify the project in which to retrieve a content package, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param content_package_id: The unique identifier of the content package you want to retrieve. (required)
        :type content_package_id: str
        :param tenant_code: Specify the tenant to retrieve a content package from.
        :type tenant_code: str
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

        _param = self._get_content_package_serialize(
            content_package_id=content_package_id,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContentPackageDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_content_package_serialize(
        self,
        content_package_id,
        tenant_code,
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
        if content_package_id is not None:
            _path_params['contentPackageId'] = content_package_id
        # process the query parameters
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        # process the header parameters
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
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/content-packages/{contentPackageId}',
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
    def get_content_packages(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the content packages from.")] = None,
        search_string: Annotated[Optional[StrictStr], Field(description="Optional search string to return only content packages whose display name or description contains that search string.  If searchString is empty or not provided, the response returns a list of all content packages.")] = None,
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
    ) -> GetContentPackagesAPIResponseDTO:
        """Retrieve a list of all content packages

        Retrieve the list of available content packages.  You can use the returned content packages in other API calls when creating or updating permissions to add the content package to the permission.   To specify the project in which to retrieve the available content packages, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param tenant_code: Specify the tenant to retrieve the content packages from.
        :type tenant_code: str
        :param search_string: Optional search string to return only content packages whose display name or description contains that search string.  If searchString is empty or not provided, the response returns a list of all content packages.
        :type search_string: str
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

        _param = self._get_content_packages_serialize(
            tenant_code=tenant_code,
            search_string=search_string,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetContentPackagesAPIResponseDTO",
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
    def get_content_packages_with_http_info(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the content packages from.")] = None,
        search_string: Annotated[Optional[StrictStr], Field(description="Optional search string to return only content packages whose display name or description contains that search string.  If searchString is empty or not provided, the response returns a list of all content packages.")] = None,
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
    ) -> ApiResponse[GetContentPackagesAPIResponseDTO]:
        """Retrieve a list of all content packages

        Retrieve the list of available content packages.  You can use the returned content packages in other API calls when creating or updating permissions to add the content package to the permission.   To specify the project in which to retrieve the available content packages, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param tenant_code: Specify the tenant to retrieve the content packages from.
        :type tenant_code: str
        :param search_string: Optional search string to return only content packages whose display name or description contains that search string.  If searchString is empty or not provided, the response returns a list of all content packages.
        :type search_string: str
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

        _param = self._get_content_packages_serialize(
            tenant_code=tenant_code,
            search_string=search_string,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetContentPackagesAPIResponseDTO",
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
    def get_content_packages_without_preload_content(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the content packages from.")] = None,
        search_string: Annotated[Optional[StrictStr], Field(description="Optional search string to return only content packages whose display name or description contains that search string.  If searchString is empty or not provided, the response returns a list of all content packages.")] = None,
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
        """Retrieve a list of all content packages

        Retrieve the list of available content packages.  You can use the returned content packages in other API calls when creating or updating permissions to add the content package to the permission.   To specify the project in which to retrieve the available content packages, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param tenant_code: Specify the tenant to retrieve the content packages from.
        :type tenant_code: str
        :param search_string: Optional search string to return only content packages whose display name or description contains that search string.  If searchString is empty or not provided, the response returns a list of all content packages.
        :type search_string: str
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

        _param = self._get_content_packages_serialize(
            tenant_code=tenant_code,
            search_string=search_string,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetContentPackagesAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_content_packages_serialize(
        self,
        tenant_code,
        search_string,
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
            
        if search_string is not None:
            
            _query_params.append(('searchString', search_string))
            
        # process the header parameters
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
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/content-packages',
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
    def get_data_access_set(
        self,
        data_access_set_id: Annotated[StrictStr, Field(description="The unique identifier of the data access set you want to retrieve.")],
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
    ) -> DataAccessSetDTO:
        """Retrieve a data access set's details

        Retrieve the details of a specific shareable data access set. You must know the ID of the data access set to retrieve its details. To retrieve data access set IDs, see `GET v1/admin/data-access-sets`.   To specify the project in which to retrieve the shareable data access set, provide a project UUID in the `ProjectID` request header.   **Note:** This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).

        :param data_access_set_id: The unique identifier of the data access set you want to retrieve. (required)
        :type data_access_set_id: str
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

        _param = self._get_data_access_set_serialize(
            data_access_set_id=data_access_set_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DataAccessSetDTO",
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
    def get_data_access_set_with_http_info(
        self,
        data_access_set_id: Annotated[StrictStr, Field(description="The unique identifier of the data access set you want to retrieve.")],
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
    ) -> ApiResponse[DataAccessSetDTO]:
        """Retrieve a data access set's details

        Retrieve the details of a specific shareable data access set. You must know the ID of the data access set to retrieve its details. To retrieve data access set IDs, see `GET v1/admin/data-access-sets`.   To specify the project in which to retrieve the shareable data access set, provide a project UUID in the `ProjectID` request header.   **Note:** This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).

        :param data_access_set_id: The unique identifier of the data access set you want to retrieve. (required)
        :type data_access_set_id: str
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

        _param = self._get_data_access_set_serialize(
            data_access_set_id=data_access_set_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DataAccessSetDTO",
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
    def get_data_access_set_without_preload_content(
        self,
        data_access_set_id: Annotated[StrictStr, Field(description="The unique identifier of the data access set you want to retrieve.")],
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
        """Retrieve a data access set's details

        Retrieve the details of a specific shareable data access set. You must know the ID of the data access set to retrieve its details. To retrieve data access set IDs, see `GET v1/admin/data-access-sets`.   To specify the project in which to retrieve the shareable data access set, provide a project UUID in the `ProjectID` request header.   **Note:** This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).

        :param data_access_set_id: The unique identifier of the data access set you want to retrieve. (required)
        :type data_access_set_id: str
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

        _param = self._get_data_access_set_serialize(
            data_access_set_id=data_access_set_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DataAccessSetDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_data_access_set_serialize(
        self,
        data_access_set_id,
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
        if data_access_set_id is not None:
            _path_params['dataAccessSetId'] = data_access_set_id
        # process the query parameters
        # process the header parameters
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
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/data-access-sets/{dataAccessSetId}',
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
    def get_data_access_sets(
        self,
        analytic_object_id: Annotated[Optional[StrictStr], Field(description="Specify the analytic object ID to retrieve the shareable data access sets for. Default is all analytic objects.")] = None,
        var_with: Annotated[Optional[List[StrictStr]], Field(description="The information about the data access set to include in the request response.  * If empty, returns basic information for the data access set, including its unique ID, display name, description, and analytic object ID.  * If `details`, returns basic information and property data access information (`propertyAccessConfigs`).")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The maximum number of data access sets to return. Default is 100. Maximum is 1000.")] = None,
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
    ) -> GetDataAccessSetsAPIResponseDTO:
        """Retrieve a list of all data access sets

        Retrieve a list of all shareable data access sets. Data access sets define the level of access that users have to properties and property values for the analytic object in a permission. Data access sets also grant access to properties of subjects that are referenced by the analytic object in the permission.  You can assign data access sets to a permission when creating or updating permissions.   To specify the project in which to retrieve the shareable data access sets, provide a project UUID in the `ProjectID` request header.   **Note:**   * If the number of valid data access sets exceeds the default limit of 100, the response status code is 206. To retrieve more than 100 data access sets, set `limit` to a higher number.  * This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).

        :param analytic_object_id: Specify the analytic object ID to retrieve the shareable data access sets for. Default is all analytic objects.
        :type analytic_object_id: str
        :param var_with: The information about the data access set to include in the request response.  * If empty, returns basic information for the data access set, including its unique ID, display name, description, and analytic object ID.  * If `details`, returns basic information and property data access information (`propertyAccessConfigs`).
        :type var_with: List[str]
        :param limit: The maximum number of data access sets to return. Default is 100. Maximum is 1000.
        :type limit: int
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

        _param = self._get_data_access_sets_serialize(
            analytic_object_id=analytic_object_id,
            var_with=var_with,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetDataAccessSetsAPIResponseDTO",
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
    def get_data_access_sets_with_http_info(
        self,
        analytic_object_id: Annotated[Optional[StrictStr], Field(description="Specify the analytic object ID to retrieve the shareable data access sets for. Default is all analytic objects.")] = None,
        var_with: Annotated[Optional[List[StrictStr]], Field(description="The information about the data access set to include in the request response.  * If empty, returns basic information for the data access set, including its unique ID, display name, description, and analytic object ID.  * If `details`, returns basic information and property data access information (`propertyAccessConfigs`).")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The maximum number of data access sets to return. Default is 100. Maximum is 1000.")] = None,
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
    ) -> ApiResponse[GetDataAccessSetsAPIResponseDTO]:
        """Retrieve a list of all data access sets

        Retrieve a list of all shareable data access sets. Data access sets define the level of access that users have to properties and property values for the analytic object in a permission. Data access sets also grant access to properties of subjects that are referenced by the analytic object in the permission.  You can assign data access sets to a permission when creating or updating permissions.   To specify the project in which to retrieve the shareable data access sets, provide a project UUID in the `ProjectID` request header.   **Note:**   * If the number of valid data access sets exceeds the default limit of 100, the response status code is 206. To retrieve more than 100 data access sets, set `limit` to a higher number.  * This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).

        :param analytic_object_id: Specify the analytic object ID to retrieve the shareable data access sets for. Default is all analytic objects.
        :type analytic_object_id: str
        :param var_with: The information about the data access set to include in the request response.  * If empty, returns basic information for the data access set, including its unique ID, display name, description, and analytic object ID.  * If `details`, returns basic information and property data access information (`propertyAccessConfigs`).
        :type var_with: List[str]
        :param limit: The maximum number of data access sets to return. Default is 100. Maximum is 1000.
        :type limit: int
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

        _param = self._get_data_access_sets_serialize(
            analytic_object_id=analytic_object_id,
            var_with=var_with,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetDataAccessSetsAPIResponseDTO",
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
    def get_data_access_sets_without_preload_content(
        self,
        analytic_object_id: Annotated[Optional[StrictStr], Field(description="Specify the analytic object ID to retrieve the shareable data access sets for. Default is all analytic objects.")] = None,
        var_with: Annotated[Optional[List[StrictStr]], Field(description="The information about the data access set to include in the request response.  * If empty, returns basic information for the data access set, including its unique ID, display name, description, and analytic object ID.  * If `details`, returns basic information and property data access information (`propertyAccessConfigs`).")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The maximum number of data access sets to return. Default is 100. Maximum is 1000.")] = None,
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
        """Retrieve a list of all data access sets

        Retrieve a list of all shareable data access sets. Data access sets define the level of access that users have to properties and property values for the analytic object in a permission. Data access sets also grant access to properties of subjects that are referenced by the analytic object in the permission.  You can assign data access sets to a permission when creating or updating permissions.   To specify the project in which to retrieve the shareable data access sets, provide a project UUID in the `ProjectID` request header.   **Note:**   * If the number of valid data access sets exceeds the default limit of 100, the response status code is 206. To retrieve more than 100 data access sets, set `limit` to a higher number.  * This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).

        :param analytic_object_id: Specify the analytic object ID to retrieve the shareable data access sets for. Default is all analytic objects.
        :type analytic_object_id: str
        :param var_with: The information about the data access set to include in the request response.  * If empty, returns basic information for the data access set, including its unique ID, display name, description, and analytic object ID.  * If `details`, returns basic information and property data access information (`propertyAccessConfigs`).
        :type var_with: List[str]
        :param limit: The maximum number of data access sets to return. Default is 100. Maximum is 1000.
        :type limit: int
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

        _param = self._get_data_access_sets_serialize(
            analytic_object_id=analytic_object_id,
            var_with=var_with,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetDataAccessSetsAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_data_access_sets_serialize(
        self,
        analytic_object_id,
        var_with,
        limit,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'with': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if analytic_object_id is not None:
            
            _query_params.append(('analyticObjectId', analytic_object_id))
            
        if var_with is not None:
            
            _query_params.append(('with', var_with))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        # process the header parameters
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
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/data-access-sets',
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
    def get_data_security_objects(
        self,
        id: Annotated[Optional[List[StrictStr]], Field(description="The unique identifiers of the data security objects (analytic objects) to retrieve.  Default is all data security objects.")] = None,
        include_details: Annotated[Optional[StrictBool], Field(description="If `true`, the response includes the analytic objects (display name, ID, and object type), related objects,  securable properties, and securable dimensions. If `false`, the response only includes analytic objects  (display name, ID, and object type). Default is `false`.")] = None,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve data security objects from.")] = None,
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
    ) -> GetDataSecurityObjectsAPIResponseDTO:
        """Retrieve a list of data security objects

        Retrieve the list of available data security objects.  Data security objects are analytic objects and their related objects that are available to define  permissions' data security profiles.   To specify the project in which to retrieve the available data security objects, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param id: The unique identifiers of the data security objects (analytic objects) to retrieve.  Default is all data security objects.
        :type id: List[str]
        :param include_details: If `true`, the response includes the analytic objects (display name, ID, and object type), related objects,  securable properties, and securable dimensions. If `false`, the response only includes analytic objects  (display name, ID, and object type). Default is `false`.
        :type include_details: bool
        :param tenant_code: Specify the tenant to retrieve data security objects from.
        :type tenant_code: str
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

        _param = self._get_data_security_objects_serialize(
            id=id,
            include_details=include_details,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetDataSecurityObjectsAPIResponseDTO",
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
    def get_data_security_objects_with_http_info(
        self,
        id: Annotated[Optional[List[StrictStr]], Field(description="The unique identifiers of the data security objects (analytic objects) to retrieve.  Default is all data security objects.")] = None,
        include_details: Annotated[Optional[StrictBool], Field(description="If `true`, the response includes the analytic objects (display name, ID, and object type), related objects,  securable properties, and securable dimensions. If `false`, the response only includes analytic objects  (display name, ID, and object type). Default is `false`.")] = None,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve data security objects from.")] = None,
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
    ) -> ApiResponse[GetDataSecurityObjectsAPIResponseDTO]:
        """Retrieve a list of data security objects

        Retrieve the list of available data security objects.  Data security objects are analytic objects and their related objects that are available to define  permissions' data security profiles.   To specify the project in which to retrieve the available data security objects, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param id: The unique identifiers of the data security objects (analytic objects) to retrieve.  Default is all data security objects.
        :type id: List[str]
        :param include_details: If `true`, the response includes the analytic objects (display name, ID, and object type), related objects,  securable properties, and securable dimensions. If `false`, the response only includes analytic objects  (display name, ID, and object type). Default is `false`.
        :type include_details: bool
        :param tenant_code: Specify the tenant to retrieve data security objects from.
        :type tenant_code: str
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

        _param = self._get_data_security_objects_serialize(
            id=id,
            include_details=include_details,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetDataSecurityObjectsAPIResponseDTO",
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
    def get_data_security_objects_without_preload_content(
        self,
        id: Annotated[Optional[List[StrictStr]], Field(description="The unique identifiers of the data security objects (analytic objects) to retrieve.  Default is all data security objects.")] = None,
        include_details: Annotated[Optional[StrictBool], Field(description="If `true`, the response includes the analytic objects (display name, ID, and object type), related objects,  securable properties, and securable dimensions. If `false`, the response only includes analytic objects  (display name, ID, and object type). Default is `false`.")] = None,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve data security objects from.")] = None,
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
        """Retrieve a list of data security objects

        Retrieve the list of available data security objects.  Data security objects are analytic objects and their related objects that are available to define  permissions' data security profiles.   To specify the project in which to retrieve the available data security objects, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param id: The unique identifiers of the data security objects (analytic objects) to retrieve.  Default is all data security objects.
        :type id: List[str]
        :param include_details: If `true`, the response includes the analytic objects (display name, ID, and object type), related objects,  securable properties, and securable dimensions. If `false`, the response only includes analytic objects  (display name, ID, and object type). Default is `false`.
        :type include_details: bool
        :param tenant_code: Specify the tenant to retrieve data security objects from.
        :type tenant_code: str
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

        _param = self._get_data_security_objects_serialize(
            id=id,
            include_details=include_details,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetDataSecurityObjectsAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_data_security_objects_serialize(
        self,
        id,
        include_details,
        tenant_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'id': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if id is not None:
            
            _query_params.append(('id', id))
            
        if include_details is not None:
            
            _query_params.append(('includeDetails', include_details))
            
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        # process the header parameters
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
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/data-security-objects',
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
    def get_permission(
        self,
        permission_id: Annotated[StrictStr, Field(description="The unique identifier of the permission you want to retrieve.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a permission from.")] = None,
        include_details_with_status: Annotated[Optional[StrictStr], Field(description="If `true`, returns the validity statuses for the permission's properties in data access sets and the  permission's dimensions, dimension members, and hierarchy properties in member filters. If `false`,  doesn't return validity status information. Default is `false`.")] = None,
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
    ) -> PermissionDTO:
        """Retrieve a permission's details

        Retrieve the details for a specified permission.   To specify the project in which to retrieve the permission, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param permission_id: The unique identifier of the permission you want to retrieve. (required)
        :type permission_id: str
        :param tenant_code: Specify the tenant to retrieve a permission from.
        :type tenant_code: str
        :param include_details_with_status: If `true`, returns the validity statuses for the permission's properties in data access sets and the  permission's dimensions, dimension members, and hierarchy properties in member filters. If `false`,  doesn't return validity status information. Default is `false`.
        :type include_details_with_status: str
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

        _param = self._get_permission_serialize(
            permission_id=permission_id,
            tenant_code=tenant_code,
            include_details_with_status=include_details_with_status,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PermissionDTO",
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
    def get_permission_with_http_info(
        self,
        permission_id: Annotated[StrictStr, Field(description="The unique identifier of the permission you want to retrieve.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a permission from.")] = None,
        include_details_with_status: Annotated[Optional[StrictStr], Field(description="If `true`, returns the validity statuses for the permission's properties in data access sets and the  permission's dimensions, dimension members, and hierarchy properties in member filters. If `false`,  doesn't return validity status information. Default is `false`.")] = None,
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
    ) -> ApiResponse[PermissionDTO]:
        """Retrieve a permission's details

        Retrieve the details for a specified permission.   To specify the project in which to retrieve the permission, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param permission_id: The unique identifier of the permission you want to retrieve. (required)
        :type permission_id: str
        :param tenant_code: Specify the tenant to retrieve a permission from.
        :type tenant_code: str
        :param include_details_with_status: If `true`, returns the validity statuses for the permission's properties in data access sets and the  permission's dimensions, dimension members, and hierarchy properties in member filters. If `false`,  doesn't return validity status information. Default is `false`.
        :type include_details_with_status: str
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

        _param = self._get_permission_serialize(
            permission_id=permission_id,
            tenant_code=tenant_code,
            include_details_with_status=include_details_with_status,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PermissionDTO",
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
    def get_permission_without_preload_content(
        self,
        permission_id: Annotated[StrictStr, Field(description="The unique identifier of the permission you want to retrieve.")],
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve a permission from.")] = None,
        include_details_with_status: Annotated[Optional[StrictStr], Field(description="If `true`, returns the validity statuses for the permission's properties in data access sets and the  permission's dimensions, dimension members, and hierarchy properties in member filters. If `false`,  doesn't return validity status information. Default is `false`.")] = None,
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
        """Retrieve a permission's details

        Retrieve the details for a specified permission.   To specify the project in which to retrieve the permission, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param permission_id: The unique identifier of the permission you want to retrieve. (required)
        :type permission_id: str
        :param tenant_code: Specify the tenant to retrieve a permission from.
        :type tenant_code: str
        :param include_details_with_status: If `true`, returns the validity statuses for the permission's properties in data access sets and the  permission's dimensions, dimension members, and hierarchy properties in member filters. If `false`,  doesn't return validity status information. Default is `false`.
        :type include_details_with_status: str
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

        _param = self._get_permission_serialize(
            permission_id=permission_id,
            tenant_code=tenant_code,
            include_details_with_status=include_details_with_status,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PermissionDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_permission_serialize(
        self,
        permission_id,
        tenant_code,
        include_details_with_status,
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
        if tenant_code is not None:
            
            _query_params.append(('tenantCode', tenant_code))
            
        if include_details_with_status is not None:
            
            _query_params.append(('includeDetailsWithStatus', include_details_with_status))
            
        # process the header parameters
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
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/permissions/{permissionId}',
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
    def get_permissions(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the permissions from.")] = None,
        include_details: Annotated[Optional[StrictBool], Field(description="If `true`, returns the permission's details. If `false`, only returns the permissions' ID, display name,  and description. Default is `false`.")] = None,
        include_details_with_status: Annotated[Optional[StrictBool], Field(description="If `true`, returns the validity statuses for the permission's properties in data access sets and the  permission's dimensions, dimension members, and hierarchy properties in member filters. If `false`,  doesn't return validity status information. Default is `false`.")] = None,
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
    ) -> GetPermissionsAPIResponseDTO:
        """Retrieve a list of all permissions

        Retrieve the full list of user permissions in your tenant.   To specify the project in which to retrieve permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param tenant_code: Specify the tenant to retrieve the permissions from.
        :type tenant_code: str
        :param include_details: If `true`, returns the permission's details. If `false`, only returns the permissions' ID, display name,  and description. Default is `false`.
        :type include_details: bool
        :param include_details_with_status: If `true`, returns the validity statuses for the permission's properties in data access sets and the  permission's dimensions, dimension members, and hierarchy properties in member filters. If `false`,  doesn't return validity status information. Default is `false`.
        :type include_details_with_status: bool
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

        _param = self._get_permissions_serialize(
            tenant_code=tenant_code,
            include_details=include_details,
            include_details_with_status=include_details_with_status,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetPermissionsAPIResponseDTO",
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
    def get_permissions_with_http_info(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the permissions from.")] = None,
        include_details: Annotated[Optional[StrictBool], Field(description="If `true`, returns the permission's details. If `false`, only returns the permissions' ID, display name,  and description. Default is `false`.")] = None,
        include_details_with_status: Annotated[Optional[StrictBool], Field(description="If `true`, returns the validity statuses for the permission's properties in data access sets and the  permission's dimensions, dimension members, and hierarchy properties in member filters. If `false`,  doesn't return validity status information. Default is `false`.")] = None,
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
    ) -> ApiResponse[GetPermissionsAPIResponseDTO]:
        """Retrieve a list of all permissions

        Retrieve the full list of user permissions in your tenant.   To specify the project in which to retrieve permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param tenant_code: Specify the tenant to retrieve the permissions from.
        :type tenant_code: str
        :param include_details: If `true`, returns the permission's details. If `false`, only returns the permissions' ID, display name,  and description. Default is `false`.
        :type include_details: bool
        :param include_details_with_status: If `true`, returns the validity statuses for the permission's properties in data access sets and the  permission's dimensions, dimension members, and hierarchy properties in member filters. If `false`,  doesn't return validity status information. Default is `false`.
        :type include_details_with_status: bool
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

        _param = self._get_permissions_serialize(
            tenant_code=tenant_code,
            include_details=include_details,
            include_details_with_status=include_details_with_status,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetPermissionsAPIResponseDTO",
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
    def get_permissions_without_preload_content(
        self,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to retrieve the permissions from.")] = None,
        include_details: Annotated[Optional[StrictBool], Field(description="If `true`, returns the permission's details. If `false`, only returns the permissions' ID, display name,  and description. Default is `false`.")] = None,
        include_details_with_status: Annotated[Optional[StrictBool], Field(description="If `true`, returns the validity statuses for the permission's properties in data access sets and the  permission's dimensions, dimension members, and hierarchy properties in member filters. If `false`,  doesn't return validity status information. Default is `false`.")] = None,
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
        """Retrieve a list of all permissions

        Retrieve the full list of user permissions in your tenant.   To specify the project in which to retrieve permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param tenant_code: Specify the tenant to retrieve the permissions from.
        :type tenant_code: str
        :param include_details: If `true`, returns the permission's details. If `false`, only returns the permissions' ID, display name,  and description. Default is `false`.
        :type include_details: bool
        :param include_details_with_status: If `true`, returns the validity statuses for the permission's properties in data access sets and the  permission's dimensions, dimension members, and hierarchy properties in member filters. If `false`,  doesn't return validity status information. Default is `false`.
        :type include_details_with_status: bool
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

        _param = self._get_permissions_serialize(
            tenant_code=tenant_code,
            include_details=include_details,
            include_details_with_status=include_details_with_status,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetPermissionsAPIResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_permissions_serialize(
        self,
        tenant_code,
        include_details,
        include_details_with_status,
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
            
        if include_details is not None:
            
            _query_params.append(('includeDetails', include_details))
            
        if include_details_with_status is not None:
            
            _query_params.append(('includeDetailsWithStatus', include_details_with_status))
            
        # process the header parameters
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
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/v1/admin/permissions',
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
    def update_permissions(
        self,
        permissions_list_dto: PermissionsListDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to update permissions in.")] = None,
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
    ) -> PermissionBulkOperationResponseDTO:
        """Update permissions

        Update existing permissions.   To specify the project in which to update permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param permissions_list_dto: (required)
        :type permissions_list_dto: PermissionsListDTO
        :param tenant_code: Specify the tenant to update permissions in.
        :type tenant_code: str
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

        _param = self._update_permissions_serialize(
            permissions_list_dto=permissions_list_dto,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PermissionBulkOperationResponseDTO",
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
    def update_permissions_with_http_info(
        self,
        permissions_list_dto: PermissionsListDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to update permissions in.")] = None,
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
    ) -> ApiResponse[PermissionBulkOperationResponseDTO]:
        """Update permissions

        Update existing permissions.   To specify the project in which to update permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param permissions_list_dto: (required)
        :type permissions_list_dto: PermissionsListDTO
        :param tenant_code: Specify the tenant to update permissions in.
        :type tenant_code: str
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

        _param = self._update_permissions_serialize(
            permissions_list_dto=permissions_list_dto,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PermissionBulkOperationResponseDTO",
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
    def update_permissions_without_preload_content(
        self,
        permissions_list_dto: PermissionsListDTO,
        tenant_code: Annotated[Optional[StrictStr], Field(description="Specify the tenant to update permissions in.")] = None,
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
        """Update permissions

        Update existing permissions.   To specify the project in which to update permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

        :param permissions_list_dto: (required)
        :type permissions_list_dto: PermissionsListDTO
        :param tenant_code: Specify the tenant to update permissions in.
        :type tenant_code: str
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

        _param = self._update_permissions_serialize(
            permissions_list_dto=permissions_list_dto,
            tenant_code=tenant_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PermissionBulkOperationResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _update_permissions_serialize(
        self,
        permissions_list_dto,
        tenant_code,
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
        # process the form parameters
        # process the body parameter
        if permissions_list_dto is not None:
            _body_params = permissions_list_dto


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
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/v1/admin/permissions',
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


