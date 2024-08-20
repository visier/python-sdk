# visier.sdk.api.administration.ProductionVersionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_production_versions**](ProductionVersionsApi.md#get_production_versions) | **GET** /v1alpha/admin/production-versions | Retrieve a list of all production versions
[**post_production_version**](ProductionVersionsApi.md#post_production_version) | **POST** /v1alpha/admin/production-versions/{productionVersionId} | Perform an operation on a production version
[**post_production_versions**](ProductionVersionsApi.md#post_production_versions) | **POST** /v1alpha/admin/production-versions | Perform an operation on production versions


# **get_production_versions**
> GetProductionVersionsAPIResponseDTO get_production_versions(limit=limit, start=start)

Retrieve a list of all production versions

Retrieve a list of all projects that were published to production, ordered from latest published to earliest published.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.get_production_versions_api_response_dto import GetProductionVersionsAPIResponseDTO
from visier.sdk.api.administration.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.sdk.api.administration.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.sdk.api.administration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.sdk.api.administration.ProductionVersionsApi(api_client)
    limit = 56 # int | The maximum number of production versions to return. Default is 400. (optional)
    start = 56 # int | The starting index of the first production version to return. Default is 0. (optional)

    try:
        # Retrieve a list of all production versions
        api_response = api_instance.get_production_versions(limit=limit, start=start)
        print("The response of ProductionVersionsApi->get_production_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionVersionsApi->get_production_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of production versions to return. Default is 400. | [optional] 
 **start** | **int**| The starting index of the first production version to return. Default is 0. | [optional] 

### Return type

[**GetProductionVersionsAPIResponseDTO**](GetProductionVersionsAPIResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_production_version**
> ProductionVersionAPIOperationResponseDTO post_production_version(production_version_id, operation=operation)

Perform an operation on a production version

Perform operations on a specific production version. The following operations are supported:  * `rollBackTo`: Create a project that rolls back the production version to the specified version. The project contains uncommitted changes that reverse the published versions after the target production version.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.production_version_api_operation_response_dto import ProductionVersionAPIOperationResponseDTO
from visier.sdk.api.administration.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.sdk.api.administration.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.sdk.api.administration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.sdk.api.administration.ProductionVersionsApi(api_client)
    production_version_id = 'production_version_id_example' # str | 
    operation = 'operation_example' # str | The operation to perform. Valid values:  * `rollBackTo`: Create a project that rolls back the production version to the specified version. The project contains uncommitted changes that reverse the published versions after the target production version. (optional)

    try:
        # Perform an operation on a production version
        api_response = api_instance.post_production_version(production_version_id, operation=operation)
        print("The response of ProductionVersionsApi->post_production_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionVersionsApi->post_production_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_version_id** | **str**|  | 
 **operation** | **str**| The operation to perform. Valid values:  * &#x60;rollBackTo&#x60;: Create a project that rolls back the production version to the specified version. The project contains uncommitted changes that reverse the published versions after the target production version. | [optional] 

### Return type

[**ProductionVersionAPIOperationResponseDTO**](ProductionVersionAPIOperationResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_production_versions**
> ProductionVersionsAPIOperationResponseDTO post_production_versions(production_versions_api_operation_request_dto)

Perform an operation on production versions

Perform operations on production versions, such as exporting a production project's committed changes. If exporting, please specify `Accept: application/zip, application/json` in the header.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.production_versions_api_operation_request_dto import ProductionVersionsAPIOperationRequestDTO
from visier.sdk.api.administration.models.production_versions_api_operation_response_dto import ProductionVersionsAPIOperationResponseDTO
from visier.sdk.api.administration.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.sdk.api.administration.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.sdk.api.administration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.sdk.api.administration.ProductionVersionsApi(api_client)
    production_versions_api_operation_request_dto = visier.sdk.api.administration.ProductionVersionsAPIOperationRequestDTO() # ProductionVersionsAPIOperationRequestDTO | 

    try:
        # Perform an operation on production versions
        api_response = api_instance.post_production_versions(production_versions_api_operation_request_dto)
        print("The response of ProductionVersionsApi->post_production_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionVersionsApi->post_production_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_versions_api_operation_request_dto** | [**ProductionVersionsAPIOperationRequestDTO**](ProductionVersionsAPIOperationRequestDTO.md)|  | 

### Return type

[**ProductionVersionsAPIOperationResponseDTO**](ProductionVersionsAPIOperationResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

