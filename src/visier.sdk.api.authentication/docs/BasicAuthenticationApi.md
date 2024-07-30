# visier.sdk.api.authentication.BasicAuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**a_sid_token_authentication**](BasicAuthenticationApi.md#a_sid_token_authentication) | **POST** /v1/admin/visierSecureToken | Request a Visier authentication token
[**generate_impersonation_token**](BasicAuthenticationApi.md#generate_impersonation_token) | **POST** /v1/admin/visierImpersonationToken | Request an impersonation token


# **a_sid_token_authentication**
> str a_sid_token_authentication(password=password, username=username)

Request a Visier authentication token

Generate a secure ASID token.

### Example


```python
import visier.sdk.api.authentication
from visier.sdk.api.authentication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.sdk.api.authentication.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.sdk.api.authentication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.sdk.api.authentication.BasicAuthenticationApi(api_client)
    password = 'password_example' # str | The password that corresponds to the user making the request. (optional)
    username = 'username_example' # str | The unique identifier of the API user requesting a security token. (optional)

    try:
        # Request a Visier authentication token
        api_response = api_instance.a_sid_token_authentication(password=password, username=username)
        print("The response of BasicAuthenticationApi->a_sid_token_authentication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicAuthenticationApi->a_sid_token_authentication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| The password that corresponds to the user making the request. | [optional] 
 **username** | **str**| The unique identifier of the API user requesting a security token. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authentication token response |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_impersonation_token**
> str generate_impersonation_token(generate_impersonation_token_request, target_tenant_id=target_tenant_id)

Request an impersonation token

Generate an impersonation token for the given username.

### Example


```python
import visier.sdk.api.authentication
from visier.sdk.api.authentication.models.generate_impersonation_token_request import GenerateImpersonationTokenRequest
from visier.sdk.api.authentication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.sdk.api.authentication.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.sdk.api.authentication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.sdk.api.authentication.BasicAuthenticationApi(api_client)
    generate_impersonation_token_request = visier.sdk.api.authentication.GenerateImpersonationTokenRequest() # GenerateImpersonationTokenRequest | Request to generate an impersonation token.
    target_tenant_id = 'target_tenant_id_example' # str | The tenant ID to execute the call on. (optional)

    try:
        # Request an impersonation token
        api_response = api_instance.generate_impersonation_token(generate_impersonation_token_request, target_tenant_id=target_tenant_id)
        print("The response of BasicAuthenticationApi->generate_impersonation_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicAuthenticationApi->generate_impersonation_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_impersonation_token_request** | [**GenerateImpersonationTokenRequest**](GenerateImpersonationTokenRequest.md)| Request to generate an impersonation token. | 
 **target_tenant_id** | **str**| The tenant ID to execute the call on. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Impersonation token response |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

