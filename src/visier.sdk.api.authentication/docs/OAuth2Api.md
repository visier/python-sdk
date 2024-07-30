# visier.sdk.api.authentication.OAuth2Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_auth2_token**](OAuth2Api.md#o_auth2_token) | **POST** /v1/auth/oauth2/token | Request a JSON Web Token.
[**oauth2_authorize**](OAuth2Api.md#oauth2_authorize) | **GET** /v1/auth/oauth2/authorize | Request an authorization code.
[**user_info**](OAuth2Api.md#user_info) | **GET** /v1/auth/oauth2/userinfo | Retrieve the user-specific metadata


# **o_auth2_token**
> str o_auth2_token(asid_token=asid_token, client_id=client_id, code=code, grant_type=grant_type, password=password, redirect_uri=redirect_uri, username=username)

Request a JSON Web Token.

Use an OAuth 2.0 grant type to request a JWT.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import visier.sdk.api.authentication
from visier.sdk.api.authentication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.sdk.api.authentication.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = visier.sdk.api.authentication.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with visier.sdk.api.authentication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.sdk.api.authentication.OAuth2Api(api_client)
    asid_token = 'asid_token_example' # str | The ASID token. Applicable only for ASID token grant type. (optional)
    client_id = 'client_id_example' # str | The ID of the pre-registered client application. (optional)
    code = 'code_example' # str | The authorization code. Applicable only for authorization code grant type. (optional)
    grant_type = 'grant_type_example' # str | The grant type. Supported values: - `authorization_code`: The authorization code grant type. - `password`: The password grant type. - `urn:ietf:params:oauth:grant-type:saml2-bearer`: The saml2-bearer grant type. - `urn:visier:params:oauth:grant-type:asid-token`: The ASID token grant type. (optional)
    password = 'password_example' # str | The password of the user to authenticate. Applicable only for password grant type. (optional)
    redirect_uri = 'redirect_uri_example' # str | The optional URI to redirect to after authorization. (optional)
    username = 'username_example' # str | The username of the user to authenticate. Applicable only for password grant type. (optional)

    try:
        # Request a JSON Web Token.
        api_response = api_instance.o_auth2_token(asid_token=asid_token, client_id=client_id, code=code, grant_type=grant_type, password=password, redirect_uri=redirect_uri, username=username)
        print("The response of OAuth2Api->o_auth2_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2Api->o_auth2_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asid_token** | **str**| The ASID token. Applicable only for ASID token grant type. | [optional] 
 **client_id** | **str**| The ID of the pre-registered client application. | [optional] 
 **code** | **str**| The authorization code. Applicable only for authorization code grant type. | [optional] 
 **grant_type** | **str**| The grant type. Supported values: - &#x60;authorization_code&#x60;: The authorization code grant type. - &#x60;password&#x60;: The password grant type. - &#x60;urn:ietf:params:oauth:grant-type:saml2-bearer&#x60;: The saml2-bearer grant type. - &#x60;urn:visier:params:oauth:grant-type:asid-token&#x60;: The ASID token grant type. | [optional] 
 **password** | **str**| The password of the user to authenticate. Applicable only for password grant type. | [optional] 
 **redirect_uri** | **str**| The optional URI to redirect to after authorization. | [optional] 
 **username** | **str**| The username of the user to authenticate. Applicable only for password grant type. | [optional] 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/jwt

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JSON Web Token. Use this token in your API calls to authenticate the call. |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth2_authorize**
> Status oauth2_authorize(response_type, client_id, redirect_uri=redirect_uri, scope=scope)

Request an authorization code.

Request an authorization code for the authorization_code grant type. Not required in other OAuth 2.0 grant types.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import visier.sdk.api.authentication
from visier.sdk.api.authentication.models.status import Status
from visier.sdk.api.authentication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.sdk.api.authentication.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with visier.sdk.api.authentication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.sdk.api.authentication.OAuth2Api(api_client)
    response_type = 'response_type_example' # str | The response type. Must be `code`.
    client_id = 'client_id_example' # str | The ID of the pre-registered client application.
    redirect_uri = 'redirect_uri_example' # str | The optional URI to redirect to after authorization. (optional)
    scope = 'scope_example' # str | The OAuth 2.0 scope of the authorization request. Default is `read`. If the scope includes `visier:login:bypass_users`, then the redirect login URL ends in \"/auth/admin\" instead of \"/auth\". This allows single sign-on (SSO) Bypass Users to login through Visier instead of being redirected to the SSO login page. (optional)

    try:
        # Request an authorization code.
        api_response = api_instance.oauth2_authorize(response_type, client_id, redirect_uri=redirect_uri, scope=scope)
        print("The response of OAuth2Api->oauth2_authorize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2Api->oauth2_authorize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_type** | **str**| The response type. Must be &#x60;code&#x60;. | 
 **client_id** | **str**| The ID of the pre-registered client application. | 
 **redirect_uri** | **str**| The optional URI to redirect to after authorization. | [optional] 
 **scope** | **str**| The OAuth 2.0 scope of the authorization request. Default is &#x60;read&#x60;. If the scope includes &#x60;visier:login:bypass_users&#x60;, then the redirect login URL ends in \&quot;/auth/admin\&quot; instead of \&quot;/auth\&quot;. This allows single sign-on (SSO) Bypass Users to login through Visier instead of being redirected to the SSO login page. | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**3XX** | Redirect to authorization page. |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_info**
> OAuth2UserInfoDTO user_info(include_tenant_details=include_tenant_details)

Retrieve the user-specific metadata

Retrieve user-specific metadata, such as a user's ID, username, and profile capabilities.

### Example


```python
import visier.sdk.api.authentication
from visier.sdk.api.authentication.models.o_auth2_user_info_dto import OAuth2UserInfoDTO
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
    api_instance = visier.sdk.api.authentication.OAuth2Api(api_client)
    include_tenant_details = True # bool | If `true`, includes tenant details in the response. Default is `false`. (optional)

    try:
        # Retrieve the user-specific metadata
        api_response = api_instance.user_info(include_tenant_details=include_tenant_details)
        print("The response of OAuth2Api->user_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2Api->user_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_tenant_details** | **bool**| If &#x60;true&#x60;, includes tenant details in the response. Default is &#x60;false&#x60;. | [optional] 

### Return type

[**OAuth2UserInfoDTO**](OAuth2UserInfoDTO.md)

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

