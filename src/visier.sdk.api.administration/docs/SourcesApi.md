# visier.sdk.api.administration.SourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**put_sources**](SourcesApi.md#put_sources) | **PUT** /v1alpha/admin/sources | Import a ZIP file that contains a list of sources
[**run_sources_operation**](SourcesApi.md#run_sources_operation) | **POST** /v1alpha/admin/sources | Perform an operation on the collection of all sources


# **put_sources**
> SourcesAPIPutResponseDTO put_sources(replace_all_existing_sources=replace_all_existing_sources)

Import a ZIP file that contains a list of sources

*  Import a ZIP file that contains a list of sources. The file must be an export from `POST /v1alpha/admin/sources`. Use this API after making changes in a development environment to copy the changes to a draft project in your production environment.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.sources_api_put_response_dto import SourcesAPIPutResponseDTO
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
    api_instance = visier.sdk.api.administration.SourcesApi(api_client)
    replace_all_existing_sources = True # bool | `false` if the sources from the ZIP archive should be added to the sources in the target tenant. `true` if all sources in the target tenant should be removed while importing the ZIP archive. (optional)

    try:
        # Import a ZIP file that contains a list of sources
        api_response = api_instance.put_sources(replace_all_existing_sources=replace_all_existing_sources)
        print("The response of SourcesApi->put_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->put_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replace_all_existing_sources** | **bool**| &#x60;false&#x60; if the sources from the ZIP archive should be added to the sources in the target tenant. &#x60;true&#x60; if all sources in the target tenant should be removed while importing the ZIP archive. | [optional] 

### Return type

[**SourcesAPIPutResponseDTO**](SourcesAPIPutResponseDTO.md)

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

# **run_sources_operation**
> object run_sources_operation(sources_api_operation_request_dto)

Perform an operation on the collection of all sources

Perform operations on the collection of sources. The following operations are supported:  * `exportSources`: Export a ZIP file that contains a list of all sources in the application.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.sources_api_operation_request_dto import SourcesAPIOperationRequestDTO
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
    api_instance = visier.sdk.api.administration.SourcesApi(api_client)
    sources_api_operation_request_dto = visier.sdk.api.administration.SourcesAPIOperationRequestDTO() # SourcesAPIOperationRequestDTO | 

    try:
        # Perform an operation on the collection of all sources
        api_response = api_instance.run_sources_operation(sources_api_operation_request_dto)
        print("The response of SourcesApi->run_sources_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->run_sources_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sources_api_operation_request_dto** | [**SourcesAPIOperationRequestDTO**](SourcesAPIOperationRequestDTO.md)|  | 

### Return type

**object**

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

