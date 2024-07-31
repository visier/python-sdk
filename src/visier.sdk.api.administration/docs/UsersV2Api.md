# visier.sdk.api.administration.UsersV2Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_users**](UsersV2Api.md#add_users) | **POST** /v2/admin/users | Add users
[**delete_users**](UsersV2Api.md#delete_users) | **DELETE** /v2/admin/users | Delete users
[**update_users**](UsersV2Api.md#update_users) | **PUT** /v2/admin/users | Update users


# **add_users**
> UsersAPIResponseDTO add_users(users_creation_api_request_dto, tenant_code=tenant_code)

Add users

Create new users. Administrating tenant users can specify the tenant in which to add these users.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.users_api_response_dto import UsersAPIResponseDTO
from visier.sdk.api.administration.models.users_creation_api_request_dto import UsersCreationAPIRequestDTO
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
    api_instance = visier.sdk.api.administration.UsersV2Api(api_client)
    users_creation_api_request_dto = visier.sdk.api.administration.UsersCreationAPIRequestDTO() # UsersCreationAPIRequestDTO | 
    tenant_code = 'tenant_code_example' # str | Specify the tenant to create a user in. (optional)

    try:
        # Add users
        api_response = api_instance.add_users(users_creation_api_request_dto, tenant_code=tenant_code)
        print("The response of UsersV2Api->add_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->add_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_creation_api_request_dto** | [**UsersCreationAPIRequestDTO**](UsersCreationAPIRequestDTO.md)|  | 
 **tenant_code** | **str**| Specify the tenant to create a user in. | [optional] 

### Return type

[**UsersAPIResponseDTO**](UsersAPIResponseDTO.md)

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

# **delete_users**
> UsersAPIResponseDTO delete_users(users_delete_api_request_dto, tenant_code=tenant_code)

Delete users

Delete an existing user. Administrating tenant users can specify the tenant from which to delete a user.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.users_api_response_dto import UsersAPIResponseDTO
from visier.sdk.api.administration.models.users_delete_api_request_dto import UsersDeleteAPIRequestDTO
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
    api_instance = visier.sdk.api.administration.UsersV2Api(api_client)
    users_delete_api_request_dto = visier.sdk.api.administration.UsersDeleteAPIRequestDTO() # UsersDeleteAPIRequestDTO | 
    tenant_code = 'tenant_code_example' # str | Specify the tenant to delete a user in. (optional)

    try:
        # Delete users
        api_response = api_instance.delete_users(users_delete_api_request_dto, tenant_code=tenant_code)
        print("The response of UsersV2Api->delete_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->delete_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_delete_api_request_dto** | [**UsersDeleteAPIRequestDTO**](UsersDeleteAPIRequestDTO.md)|  | 
 **tenant_code** | **str**| Specify the tenant to delete a user in. | [optional] 

### Return type

[**UsersAPIResponseDTO**](UsersAPIResponseDTO.md)

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

# **update_users**
> UsersAPIResponseDTO update_users(users_update_api_request_dto, tenant_code=tenant_code)

Update users

Update an existing user's information, such as their display name or if the user is enabled in Visier.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.users_api_response_dto import UsersAPIResponseDTO
from visier.sdk.api.administration.models.users_update_api_request_dto import UsersUpdateAPIRequestDTO
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
    api_instance = visier.sdk.api.administration.UsersV2Api(api_client)
    users_update_api_request_dto = visier.sdk.api.administration.UsersUpdateAPIRequestDTO() # UsersUpdateAPIRequestDTO | 
    tenant_code = 'tenant_code_example' # str | Specify the tenant to update a user in. (optional)

    try:
        # Update users
        api_response = api_instance.update_users(users_update_api_request_dto, tenant_code=tenant_code)
        print("The response of UsersV2Api->update_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->update_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_update_api_request_dto** | [**UsersUpdateAPIRequestDTO**](UsersUpdateAPIRequestDTO.md)|  | 
 **tenant_code** | **str**| Specify the tenant to update a user in. | [optional] 

### Return type

[**UsersAPIResponseDTO**](UsersAPIResponseDTO.md)

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

