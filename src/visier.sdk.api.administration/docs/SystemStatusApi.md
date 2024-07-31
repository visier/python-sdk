# visier.sdk.api.administration.SystemStatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_system_status**](SystemStatusApi.md#post_system_status) | **POST** /v1/admin/system-status | Check the overall current status of Visier&#39;s systems
[**system_status**](SystemStatusApi.md#system_status) | **GET** /v1/admin/system-status | Check the overall current status of Visier&#39;s systems


# **post_system_status**
> SystemStatusDTO post_system_status()

Check the overall current status of Visier's systems

Check the current overall status of Visier's systems.   The overall status is one of:  * ``UP`` : All systems are operational.  * `DOWN`: At least one system is not fully operational.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.system_status_dto import SystemStatusDTO
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
    api_instance = visier.sdk.api.administration.SystemStatusApi(api_client)

    try:
        # Check the overall current status of Visier's systems
        api_response = api_instance.post_system_status()
        print("The response of SystemStatusApi->post_system_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemStatusApi->post_system_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemStatusDTO**](SystemStatusDTO.md)

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

# **system_status**
> SystemStatusDTO system_status()

Check the overall current status of Visier's systems

Check the current overall status of Visier's systems.   The overall status is one of:  * ``UP`` : All systems are operational.  * `DOWN`: At least one system is not fully operational.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.system_status_dto import SystemStatusDTO
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
    api_instance = visier.sdk.api.administration.SystemStatusApi(api_client)

    try:
        # Check the overall current status of Visier's systems
        api_response = api_instance.system_status()
        print("The response of SystemStatusApi->system_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemStatusApi->system_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemStatusDTO**](SystemStatusDTO.md)

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

