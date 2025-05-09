# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1892
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

from pydantic import Field, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_bulk_change_response_dto import ServicingV2ObjectconfigurationBulkChangeResponseDTO
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_concept_delete_request_dto import ServicingV2ObjectconfigurationConceptDeleteRequestDTO
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_concept_request_dto import ServicingV2ObjectconfigurationConceptRequestDTO
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_concept_response_dto import ServicingV2ObjectconfigurationConceptResponseDTO
import visier_api_analytic_model.models


class ConceptsV2Api:
    """
    This class provides methods to make requests to the Visier API.
    It uses the ApiClient to handle the HTTP requests and responses.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def create_concepts(
        self,
        servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
    ) -> ServicingV2ObjectconfigurationBulkChangeResponseDTO:
        """Create concepts

        Create new concepts. The response returns whether each concept was successfully created or not.  When creating objects, assign a unique object name but don't set a UUID. Visier generates UUIDs for new objects.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param servicing_v2_objectconfiguration_concept_request_dto: (required)
        :type servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._create_concepts_serialize(
            servicing_v2_objectconfiguration_concept_request_dto=servicing_v2_objectconfiguration_concept_request_dto,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationBulkChangeResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_analytic_model.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def create_concepts_with_http_info(
        self,
        servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
    ) -> ApiResponse[ServicingV2ObjectconfigurationBulkChangeResponseDTO]:
        """Create concepts

        Create new concepts. The response returns whether each concept was successfully created or not.  When creating objects, assign a unique object name but don't set a UUID. Visier generates UUIDs for new objects.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param servicing_v2_objectconfiguration_concept_request_dto: (required)
        :type servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._create_concepts_serialize(
            servicing_v2_objectconfiguration_concept_request_dto=servicing_v2_objectconfiguration_concept_request_dto,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationBulkChangeResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_analytic_model.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def create_concepts_without_preload_content(
        self,
        servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
        """Create concepts

        Create new concepts. The response returns whether each concept was successfully created or not.  When creating objects, assign a unique object name but don't set a UUID. Visier generates UUIDs for new objects.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param servicing_v2_objectconfiguration_concept_request_dto: (required)
        :type servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._create_concepts_serialize(
            servicing_v2_objectconfiguration_concept_request_dto=servicing_v2_objectconfiguration_concept_request_dto,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationBulkChangeResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_concepts_serialize(
        self,
        servicing_v2_objectconfiguration_concept_request_dto,
        target_tenant_id,
        project_id,
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
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        # process the form parameters
        # process the body parameter
        if servicing_v2_objectconfiguration_concept_request_dto is not None:
            _body_params = servicing_v2_objectconfiguration_concept_request_dto


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
            resource_path='/v2alpha/data/model/concepts',
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
    def delete_concepts(
        self,
        servicing_v2_objectconfiguration_concept_delete_request_dto: ServicingV2ObjectconfigurationConceptDeleteRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
    ) -> ServicingV2ObjectconfigurationBulkChangeResponseDTO:
        """Delete concepts

        Delete existing concepts. The response returns whether each concept was successfully deleted or not.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param servicing_v2_objectconfiguration_concept_delete_request_dto: (required)
        :type servicing_v2_objectconfiguration_concept_delete_request_dto: ServicingV2ObjectconfigurationConceptDeleteRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._delete_concepts_serialize(
            servicing_v2_objectconfiguration_concept_delete_request_dto=servicing_v2_objectconfiguration_concept_delete_request_dto,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationBulkChangeResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_analytic_model.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def delete_concepts_with_http_info(
        self,
        servicing_v2_objectconfiguration_concept_delete_request_dto: ServicingV2ObjectconfigurationConceptDeleteRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
    ) -> ApiResponse[ServicingV2ObjectconfigurationBulkChangeResponseDTO]:
        """Delete concepts

        Delete existing concepts. The response returns whether each concept was successfully deleted or not.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param servicing_v2_objectconfiguration_concept_delete_request_dto: (required)
        :type servicing_v2_objectconfiguration_concept_delete_request_dto: ServicingV2ObjectconfigurationConceptDeleteRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._delete_concepts_serialize(
            servicing_v2_objectconfiguration_concept_delete_request_dto=servicing_v2_objectconfiguration_concept_delete_request_dto,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationBulkChangeResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_analytic_model.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def delete_concepts_without_preload_content(
        self,
        servicing_v2_objectconfiguration_concept_delete_request_dto: ServicingV2ObjectconfigurationConceptDeleteRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
        """Delete concepts

        Delete existing concepts. The response returns whether each concept was successfully deleted or not.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param servicing_v2_objectconfiguration_concept_delete_request_dto: (required)
        :type servicing_v2_objectconfiguration_concept_delete_request_dto: ServicingV2ObjectconfigurationConceptDeleteRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._delete_concepts_serialize(
            servicing_v2_objectconfiguration_concept_delete_request_dto=servicing_v2_objectconfiguration_concept_delete_request_dto,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationBulkChangeResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_concepts_serialize(
        self,
        servicing_v2_objectconfiguration_concept_delete_request_dto,
        target_tenant_id,
        project_id,
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
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        # process the form parameters
        # process the body parameter
        if servicing_v2_objectconfiguration_concept_delete_request_dto is not None:
            _body_params = servicing_v2_objectconfiguration_concept_delete_request_dto


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
            resource_path='/v2alpha/data/model/concepts',
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
    def get_all_concepts(
        self,
        type: Annotated[Optional[List[StrictStr]], Field(description="The type of the concept to retrieve. Valid values:  - `process`: Retrieves all process concepts. This is the default.")] = None,
        var_with: Annotated[Optional[List[StrictStr]], Field(description="The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.")] = None,
        object_name: Annotated[Optional[List[StrictStr]], Field(description="The concept object names to return in the response. When combined with `uuid`, the results return objects that match either the `objectName` or `uuid`.")] = None,
        uuid: Annotated[Optional[List[StrictStr]], Field(description="The concept UUIDs to return in the response. When combined with `objectName`, the results return objects that match either the `objectName` or `uuid`.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
    ) -> ServicingV2ObjectconfigurationConceptResponseDTO:
        """Retrieve a list of concepts

        Retrieve a list of all concepts in your Visier tenant.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param type: The type of the concept to retrieve. Valid values:  - `process`: Retrieves all process concepts. This is the default.
        :type type: List[str]
        :param var_with: The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.
        :type var_with: List[str]
        :param object_name: The concept object names to return in the response. When combined with `uuid`, the results return objects that match either the `objectName` or `uuid`.
        :type object_name: List[str]
        :param uuid: The concept UUIDs to return in the response. When combined with `objectName`, the results return objects that match either the `objectName` or `uuid`.
        :type uuid: List[str]
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._get_all_concepts_serialize(
            type=type,
            var_with=var_with,
            object_name=object_name,
            uuid=uuid,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationConceptResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_analytic_model.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_all_concepts_with_http_info(
        self,
        type: Annotated[Optional[List[StrictStr]], Field(description="The type of the concept to retrieve. Valid values:  - `process`: Retrieves all process concepts. This is the default.")] = None,
        var_with: Annotated[Optional[List[StrictStr]], Field(description="The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.")] = None,
        object_name: Annotated[Optional[List[StrictStr]], Field(description="The concept object names to return in the response. When combined with `uuid`, the results return objects that match either the `objectName` or `uuid`.")] = None,
        uuid: Annotated[Optional[List[StrictStr]], Field(description="The concept UUIDs to return in the response. When combined with `objectName`, the results return objects that match either the `objectName` or `uuid`.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
    ) -> ApiResponse[ServicingV2ObjectconfigurationConceptResponseDTO]:
        """Retrieve a list of concepts

        Retrieve a list of all concepts in your Visier tenant.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param type: The type of the concept to retrieve. Valid values:  - `process`: Retrieves all process concepts. This is the default.
        :type type: List[str]
        :param var_with: The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.
        :type var_with: List[str]
        :param object_name: The concept object names to return in the response. When combined with `uuid`, the results return objects that match either the `objectName` or `uuid`.
        :type object_name: List[str]
        :param uuid: The concept UUIDs to return in the response. When combined with `objectName`, the results return objects that match either the `objectName` or `uuid`.
        :type uuid: List[str]
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._get_all_concepts_serialize(
            type=type,
            var_with=var_with,
            object_name=object_name,
            uuid=uuid,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationConceptResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_analytic_model.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_all_concepts_without_preload_content(
        self,
        type: Annotated[Optional[List[StrictStr]], Field(description="The type of the concept to retrieve. Valid values:  - `process`: Retrieves all process concepts. This is the default.")] = None,
        var_with: Annotated[Optional[List[StrictStr]], Field(description="The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.")] = None,
        object_name: Annotated[Optional[List[StrictStr]], Field(description="The concept object names to return in the response. When combined with `uuid`, the results return objects that match either the `objectName` or `uuid`.")] = None,
        uuid: Annotated[Optional[List[StrictStr]], Field(description="The concept UUIDs to return in the response. When combined with `objectName`, the results return objects that match either the `objectName` or `uuid`.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
        """Retrieve a list of concepts

        Retrieve a list of all concepts in your Visier tenant.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param type: The type of the concept to retrieve. Valid values:  - `process`: Retrieves all process concepts. This is the default.
        :type type: List[str]
        :param var_with: The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.
        :type var_with: List[str]
        :param object_name: The concept object names to return in the response. When combined with `uuid`, the results return objects that match either the `objectName` or `uuid`.
        :type object_name: List[str]
        :param uuid: The concept UUIDs to return in the response. When combined with `objectName`, the results return objects that match either the `objectName` or `uuid`.
        :type uuid: List[str]
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._get_all_concepts_serialize(
            type=type,
            var_with=var_with,
            object_name=object_name,
            uuid=uuid,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationConceptResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_all_concepts_serialize(
        self,
        type,
        var_with,
        object_name,
        uuid,
        target_tenant_id,
        project_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'type': 'multi',
            'with': 'multi',
            'objectName': 'multi',
            'uuid': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if type is not None:
            
            _query_params.append(('type', type))
            
        if var_with is not None:
            
            _query_params.append(('with', var_with))
            
        if object_name is not None:
            
            _query_params.append(('objectName', object_name))
            
        if uuid is not None:
            
            _query_params.append(('uuid', uuid))
            
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        if project_id is not None:
            _header_params['ProjectID'] = project_id
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
            resource_path='/v2alpha/data/model/concepts',
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
    def get_analytic_object_concepts(
        self,
        analytic_object_name: Annotated[StrictStr, Field(description="The object name of the analytic object from which to retrieve concepts.")],
        type: Annotated[Optional[List[StrictStr]], Field(description="The type of the concept to retrieve. Valid values:  - `process`: Retrieves all process concepts. This is the default.")] = None,
        var_with: Annotated[Optional[List[StrictStr]], Field(description="The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.")] = None,
        object_name: Annotated[Optional[List[StrictStr]], Field(description="The concept object names to return in the response. When combined with `uuid`, the results return objects that match either the `objectName` or `uuid`.")] = None,
        uuid: Annotated[Optional[List[StrictStr]], Field(description="The concept UUIDs to return in the response. When combined with `objectName`, the results return objects that match either the `objectName` or `uuid`.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
    ) -> ServicingV2ObjectconfigurationConceptResponseDTO:
        """Retrieve a list of concepts by analytic object

        Retrieve all the concepts for a specific analytic object. The response returns the details of all concepts for the analytic object, including object names, concept types, and descriptions.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param analytic_object_name: The object name of the analytic object from which to retrieve concepts. (required)
        :type analytic_object_name: str
        :param type: The type of the concept to retrieve. Valid values:  - `process`: Retrieves all process concepts. This is the default.
        :type type: List[str]
        :param var_with: The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.
        :type var_with: List[str]
        :param object_name: The concept object names to return in the response. When combined with `uuid`, the results return objects that match either the `objectName` or `uuid`.
        :type object_name: List[str]
        :param uuid: The concept UUIDs to return in the response. When combined with `objectName`, the results return objects that match either the `objectName` or `uuid`.
        :type uuid: List[str]
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._get_analytic_object_concepts_serialize(
            analytic_object_name=analytic_object_name,
            type=type,
            var_with=var_with,
            object_name=object_name,
            uuid=uuid,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationConceptResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_analytic_model.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_analytic_object_concepts_with_http_info(
        self,
        analytic_object_name: Annotated[StrictStr, Field(description="The object name of the analytic object from which to retrieve concepts.")],
        type: Annotated[Optional[List[StrictStr]], Field(description="The type of the concept to retrieve. Valid values:  - `process`: Retrieves all process concepts. This is the default.")] = None,
        var_with: Annotated[Optional[List[StrictStr]], Field(description="The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.")] = None,
        object_name: Annotated[Optional[List[StrictStr]], Field(description="The concept object names to return in the response. When combined with `uuid`, the results return objects that match either the `objectName` or `uuid`.")] = None,
        uuid: Annotated[Optional[List[StrictStr]], Field(description="The concept UUIDs to return in the response. When combined with `objectName`, the results return objects that match either the `objectName` or `uuid`.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
    ) -> ApiResponse[ServicingV2ObjectconfigurationConceptResponseDTO]:
        """Retrieve a list of concepts by analytic object

        Retrieve all the concepts for a specific analytic object. The response returns the details of all concepts for the analytic object, including object names, concept types, and descriptions.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param analytic_object_name: The object name of the analytic object from which to retrieve concepts. (required)
        :type analytic_object_name: str
        :param type: The type of the concept to retrieve. Valid values:  - `process`: Retrieves all process concepts. This is the default.
        :type type: List[str]
        :param var_with: The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.
        :type var_with: List[str]
        :param object_name: The concept object names to return in the response. When combined with `uuid`, the results return objects that match either the `objectName` or `uuid`.
        :type object_name: List[str]
        :param uuid: The concept UUIDs to return in the response. When combined with `objectName`, the results return objects that match either the `objectName` or `uuid`.
        :type uuid: List[str]
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._get_analytic_object_concepts_serialize(
            analytic_object_name=analytic_object_name,
            type=type,
            var_with=var_with,
            object_name=object_name,
            uuid=uuid,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationConceptResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_analytic_model.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_analytic_object_concepts_without_preload_content(
        self,
        analytic_object_name: Annotated[StrictStr, Field(description="The object name of the analytic object from which to retrieve concepts.")],
        type: Annotated[Optional[List[StrictStr]], Field(description="The type of the concept to retrieve. Valid values:  - `process`: Retrieves all process concepts. This is the default.")] = None,
        var_with: Annotated[Optional[List[StrictStr]], Field(description="The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.")] = None,
        object_name: Annotated[Optional[List[StrictStr]], Field(description="The concept object names to return in the response. When combined with `uuid`, the results return objects that match either the `objectName` or `uuid`.")] = None,
        uuid: Annotated[Optional[List[StrictStr]], Field(description="The concept UUIDs to return in the response. When combined with `objectName`, the results return objects that match either the `objectName` or `uuid`.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
        """Retrieve a list of concepts by analytic object

        Retrieve all the concepts for a specific analytic object. The response returns the details of all concepts for the analytic object, including object names, concept types, and descriptions.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param analytic_object_name: The object name of the analytic object from which to retrieve concepts. (required)
        :type analytic_object_name: str
        :param type: The type of the concept to retrieve. Valid values:  - `process`: Retrieves all process concepts. This is the default.
        :type type: List[str]
        :param var_with: The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.
        :type var_with: List[str]
        :param object_name: The concept object names to return in the response. When combined with `uuid`, the results return objects that match either the `objectName` or `uuid`.
        :type object_name: List[str]
        :param uuid: The concept UUIDs to return in the response. When combined with `objectName`, the results return objects that match either the `objectName` or `uuid`.
        :type uuid: List[str]
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._get_analytic_object_concepts_serialize(
            analytic_object_name=analytic_object_name,
            type=type,
            var_with=var_with,
            object_name=object_name,
            uuid=uuid,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationConceptResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_analytic_object_concepts_serialize(
        self,
        analytic_object_name,
        type,
        var_with,
        object_name,
        uuid,
        target_tenant_id,
        project_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'type': 'multi',
            'with': 'multi',
            'objectName': 'multi',
            'uuid': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if analytic_object_name is not None:
            _path_params['analyticObjectName'] = analytic_object_name
        # process the query parameters
        if type is not None:
            
            _query_params.append(('type', type))
            
        if var_with is not None:
            
            _query_params.append(('with', var_with))
            
        if object_name is not None:
            
            _query_params.append(('objectName', object_name))
            
        if uuid is not None:
            
            _query_params.append(('uuid', uuid))
            
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        if project_id is not None:
            _header_params['ProjectID'] = project_id
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
            resource_path='/v2alpha/data/model/analytic-objects/{analyticObjectName}/concepts',
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
    def get_one_concept(
        self,
        concept_id: Annotated[StrictStr, Field(description="The object name or UUID of the concept to retrieve.")],
        var_with: Annotated[Optional[List[StrictStr]], Field(description="The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
    ) -> ServicingV2ObjectconfigurationConceptResponseDTO:
        """Retrieve a concept's details

        Retrieve the details of a specific concept, such as its concept type and description.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param concept_id: The object name or UUID of the concept to retrieve. (required)
        :type concept_id: str
        :param var_with: The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.
        :type var_with: List[str]
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._get_one_concept_serialize(
            concept_id=concept_id,
            var_with=var_with,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationConceptResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_analytic_model.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_one_concept_with_http_info(
        self,
        concept_id: Annotated[StrictStr, Field(description="The object name or UUID of the concept to retrieve.")],
        var_with: Annotated[Optional[List[StrictStr]], Field(description="The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
    ) -> ApiResponse[ServicingV2ObjectconfigurationConceptResponseDTO]:
        """Retrieve a concept's details

        Retrieve the details of a specific concept, such as its concept type and description.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param concept_id: The object name or UUID of the concept to retrieve. (required)
        :type concept_id: str
        :param var_with: The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.
        :type var_with: List[str]
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._get_one_concept_serialize(
            concept_id=concept_id,
            var_with=var_with,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationConceptResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_analytic_model.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_one_concept_without_preload_content(
        self,
        concept_id: Annotated[StrictStr, Field(description="The object name or UUID of the concept to retrieve.")],
        var_with: Annotated[Optional[List[StrictStr]], Field(description="The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
        """Retrieve a concept's details

        Retrieve the details of a specific concept, such as its concept type and description.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param concept_id: The object name or UUID of the concept to retrieve. (required)
        :type concept_id: str
        :param var_with: The level of information to retrieve for the concept. Valid values:  - `basic`: Retrieves the concept's UUID, object name, and basic information. This is the default.  - `details`: Retrieves the `basic` details and additional configurations, such as `visibleInApp`.
        :type var_with: List[str]
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._get_one_concept_serialize(
            concept_id=concept_id,
            var_with=var_with,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationConceptResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_one_concept_serialize(
        self,
        concept_id,
        var_with,
        target_tenant_id,
        project_id,
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
        if concept_id is not None:
            _path_params['conceptId'] = concept_id
        # process the query parameters
        if var_with is not None:
            
            _query_params.append(('with', var_with))
            
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        if project_id is not None:
            _header_params['ProjectID'] = project_id
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
            resource_path='/v2alpha/data/model/concepts/{conceptId}',
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
    def patch_concepts(
        self,
        servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
    ) -> ServicingV2ObjectconfigurationBulkChangeResponseDTO:
        """Partially update concepts

        Make partial changes to existing concepts. The response returns whether each concept was successfully patched or not. When patching objects, we recommend that you first retrieve the object definition using `GET`. You can use the `GET` response in your `PATCH` request definition.   Unlike `PUT`, which completely replaces the concept definition, use `PATCH` to change specific fields in the concept without affecting omitted fields. To replace a concept's entire definition, see the `PUT` method.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param servicing_v2_objectconfiguration_concept_request_dto: (required)
        :type servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._patch_concepts_serialize(
            servicing_v2_objectconfiguration_concept_request_dto=servicing_v2_objectconfiguration_concept_request_dto,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationBulkChangeResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_analytic_model.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def patch_concepts_with_http_info(
        self,
        servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
    ) -> ApiResponse[ServicingV2ObjectconfigurationBulkChangeResponseDTO]:
        """Partially update concepts

        Make partial changes to existing concepts. The response returns whether each concept was successfully patched or not. When patching objects, we recommend that you first retrieve the object definition using `GET`. You can use the `GET` response in your `PATCH` request definition.   Unlike `PUT`, which completely replaces the concept definition, use `PATCH` to change specific fields in the concept without affecting omitted fields. To replace a concept's entire definition, see the `PUT` method.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param servicing_v2_objectconfiguration_concept_request_dto: (required)
        :type servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._patch_concepts_serialize(
            servicing_v2_objectconfiguration_concept_request_dto=servicing_v2_objectconfiguration_concept_request_dto,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationBulkChangeResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_analytic_model.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def patch_concepts_without_preload_content(
        self,
        servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
        """Partially update concepts

        Make partial changes to existing concepts. The response returns whether each concept was successfully patched or not. When patching objects, we recommend that you first retrieve the object definition using `GET`. You can use the `GET` response in your `PATCH` request definition.   Unlike `PUT`, which completely replaces the concept definition, use `PATCH` to change specific fields in the concept without affecting omitted fields. To replace a concept's entire definition, see the `PUT` method.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param servicing_v2_objectconfiguration_concept_request_dto: (required)
        :type servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._patch_concepts_serialize(
            servicing_v2_objectconfiguration_concept_request_dto=servicing_v2_objectconfiguration_concept_request_dto,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationBulkChangeResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _patch_concepts_serialize(
        self,
        servicing_v2_objectconfiguration_concept_request_dto,
        target_tenant_id,
        project_id,
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
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        # process the form parameters
        # process the body parameter
        if servicing_v2_objectconfiguration_concept_request_dto is not None:
            _body_params = servicing_v2_objectconfiguration_concept_request_dto


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
            method='PATCH',
            resource_path='/v2alpha/data/model/concepts',
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
    def put_concepts(
        self,
        servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
    ) -> ServicingV2ObjectconfigurationBulkChangeResponseDTO:
        """Update concepts

        Update existing concepts. The response returns whether each concept was successfully updated or not. When updating objects, we recommend that you first retrieve the object definition using `GET`. You can use the `GET` response in your `PUT` request definition.   In `PUT` calls, the definition in your API call replaces the prior definition. You must provide the entire definition in the `PUT` call. If you omit values from the update request, those values are removed from the concept. To partially update a concept, see the `PATCH` method.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param servicing_v2_objectconfiguration_concept_request_dto: (required)
        :type servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._put_concepts_serialize(
            servicing_v2_objectconfiguration_concept_request_dto=servicing_v2_objectconfiguration_concept_request_dto,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationBulkChangeResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_analytic_model.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def put_concepts_with_http_info(
        self,
        servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
    ) -> ApiResponse[ServicingV2ObjectconfigurationBulkChangeResponseDTO]:
        """Update concepts

        Update existing concepts. The response returns whether each concept was successfully updated or not. When updating objects, we recommend that you first retrieve the object definition using `GET`. You can use the `GET` response in your `PUT` request definition.   In `PUT` calls, the definition in your API call replaces the prior definition. You must provide the entire definition in the `PUT` call. If you omit values from the update request, those values are removed from the concept. To partially update a concept, see the `PATCH` method.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param servicing_v2_objectconfiguration_concept_request_dto: (required)
        :type servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._put_concepts_serialize(
            servicing_v2_objectconfiguration_concept_request_dto=servicing_v2_objectconfiguration_concept_request_dto,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationBulkChangeResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_analytic_model.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def put_concepts_without_preload_content(
        self,
        servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        project_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify a project in which to make the request.")] = None,
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
        """Update concepts

        Update existing concepts. The response returns whether each concept was successfully updated or not. When updating objects, we recommend that you first retrieve the object definition using `GET`. You can use the `GET` response in your `PUT` request definition.   In `PUT` calls, the definition in your API call replaces the prior definition. You must provide the entire definition in the `PUT` call. If you omit values from the update request, those values are removed from the concept. To partially update a concept, see the `PATCH` method.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param servicing_v2_objectconfiguration_concept_request_dto: (required)
        :type servicing_v2_objectconfiguration_concept_request_dto: ServicingV2ObjectconfigurationConceptRequestDTO
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param project_id: Optionally, specify a project in which to make the request.
        :type project_id: str
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

        _param = self._put_concepts_serialize(
            servicing_v2_objectconfiguration_concept_request_dto=servicing_v2_objectconfiguration_concept_request_dto,
            target_tenant_id=target_tenant_id,
            project_id=project_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServicingV2ObjectconfigurationBulkChangeResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _put_concepts_serialize(
        self,
        servicing_v2_objectconfiguration_concept_request_dto,
        target_tenant_id,
        project_id,
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
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        if project_id is not None:
            _header_params['ProjectID'] = project_id
        # process the form parameters
        # process the body parameter
        if servicing_v2_objectconfiguration_concept_request_dto is not None:
            _body_params = servicing_v2_objectconfiguration_concept_request_dto


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
            resource_path='/v2alpha/data/model/concepts',
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


