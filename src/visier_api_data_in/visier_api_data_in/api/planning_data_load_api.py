# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1598
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

from pydantic import Field, StrictBytes, StrictStr
from typing import Optional, Tuple, Union
from typing_extensions import Annotated
from visier_api_data_in.models.plan_data_upload_response_dto import PlanDataUploadResponseDTO
from visier_api_data_in.models.plan_row_data_load_response_dto import PlanRowDataLoadResponseDTO
import visier_api_data_in.models


class PlanningDataLoadApi:
    """
    This class provides methods to make requests to the Visier API.
    It uses the ApiClient to handle the HTTP requests and responses.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def plan_data_load_plan_data_upload(
        self,
        plan_id: Annotated[StrictStr, Field(description="The unique identifier of the plan.")],
        sceanrio_id: Annotated[StrictStr, Field(description="The unique identifier of the plan scenario to load data into.")],
        calculation: Annotated[Optional[StrictStr], Field(description="Sets the plan values to rollup, distribute, or neither. Valid values:   - **ROLLUP**: Roll up children data values to parent data values. If the data provides a parent value and its child value, this method prioritizes the loaded value for the child and and overwrites the parent.   - **DISTRIBUTE**: Distribute parent data values to their children. If the value of the child conflicts with the calculated distribution, this method overrides the loaded child value.   - **NONE**: The loaded values are neither rolled up or distributed. This is the default.")] = None,
        currency: Annotated[Optional[StrictStr], Field(description="The 3-digit ISO 4217 currency code of the data. If undefined, default is the plan's consolidation currency. If the currency is different from the plan's consolidation currency, the values are converted to the consolidation currency using the conversion rates loaded for the plan's baseline period.")] = None,
        method: Annotated[Optional[StrictStr], Field(description="Sets how to validate the data being loaded into Visier. Valid values:   - **VALIDATE**: Runs a test load through all the validation steps without putting the data into the plan. Use `VALIDATE` to find any errors before using `STRICT_UPLOAD` to load the data.   - **SKIP_ERRORS**: Loads all data without errors into the plan. Any rows with errors are excluded from the plan.   - **STRICT_UPLOAD**: Loads data into the plan if there are no errors in any row. If there are errors, the load fails. This is the default.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="The CSV file to load into the plan.")] = None,
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
    ) -> PlanDataUploadResponseDTO:
        """Upload plan data

        Send a file to Visier to modify a plan's data. The file must be in CSV format and match the plan's schema. To get the plan's schema, call `GET /v1alpha/planning/model/plans/{id}?withSchema=true`. The data file must contain the following columns: - `periodId`: From the GET response, use the `date` values in the `timePeriods` array as values in this column. - A column for each `id` value in the `planSegmentLevels` object, where the row value is the `segmentId`. - A column for each  `id` value in the `planItems` object that you want to modify data for, where the row value is the data value. <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued. If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param plan_id: The unique identifier of the plan. (required)
        :type plan_id: str
        :param sceanrio_id: The unique identifier of the plan scenario to load data into. (required)
        :type sceanrio_id: str
        :param calculation: Sets the plan values to rollup, distribute, or neither. Valid values:   - **ROLLUP**: Roll up children data values to parent data values. If the data provides a parent value and its child value, this method prioritizes the loaded value for the child and and overwrites the parent.   - **DISTRIBUTE**: Distribute parent data values to their children. If the value of the child conflicts with the calculated distribution, this method overrides the loaded child value.   - **NONE**: The loaded values are neither rolled up or distributed. This is the default.
        :type calculation: str
        :param currency: The 3-digit ISO 4217 currency code of the data. If undefined, default is the plan's consolidation currency. If the currency is different from the plan's consolidation currency, the values are converted to the consolidation currency using the conversion rates loaded for the plan's baseline period.
        :type currency: str
        :param method: Sets how to validate the data being loaded into Visier. Valid values:   - **VALIDATE**: Runs a test load through all the validation steps without putting the data into the plan. Use `VALIDATE` to find any errors before using `STRICT_UPLOAD` to load the data.   - **SKIP_ERRORS**: Loads all data without errors into the plan. Any rows with errors are excluded from the plan.   - **STRICT_UPLOAD**: Loads data into the plan if there are no errors in any row. If there are errors, the load fails. This is the default.
        :type method: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param file: The CSV file to load into the plan.
        :type file: bytearray
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

        _param = self._plan_data_load_plan_data_upload_serialize(
            plan_id=plan_id,
            sceanrio_id=sceanrio_id,
            calculation=calculation,
            currency=currency,
            method=method,
            target_tenant_id=target_tenant_id,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PlanDataUploadResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_data_in.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def plan_data_load_plan_data_upload_with_http_info(
        self,
        plan_id: Annotated[StrictStr, Field(description="The unique identifier of the plan.")],
        sceanrio_id: Annotated[StrictStr, Field(description="The unique identifier of the plan scenario to load data into.")],
        calculation: Annotated[Optional[StrictStr], Field(description="Sets the plan values to rollup, distribute, or neither. Valid values:   - **ROLLUP**: Roll up children data values to parent data values. If the data provides a parent value and its child value, this method prioritizes the loaded value for the child and and overwrites the parent.   - **DISTRIBUTE**: Distribute parent data values to their children. If the value of the child conflicts with the calculated distribution, this method overrides the loaded child value.   - **NONE**: The loaded values are neither rolled up or distributed. This is the default.")] = None,
        currency: Annotated[Optional[StrictStr], Field(description="The 3-digit ISO 4217 currency code of the data. If undefined, default is the plan's consolidation currency. If the currency is different from the plan's consolidation currency, the values are converted to the consolidation currency using the conversion rates loaded for the plan's baseline period.")] = None,
        method: Annotated[Optional[StrictStr], Field(description="Sets how to validate the data being loaded into Visier. Valid values:   - **VALIDATE**: Runs a test load through all the validation steps without putting the data into the plan. Use `VALIDATE` to find any errors before using `STRICT_UPLOAD` to load the data.   - **SKIP_ERRORS**: Loads all data without errors into the plan. Any rows with errors are excluded from the plan.   - **STRICT_UPLOAD**: Loads data into the plan if there are no errors in any row. If there are errors, the load fails. This is the default.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="The CSV file to load into the plan.")] = None,
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
    ) -> ApiResponse[PlanDataUploadResponseDTO]:
        """Upload plan data

        Send a file to Visier to modify a plan's data. The file must be in CSV format and match the plan's schema. To get the plan's schema, call `GET /v1alpha/planning/model/plans/{id}?withSchema=true`. The data file must contain the following columns: - `periodId`: From the GET response, use the `date` values in the `timePeriods` array as values in this column. - A column for each `id` value in the `planSegmentLevels` object, where the row value is the `segmentId`. - A column for each  `id` value in the `planItems` object that you want to modify data for, where the row value is the data value. <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued. If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param plan_id: The unique identifier of the plan. (required)
        :type plan_id: str
        :param sceanrio_id: The unique identifier of the plan scenario to load data into. (required)
        :type sceanrio_id: str
        :param calculation: Sets the plan values to rollup, distribute, or neither. Valid values:   - **ROLLUP**: Roll up children data values to parent data values. If the data provides a parent value and its child value, this method prioritizes the loaded value for the child and and overwrites the parent.   - **DISTRIBUTE**: Distribute parent data values to their children. If the value of the child conflicts with the calculated distribution, this method overrides the loaded child value.   - **NONE**: The loaded values are neither rolled up or distributed. This is the default.
        :type calculation: str
        :param currency: The 3-digit ISO 4217 currency code of the data. If undefined, default is the plan's consolidation currency. If the currency is different from the plan's consolidation currency, the values are converted to the consolidation currency using the conversion rates loaded for the plan's baseline period.
        :type currency: str
        :param method: Sets how to validate the data being loaded into Visier. Valid values:   - **VALIDATE**: Runs a test load through all the validation steps without putting the data into the plan. Use `VALIDATE` to find any errors before using `STRICT_UPLOAD` to load the data.   - **SKIP_ERRORS**: Loads all data without errors into the plan. Any rows with errors are excluded from the plan.   - **STRICT_UPLOAD**: Loads data into the plan if there are no errors in any row. If there are errors, the load fails. This is the default.
        :type method: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param file: The CSV file to load into the plan.
        :type file: bytearray
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

        _param = self._plan_data_load_plan_data_upload_serialize(
            plan_id=plan_id,
            sceanrio_id=sceanrio_id,
            calculation=calculation,
            currency=currency,
            method=method,
            target_tenant_id=target_tenant_id,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PlanDataUploadResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_data_in.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def plan_data_load_plan_data_upload_without_preload_content(
        self,
        plan_id: Annotated[StrictStr, Field(description="The unique identifier of the plan.")],
        sceanrio_id: Annotated[StrictStr, Field(description="The unique identifier of the plan scenario to load data into.")],
        calculation: Annotated[Optional[StrictStr], Field(description="Sets the plan values to rollup, distribute, or neither. Valid values:   - **ROLLUP**: Roll up children data values to parent data values. If the data provides a parent value and its child value, this method prioritizes the loaded value for the child and and overwrites the parent.   - **DISTRIBUTE**: Distribute parent data values to their children. If the value of the child conflicts with the calculated distribution, this method overrides the loaded child value.   - **NONE**: The loaded values are neither rolled up or distributed. This is the default.")] = None,
        currency: Annotated[Optional[StrictStr], Field(description="The 3-digit ISO 4217 currency code of the data. If undefined, default is the plan's consolidation currency. If the currency is different from the plan's consolidation currency, the values are converted to the consolidation currency using the conversion rates loaded for the plan's baseline period.")] = None,
        method: Annotated[Optional[StrictStr], Field(description="Sets how to validate the data being loaded into Visier. Valid values:   - **VALIDATE**: Runs a test load through all the validation steps without putting the data into the plan. Use `VALIDATE` to find any errors before using `STRICT_UPLOAD` to load the data.   - **SKIP_ERRORS**: Loads all data without errors into the plan. Any rows with errors are excluded from the plan.   - **STRICT_UPLOAD**: Loads data into the plan if there are no errors in any row. If there are errors, the load fails. This is the default.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="The CSV file to load into the plan.")] = None,
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
        """Upload plan data

        Send a file to Visier to modify a plan's data. The file must be in CSV format and match the plan's schema. To get the plan's schema, call `GET /v1alpha/planning/model/plans/{id}?withSchema=true`. The data file must contain the following columns: - `periodId`: From the GET response, use the `date` values in the `timePeriods` array as values in this column. - A column for each `id` value in the `planSegmentLevels` object, where the row value is the `segmentId`. - A column for each  `id` value in the `planItems` object that you want to modify data for, where the row value is the data value. <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued. If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param plan_id: The unique identifier of the plan. (required)
        :type plan_id: str
        :param sceanrio_id: The unique identifier of the plan scenario to load data into. (required)
        :type sceanrio_id: str
        :param calculation: Sets the plan values to rollup, distribute, or neither. Valid values:   - **ROLLUP**: Roll up children data values to parent data values. If the data provides a parent value and its child value, this method prioritizes the loaded value for the child and and overwrites the parent.   - **DISTRIBUTE**: Distribute parent data values to their children. If the value of the child conflicts with the calculated distribution, this method overrides the loaded child value.   - **NONE**: The loaded values are neither rolled up or distributed. This is the default.
        :type calculation: str
        :param currency: The 3-digit ISO 4217 currency code of the data. If undefined, default is the plan's consolidation currency. If the currency is different from the plan's consolidation currency, the values are converted to the consolidation currency using the conversion rates loaded for the plan's baseline period.
        :type currency: str
        :param method: Sets how to validate the data being loaded into Visier. Valid values:   - **VALIDATE**: Runs a test load through all the validation steps without putting the data into the plan. Use `VALIDATE` to find any errors before using `STRICT_UPLOAD` to load the data.   - **SKIP_ERRORS**: Loads all data without errors into the plan. Any rows with errors are excluded from the plan.   - **STRICT_UPLOAD**: Loads data into the plan if there are no errors in any row. If there are errors, the load fails. This is the default.
        :type method: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param file: The CSV file to load into the plan.
        :type file: bytearray
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

        _param = self._plan_data_load_plan_data_upload_serialize(
            plan_id=plan_id,
            sceanrio_id=sceanrio_id,
            calculation=calculation,
            currency=currency,
            method=method,
            target_tenant_id=target_tenant_id,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PlanDataUploadResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _plan_data_load_plan_data_upload_serialize(
        self,
        plan_id,
        sceanrio_id,
        calculation,
        currency,
        method,
        target_tenant_id,
        file,
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
        if plan_id is not None:
            _path_params['planId'] = plan_id
        if sceanrio_id is not None:
            _path_params['sceanrioId'] = sceanrio_id
        if calculation is not None:
            _path_params['calculation'] = calculation
        if currency is not None:
            _path_params['currency'] = currency
        if method is not None:
            _path_params['method'] = method
        # process the query parameters
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        if file is not None:
            _files['file'] = file
        # process the body parameter


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
                        'multipart/form-data'
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
            resource_path='/v1alpha/planning/data/plans/{planId}/scenarios/{scenarioId}',
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
    def plan_data_load_plan_row_data_load(
        self,
        plan_id: Annotated[StrictStr, Field(description="The unique identifier of the plan.")],
        method: Annotated[Optional[StrictStr], Field(description="Sets how to validate the data being loaded into Visier. Valid values:   - **VALIDATE**: Runs a test load through all the validation steps without putting the data into the plan. Use `VALIDATE` to find any errors before using `STRICT_UPLOAD` to load the data.   - **SKIP_ERRORS**: Loads all data without errors into the plan. Any rows with errors are excluded from the plan.   - **STRICT_UPLOAD**: Loads data into the plan if there are no errors in any row. If there are errors, the load fails. This is the default.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="The CSV file to load into the plan.")] = None,
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
    ) -> PlanRowDataLoadResponseDTO:
        """Add or remove plan rows

        Send a file to Visier to modify a plan's rows. The file must be in CSV format and contain the following columns: - Add/Remove: In the column, use the value \"Add\" to add the specified row to the plan or \"Remove\" to remove the specified row from the plan. - A column for each dimension path or `planSegmentLevels` ID.    - If adding rows, use one column per part of the path. For example, to add a new organization under Product, use 3 columns: Organization_Hierarchy.Level_1, Organization_Hierarchy.Level_2, Organization_Hierarchy.Level_3 with 3 segment member values: [Organization_Hierarchy].[Bluesphere], [Organization_Hierarchy].[Product], New Organization.      - If the segment member does not exist, write its display name.     - If the segment member exists, use its `planSegmentLevelMembers` ID. For example, if your plan is segmented by Organization Hierarchy and Location and you want to add a location under your new organization, you would use the columns  Organization_Hierarchy.Level_1, Organization_Hierarchy.Level_2, Organization_Hierarchy.Level_3, Location.Location_1 with the following values: [Organization_Hierarchy].[Bluesphere], [Organization_Hierarchy].[Product], New Organization, [Location].[North America].[United States].   - If removing rows, use one column per plan segment level `segmentId`, where the values are the plan segment levels `id`. To get the IDs, call `GET /v1alpha/planning/model/plans/{id}?withSchema=true`. <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued. If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param plan_id: The unique identifier of the plan. (required)
        :type plan_id: str
        :param method: Sets how to validate the data being loaded into Visier. Valid values:   - **VALIDATE**: Runs a test load through all the validation steps without putting the data into the plan. Use `VALIDATE` to find any errors before using `STRICT_UPLOAD` to load the data.   - **SKIP_ERRORS**: Loads all data without errors into the plan. Any rows with errors are excluded from the plan.   - **STRICT_UPLOAD**: Loads data into the plan if there are no errors in any row. If there are errors, the load fails. This is the default.
        :type method: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param file: The CSV file to load into the plan.
        :type file: bytearray
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

        _param = self._plan_data_load_plan_row_data_load_serialize(
            plan_id=plan_id,
            method=method,
            target_tenant_id=target_tenant_id,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PlanRowDataLoadResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_data_in.models,
            response_data=response_data,
            response_types_map=_response_types_map
        ).data


    @validate_call
    def plan_data_load_plan_row_data_load_with_http_info(
        self,
        plan_id: Annotated[StrictStr, Field(description="The unique identifier of the plan.")],
        method: Annotated[Optional[StrictStr], Field(description="Sets how to validate the data being loaded into Visier. Valid values:   - **VALIDATE**: Runs a test load through all the validation steps without putting the data into the plan. Use `VALIDATE` to find any errors before using `STRICT_UPLOAD` to load the data.   - **SKIP_ERRORS**: Loads all data without errors into the plan. Any rows with errors are excluded from the plan.   - **STRICT_UPLOAD**: Loads data into the plan if there are no errors in any row. If there are errors, the load fails. This is the default.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="The CSV file to load into the plan.")] = None,
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
    ) -> ApiResponse[PlanRowDataLoadResponseDTO]:
        """Add or remove plan rows

        Send a file to Visier to modify a plan's rows. The file must be in CSV format and contain the following columns: - Add/Remove: In the column, use the value \"Add\" to add the specified row to the plan or \"Remove\" to remove the specified row from the plan. - A column for each dimension path or `planSegmentLevels` ID.    - If adding rows, use one column per part of the path. For example, to add a new organization under Product, use 3 columns: Organization_Hierarchy.Level_1, Organization_Hierarchy.Level_2, Organization_Hierarchy.Level_3 with 3 segment member values: [Organization_Hierarchy].[Bluesphere], [Organization_Hierarchy].[Product], New Organization.      - If the segment member does not exist, write its display name.     - If the segment member exists, use its `planSegmentLevelMembers` ID. For example, if your plan is segmented by Organization Hierarchy and Location and you want to add a location under your new organization, you would use the columns  Organization_Hierarchy.Level_1, Organization_Hierarchy.Level_2, Organization_Hierarchy.Level_3, Location.Location_1 with the following values: [Organization_Hierarchy].[Bluesphere], [Organization_Hierarchy].[Product], New Organization, [Location].[North America].[United States].   - If removing rows, use one column per plan segment level `segmentId`, where the values are the plan segment levels `id`. To get the IDs, call `GET /v1alpha/planning/model/plans/{id}?withSchema=true`. <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued. If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param plan_id: The unique identifier of the plan. (required)
        :type plan_id: str
        :param method: Sets how to validate the data being loaded into Visier. Valid values:   - **VALIDATE**: Runs a test load through all the validation steps without putting the data into the plan. Use `VALIDATE` to find any errors before using `STRICT_UPLOAD` to load the data.   - **SKIP_ERRORS**: Loads all data without errors into the plan. Any rows with errors are excluded from the plan.   - **STRICT_UPLOAD**: Loads data into the plan if there are no errors in any row. If there are errors, the load fails. This is the default.
        :type method: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param file: The CSV file to load into the plan.
        :type file: bytearray
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

        _param = self._plan_data_load_plan_row_data_load_serialize(
            plan_id=plan_id,
            method=method,
            target_tenant_id=target_tenant_id,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PlanRowDataLoadResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            model_package=visier_api_data_in.models,
            response_data=response_data,
            response_types_map=_response_types_map
        )


    @validate_call
    def plan_data_load_plan_row_data_load_without_preload_content(
        self,
        plan_id: Annotated[StrictStr, Field(description="The unique identifier of the plan.")],
        method: Annotated[Optional[StrictStr], Field(description="Sets how to validate the data being loaded into Visier. Valid values:   - **VALIDATE**: Runs a test load through all the validation steps without putting the data into the plan. Use `VALIDATE` to find any errors before using `STRICT_UPLOAD` to load the data.   - **SKIP_ERRORS**: Loads all data without errors into the plan. Any rows with errors are excluded from the plan.   - **STRICT_UPLOAD**: Loads data into the plan if there are no errors in any row. If there are errors, the load fails. This is the default.")] = None,
        target_tenant_id: Annotated[Optional[StrictStr], Field(description="Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="The CSV file to load into the plan.")] = None,
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
        """Add or remove plan rows

        Send a file to Visier to modify a plan's rows. The file must be in CSV format and contain the following columns: - Add/Remove: In the column, use the value \"Add\" to add the specified row to the plan or \"Remove\" to remove the specified row from the plan. - A column for each dimension path or `planSegmentLevels` ID.    - If adding rows, use one column per part of the path. For example, to add a new organization under Product, use 3 columns: Organization_Hierarchy.Level_1, Organization_Hierarchy.Level_2, Organization_Hierarchy.Level_3 with 3 segment member values: [Organization_Hierarchy].[Bluesphere], [Organization_Hierarchy].[Product], New Organization.      - If the segment member does not exist, write its display name.     - If the segment member exists, use its `planSegmentLevelMembers` ID. For example, if your plan is segmented by Organization Hierarchy and Location and you want to add a location under your new organization, you would use the columns  Organization_Hierarchy.Level_1, Organization_Hierarchy.Level_2, Organization_Hierarchy.Level_3, Location.Location_1 with the following values: [Organization_Hierarchy].[Bluesphere], [Organization_Hierarchy].[Product], New Organization, [Location].[North America].[United States].   - If removing rows, use one column per plan segment level `segmentId`, where the values are the plan segment levels `id`. To get the IDs, call `GET /v1alpha/planning/model/plans/{id}?withSchema=true`. <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued. If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

        :param plan_id: The unique identifier of the plan. (required)
        :type plan_id: str
        :param method: Sets how to validate the data being loaded into Visier. Valid values:   - **VALIDATE**: Runs a test load through all the validation steps without putting the data into the plan. Use `VALIDATE` to find any errors before using `STRICT_UPLOAD` to load the data.   - **SKIP_ERRORS**: Loads all data without errors into the plan. Any rows with errors are excluded from the plan.   - **STRICT_UPLOAD**: Loads data into the plan if there are no errors in any row. If there are errors, the load fails. This is the default.
        :type method: str
        :param target_tenant_id: Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant.
        :type target_tenant_id: str
        :param file: The CSV file to load into the plan.
        :type file: bytearray
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

        _param = self._plan_data_load_plan_row_data_load_serialize(
            plan_id=plan_id,
            method=method,
            target_tenant_id=target_tenant_id,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PlanRowDataLoadResponseDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _plan_data_load_plan_row_data_load_serialize(
        self,
        plan_id,
        method,
        target_tenant_id,
        file,
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
        if plan_id is not None:
            _path_params['planId'] = plan_id
        if method is not None:
            _path_params['method'] = method
        # process the query parameters
        # process the header parameters
        if target_tenant_id is not None:
            _header_params['TargetTenantID'] = target_tenant_id
        # process the form parameters
        if file is not None:
            _files['file'] = file
        # process the body parameter


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
                        'multipart/form-data'
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
            resource_path='/v1alpha/planning/data/plans/{planId}/rows',
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


