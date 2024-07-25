# coding: utf-8

"""
    Visier Public Direct Data Intake APIs

    Visier APIs for uploading already transformed data files directly to target objects in Visier.

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBytes, StrictStr
from typing import Optional, Union
from typing_extensions import Annotated
from visier.sdk.api.direct_data_intake.models.direct_data_upload_file_response_dto import DirectDataUploadFileResponseDTO

from visier.sdk.api.direct_data_intake.api_client import ApiClient, RequestSerialized
from visier.sdk.api.direct_data_intake.api_response import ApiResponse
from visier.sdk.api.direct_data_intake.rest import RESTResponseType


class DataIntakeApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def upload_file(
        self,
        draft_id: Annotated[StrictStr, Field(description="The unique identifier of the project to load data into. Currently, the only supported value is `prod` to update the production version.")],
        transaction_id: Annotated[StrictStr, Field(description="The unique identifier of the transaction to load data files into.")],
        object_name: Annotated[StrictStr, Field(description="The name of the object to upload the data to.  If uploading data to a multi-value property (MVP), specify the property in `{object}--{property}` format; for example, `Employee--Employee_Budgeted_Compensation`.")],
        body: Optional[Union[StrictBytes, StrictStr]] = None,
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
    ) -> DirectDataUploadFileResponseDTO:
        """Upload files

        Send upload files to a previously-created transaction. Each upload file is associated with a target object in Visier. The files are not processed in Visier until you commit the transaction.

        :param draft_id: The unique identifier of the project to load data into. Currently, the only supported value is `prod` to update the production version. (required)
        :type draft_id: str
        :param transaction_id: The unique identifier of the transaction to load data files into. (required)
        :type transaction_id: str
        :param object_name: The name of the object to upload the data to.  If uploading data to a multi-value property (MVP), specify the property in `{object}--{property}` format; for example, `Employee--Employee_Budgeted_Compensation`. (required)
        :type object_name: str
        :param body:
        :type body: bytearray
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

        _param = self._upload_file_serialize(
            draft_id=draft_id,
            transaction_id=transaction_id,
            object_name=object_name,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DirectDataUploadFileResponseDTO",
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
    def upload_file_with_http_info(
        self,
        draft_id: Annotated[StrictStr, Field(description="The unique identifier of the project to load data into. Currently, the only supported value is `prod` to update the production version.")],
        transaction_id: Annotated[StrictStr, Field(description="The unique identifier of the transaction to load data files into.")],
        object_name: Annotated[StrictStr, Field(description="The name of the object to upload the data to.  If uploading data to a multi-value property (MVP), specify the property in `{object}--{property}` format; for example, `Employee--Employee_Budgeted_Compensation`.")],
        body: Optional[Union[StrictBytes, StrictStr]] = None,
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
    ) -> ApiResponse[DirectDataUploadFileResponseDTO]:
        """Upload files

        Send upload files to a previously-created transaction. Each upload file is associated with a target object in Visier. The files are not processed in Visier until you commit the transaction.

        :param draft_id: The unique identifier of the project to load data into. Currently, the only supported value is `prod` to update the production version. (required)
        :type draft_id: str
        :param transaction_id: The unique identifier of the transaction to load data files into. (required)
        :type transaction_id: str
        :param object_name: The name of the object to upload the data to.  If uploading data to a multi-value property (MVP), specify the property in `{object}--{property}` format; for example, `Employee--Employee_Budgeted_Compensation`. (required)
        :type object_name: str
        :param body:
        :type body: bytearray
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

        _param = self._upload_file_serialize(
            draft_id=draft_id,
            transaction_id=transaction_id,
            object_name=object_name,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DirectDataUploadFileResponseDTO",
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
    def upload_file_without_preload_content(
        self,
        draft_id: Annotated[StrictStr, Field(description="The unique identifier of the project to load data into. Currently, the only supported value is `prod` to update the production version.")],
        transaction_id: Annotated[StrictStr, Field(description="The unique identifier of the transaction to load data files into.")],
        object_name: Annotated[StrictStr, Field(description="The name of the object to upload the data to.  If uploading data to a multi-value property (MVP), specify the property in `{object}--{property}` format; for example, `Employee--Employee_Budgeted_Compensation`.")],
        body: Optional[Union[StrictBytes, StrictStr]] = None,
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
        """Upload files

        Send upload files to a previously-created transaction. Each upload file is associated with a target object in Visier. The files are not processed in Visier until you commit the transaction.

        :param draft_id: The unique identifier of the project to load data into. Currently, the only supported value is `prod` to update the production version. (required)
        :type draft_id: str
        :param transaction_id: The unique identifier of the transaction to load data files into. (required)
        :type transaction_id: str
        :param object_name: The name of the object to upload the data to.  If uploading data to a multi-value property (MVP), specify the property in `{object}--{property}` format; for example, `Employee--Employee_Budgeted_Compensation`. (required)
        :type object_name: str
        :param body:
        :type body: bytearray
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

        _param = self._upload_file_serialize(
            draft_id=draft_id,
            transaction_id=transaction_id,
            object_name=object_name,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DirectDataUploadFileResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _upload_file_serialize(
        self,
        draft_id,
        transaction_id,
        object_name,
        body,
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
        if draft_id is not None:
            _path_params['draftId'] = draft_id
        if transaction_id is not None:
            _path_params['transactionId'] = transaction_id
        if object_name is not None:
            _path_params['objectName'] = object_name
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if body is not None:
            # convert to byte array if the input is a file name (str)
            if isinstance(body, str):
                with open(body, "rb") as _fp:
                    _body_params = _fp.read()
            else:
                _body_params = body


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
                        'application/octetstream'
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
            resource_path='/v1/data/directloads/{draftId}/transactions/{transactionId}/{objectName}',
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


