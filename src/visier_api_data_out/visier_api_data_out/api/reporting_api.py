# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1744
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

from pydantic import Field, StrictBytes, StrictInt, StrictStr
from typing import Optional, Tuple, Union
from typing_extensions import Annotated
from visier_api_data_out.models.report_create_request_dto import ReportCreateRequestDTO
from visier_api_data_out.models.report_dto import ReportDTO
from visier_api_data_out.models.report_delete_success_dto import ReportDeleteSuccessDTO
from visier_api_data_out.models.report_list_response_dto import ReportListResponseDTO
import visier_api_data_out.models


class ReportingApi:
    """
    This class provides methods to make requests to the Visier API.
    It uses the ApiClient to handle the HTTP requests and responses.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def create_report(
        self,
        report_create_request_dto: ReportCreateRequestDTO,
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
    ) -> ReportDTO:
        """Create a report

        Create a new report with a title and description. To edit other contents of the report, such as columns and group bys, navigate to the Reports room in Visier.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_create_request_dto: (required)
        :type report_create_request_dto: ReportCreateRequestDTO
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

        _param = self._create_report_serialize(
            report_create_request_dto=report_create_request_dto,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_data_out.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def create_report_with_http_info(
        self,
        report_create_request_dto: ReportCreateRequestDTO,
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
    ) -> ApiResponse[ReportDTO]:
        """Create a report

        Create a new report with a title and description. To edit other contents of the report, such as columns and group bys, navigate to the Reports room in Visier.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_create_request_dto: (required)
        :type report_create_request_dto: ReportCreateRequestDTO
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

        _param = self._create_report_serialize(
            report_create_request_dto=report_create_request_dto,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_data_out.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def create_report_without_preload_content(
        self,
        report_create_request_dto: ReportCreateRequestDTO,
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
        """Create a report

        Create a new report with a title and description. To edit other contents of the report, such as columns and group bys, navigate to the Reports room in Visier.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_create_request_dto: (required)
        :type report_create_request_dto: ReportCreateRequestDTO
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

        _param = self._create_report_serialize(
            report_create_request_dto=report_create_request_dto,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _create_report_serialize(
        self,
        report_create_request_dto,
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
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter
        if report_create_request_dto is not None:
            _body_params = report_create_request_dto


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
            resource_path='/v1alpha/reporting/reports',
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
    def delete_report(
        self,
        report_id: Annotated[StrictStr, Field(description="The unique identifier of the report you want to delete.")],
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
    ) -> ReportDeleteSuccessDTO:
        """Delete a report

        Delete a report in the tenant. You must know the ID of the report to delete it. To retrieve report IDs, see `GET /v1alpha/reporting/reports`.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_id: The unique identifier of the report you want to delete. (required)
        :type report_id: str
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

        _param = self._delete_report_serialize(
            report_id=report_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportDeleteSuccessDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_data_out.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def delete_report_with_http_info(
        self,
        report_id: Annotated[StrictStr, Field(description="The unique identifier of the report you want to delete.")],
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
    ) -> ApiResponse[ReportDeleteSuccessDTO]:
        """Delete a report

        Delete a report in the tenant. You must know the ID of the report to delete it. To retrieve report IDs, see `GET /v1alpha/reporting/reports`.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_id: The unique identifier of the report you want to delete. (required)
        :type report_id: str
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

        _param = self._delete_report_serialize(
            report_id=report_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportDeleteSuccessDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_data_out.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def delete_report_without_preload_content(
        self,
        report_id: Annotated[StrictStr, Field(description="The unique identifier of the report you want to delete.")],
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
        """Delete a report

        Delete a report in the tenant. You must know the ID of the report to delete it. To retrieve report IDs, see `GET /v1alpha/reporting/reports`.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_id: The unique identifier of the report you want to delete. (required)
        :type report_id: str
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

        _param = self._delete_report_serialize(
            report_id=report_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportDeleteSuccessDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_report_serialize(
        self,
        report_id,
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
        if report_id is not None:
            _path_params['reportId'] = report_id
        # process the query parameters
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
            resource_path='/v1alpha/reporting/reports/{reportId}',
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
    def download_report(
        self,
        report_id: Annotated[StrictStr, Field(description="The unique identifier of the report you want to download.")],
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
        """Download a report

        Download a report as a CSV file. The returned CSV file contains the data in the report. You must know the ID of the report to download it. To retrieve report IDs, see `GET /v1alpha/reporting/reports`.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_id: The unique identifier of the report you want to download. (required)
        :type report_id: str
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

        _param = self._download_report_serialize(
            report_id=report_id,
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
            model_package=visier_api_data_out.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def download_report_with_http_info(
        self,
        report_id: Annotated[StrictStr, Field(description="The unique identifier of the report you want to download.")],
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
        """Download a report

        Download a report as a CSV file. The returned CSV file contains the data in the report. You must know the ID of the report to download it. To retrieve report IDs, see `GET /v1alpha/reporting/reports`.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_id: The unique identifier of the report you want to download. (required)
        :type report_id: str
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

        _param = self._download_report_serialize(
            report_id=report_id,
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
            model_package=visier_api_data_out.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def download_report_without_preload_content(
        self,
        report_id: Annotated[StrictStr, Field(description="The unique identifier of the report you want to download.")],
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
        """Download a report

        Download a report as a CSV file. The returned CSV file contains the data in the report. You must know the ID of the report to download it. To retrieve report IDs, see `GET /v1alpha/reporting/reports`.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_id: The unique identifier of the report you want to download. (required)
        :type report_id: str
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

        _param = self._download_report_serialize(
            report_id=report_id,
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


    def _download_report_serialize(
        self,
        report_id,
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
        if report_id is not None:
            _path_params['reportId'] = report_id
        # process the query parameters
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/zip', 
                    'text/csv', 
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
            resource_path='/v1alpha/reporting/report-data/{reportId}',
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
    def duplicate_report(
        self,
        report_id: Annotated[StrictStr, Field(description="The unique identifier of the report you want to duplicate.")],
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
    ) -> ReportDTO:
        """Duplicate a report

        Make a copy of an existing report. You must know the ID of the report to copy it. To retrieve report IDs, see `GET /v1alpha/reporting/reports`.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_id: The unique identifier of the report you want to duplicate. (required)
        :type report_id: str
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

        _param = self._duplicate_report_serialize(
            report_id=report_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_data_out.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def duplicate_report_with_http_info(
        self,
        report_id: Annotated[StrictStr, Field(description="The unique identifier of the report you want to duplicate.")],
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
    ) -> ApiResponse[ReportDTO]:
        """Duplicate a report

        Make a copy of an existing report. You must know the ID of the report to copy it. To retrieve report IDs, see `GET /v1alpha/reporting/reports`.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_id: The unique identifier of the report you want to duplicate. (required)
        :type report_id: str
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

        _param = self._duplicate_report_serialize(
            report_id=report_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_data_out.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def duplicate_report_without_preload_content(
        self,
        report_id: Annotated[StrictStr, Field(description="The unique identifier of the report you want to duplicate.")],
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
        """Duplicate a report

        Make a copy of an existing report. You must know the ID of the report to copy it. To retrieve report IDs, see `GET /v1alpha/reporting/reports`.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_id: The unique identifier of the report you want to duplicate. (required)
        :type report_id: str
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

        _param = self._duplicate_report_serialize(
            report_id=report_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _duplicate_report_serialize(
        self,
        report_id,
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
        if report_id is not None:
            _path_params['reportId'] = report_id
        # process the query parameters
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
            method='POST',
            resource_path='/v1alpha/reporting/reports/{reportId}',
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
    def get_report(
        self,
        report_id: Annotated[StrictStr, Field(description="The unique identifier of the report you want to retrieve.")],
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
    ) -> ReportDTO:
        """Retrieve a report's details

        Retrieve the details of a specific report. The response returns information such as title, description, owner, and the allowed actions you can take on the report. You must know the ID of the report to retrieve its details. To retrieve report IDs, see `GET /v1alpha/reporting/reports`.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_id: The unique identifier of the report you want to retrieve. (required)
        :type report_id: str
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

        _param = self._get_report_serialize(
            report_id=report_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_data_out.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_report_with_http_info(
        self,
        report_id: Annotated[StrictStr, Field(description="The unique identifier of the report you want to retrieve.")],
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
    ) -> ApiResponse[ReportDTO]:
        """Retrieve a report's details

        Retrieve the details of a specific report. The response returns information such as title, description, owner, and the allowed actions you can take on the report. You must know the ID of the report to retrieve its details. To retrieve report IDs, see `GET /v1alpha/reporting/reports`.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_id: The unique identifier of the report you want to retrieve. (required)
        :type report_id: str
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

        _param = self._get_report_serialize(
            report_id=report_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_data_out.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_report_without_preload_content(
        self,
        report_id: Annotated[StrictStr, Field(description="The unique identifier of the report you want to retrieve.")],
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
        """Retrieve a report's details

        Retrieve the details of a specific report. The response returns information such as title, description, owner, and the allowed actions you can take on the report. You must know the ID of the report to retrieve its details. To retrieve report IDs, see `GET /v1alpha/reporting/reports`.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param report_id: The unique identifier of the report you want to retrieve. (required)
        :type report_id: str
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

        _param = self._get_report_serialize(
            report_id=report_id,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_report_serialize(
        self,
        report_id,
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
        if report_id is not None:
            _path_params['reportId'] = report_id
        # process the query parameters
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
            method='GET',
            resource_path='/v1alpha/reporting/reports/{reportId}',
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
    def get_reports(
        self,
        limit: Annotated[Optional[StrictInt], Field(description="Optionally, specify the number of reports to return. If omitted, the request uses the default value of 100.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="Optionally, specify the zero-based index of the report to start fetching from. If omitted, the request uses the default value of 0.")] = None,
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
    ) -> ReportListResponseDTO:
        """Retrieve a list of reports

        Retrieve a list of reports. The response returns information such as the unique ID, title, description, owner, and the allowed actions you can take on the report.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param limit: Optionally, specify the number of reports to return. If omitted, the request uses the default value of 100.
        :type limit: int
        :param start: Optionally, specify the zero-based index of the report to start fetching from. If omitted, the request uses the default value of 0.
        :type start: int
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

        _param = self._get_reports_serialize(
            limit=limit,
            start=start,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportListResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_data_out.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def get_reports_with_http_info(
        self,
        limit: Annotated[Optional[StrictInt], Field(description="Optionally, specify the number of reports to return. If omitted, the request uses the default value of 100.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="Optionally, specify the zero-based index of the report to start fetching from. If omitted, the request uses the default value of 0.")] = None,
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
    ) -> ApiResponse[ReportListResponseDTO]:
        """Retrieve a list of reports

        Retrieve a list of reports. The response returns information such as the unique ID, title, description, owner, and the allowed actions you can take on the report.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param limit: Optionally, specify the number of reports to return. If omitted, the request uses the default value of 100.
        :type limit: int
        :param start: Optionally, specify the zero-based index of the report to start fetching from. If omitted, the request uses the default value of 0.
        :type start: int
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

        _param = self._get_reports_serialize(
            limit=limit,
            start=start,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportListResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_data_out.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def get_reports_without_preload_content(
        self,
        limit: Annotated[Optional[StrictInt], Field(description="Optionally, specify the number of reports to return. If omitted, the request uses the default value of 100.")] = None,
        start: Annotated[Optional[StrictInt], Field(description="Optionally, specify the zero-based index of the report to start fetching from. If omitted, the request uses the default value of 0.")] = None,
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
        """Retrieve a list of reports

        Retrieve a list of reports. The response returns information such as the unique ID, title, description, owner, and the allowed actions you can take on the report.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param limit: Optionally, specify the number of reports to return. If omitted, the request uses the default value of 100.
        :type limit: int
        :param start: Optionally, specify the zero-based index of the report to start fetching from. If omitted, the request uses the default value of 0.
        :type start: int
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

        _param = self._get_reports_serialize(
            limit=limit,
            start=start,
            target_tenant_id=target_tenant_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ReportListResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_reports_serialize(
        self,
        limit,
        start,
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
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if start is not None:
            
            _query_params.append(('start', start))
            
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
            method='GET',
            resource_path='/v1alpha/reporting/reports',
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


