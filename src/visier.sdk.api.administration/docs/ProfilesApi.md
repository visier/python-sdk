# visier.sdk.api.administration.ProfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_analytic_profile**](ProfilesApi.md#assign_analytic_profile) | **PUT** /v1/admin/profiles/accessible-tenants/{profileId}/assign | Assign an analytic tenant profile to administrating tenant users
[**assign_profile**](ProfilesApi.md#assign_profile) | **PUT** /v1/admin/profiles/{profileId}/assign | Assign a profile to a list of users
[**get_all_profiles**](ProfilesApi.md#get_all_profiles) | **GET** /v1/admin/profiles | Retrieve a list of all profiles
[**get_analytic_profile_detail**](ProfilesApi.md#get_analytic_profile_detail) | **GET** /v1/admin/profiles/accessible-tenants/{profileId} | Retrieve the details of an analytic tenant profile
[**get_analytic_profiles**](ProfilesApi.md#get_analytic_profiles) | **GET** /v1/admin/profiles/accessible-tenants | Retrieve a list of analytic tenant profiles
[**get_analytic_user_profile**](ProfilesApi.md#get_analytic_user_profile) | **GET** /v1/admin/users/{userId}/accessible-tenant-profiles | Retrieve an administrating tenant user&#39;s analytic tenant profiles
[**get_profile_detail**](ProfilesApi.md#get_profile_detail) | **GET** /v1/admin/profiles/{profileId} | Retrieve the details of a profile
[**get_user_profile**](ProfilesApi.md#get_user_profile) | **GET** /v1/admin/users/{userId}/profiles | Retrieve a user&#39;s profiles
[**remove_analytic_profile**](ProfilesApi.md#remove_analytic_profile) | **DELETE** /v1/admin/profiles/accessible-tenants/{profileId}/remove | Remove an analytic tenant profile from administrating tenant users
[**remove_profile**](ProfilesApi.md#remove_profile) | **DELETE** /v1/admin/profiles/{profileId}/remove | Remove a profile from a list of users


# **assign_analytic_profile**
> AccessibleTenantProfileAssignmentResponseDTO assign_analytic_profile(profile_id, accessible_tenant_profile_assignment_request_dto)

Assign an analytic tenant profile to administrating tenant users

Assign an analytic tenant profile to a list of administrating tenant users  for a list of analytic tenants.   **Note:**   - Administrating tenants only.   - You can revoke a profile from a user with this request by updating the validityEndTime to be     \"less than\" the current time (that is, in the past).

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.accessible_tenant_profile_assignment_request_dto import AccessibleTenantProfileAssignmentRequestDTO
from visier.sdk.api.administration.models.accessible_tenant_profile_assignment_response_dto import AccessibleTenantProfileAssignmentResponseDTO
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
    api_instance = visier.sdk.api.administration.ProfilesApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile to assign.
    accessible_tenant_profile_assignment_request_dto = visier.sdk.api.administration.AccessibleTenantProfileAssignmentRequestDTO() # AccessibleTenantProfileAssignmentRequestDTO | 

    try:
        # Assign an analytic tenant profile to administrating tenant users
        api_response = api_instance.assign_analytic_profile(profile_id, accessible_tenant_profile_assignment_request_dto)
        print("The response of ProfilesApi->assign_analytic_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->assign_analytic_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile to assign. | 
 **accessible_tenant_profile_assignment_request_dto** | [**AccessibleTenantProfileAssignmentRequestDTO**](AccessibleTenantProfileAssignmentRequestDTO.md)|  | 

### Return type

[**AccessibleTenantProfileAssignmentResponseDTO**](AccessibleTenantProfileAssignmentResponseDTO.md)

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

# **assign_profile**
> LocalTenantProfileAssignmentResponseDTO assign_profile(profile_id, local_tenant_profile_assignment_request_dto)

Assign a profile to a list of users

Assign a profile to a list of users. For administrating tenants,  this assigns an administrating tenant profile to a list of users.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.local_tenant_profile_assignment_request_dto import LocalTenantProfileAssignmentRequestDTO
from visier.sdk.api.administration.models.local_tenant_profile_assignment_response_dto import LocalTenantProfileAssignmentResponseDTO
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
    api_instance = visier.sdk.api.administration.ProfilesApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile to assign to a list of users.
    local_tenant_profile_assignment_request_dto = visier.sdk.api.administration.LocalTenantProfileAssignmentRequestDTO() # LocalTenantProfileAssignmentRequestDTO | 

    try:
        # Assign a profile to a list of users
        api_response = api_instance.assign_profile(profile_id, local_tenant_profile_assignment_request_dto)
        print("The response of ProfilesApi->assign_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->assign_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile to assign to a list of users. | 
 **local_tenant_profile_assignment_request_dto** | [**LocalTenantProfileAssignmentRequestDTO**](LocalTenantProfileAssignmentRequestDTO.md)|  | 

### Return type

[**LocalTenantProfileAssignmentResponseDTO**](LocalTenantProfileAssignmentResponseDTO.md)

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

# **get_all_profiles**
> ProfilesGetAPIResponseDTO get_all_profiles()

Retrieve a list of all profiles

Get a list of all available profiles. For administrating tenants,  this retrieves all administrating tenant profiles.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.profiles_get_api_response_dto import ProfilesGetAPIResponseDTO
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
    api_instance = visier.sdk.api.administration.ProfilesApi(api_client)

    try:
        # Retrieve a list of all profiles
        api_response = api_instance.get_all_profiles()
        print("The response of ProfilesApi->get_all_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_all_profiles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProfilesGetAPIResponseDTO**](ProfilesGetAPIResponseDTO.md)

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

# **get_analytic_profile_detail**
> ProfileGetAPIResponseDTO get_analytic_profile_detail(profile_id)

Retrieve the details of an analytic tenant profile

Get the details of an analytic tenant profile.   **Note:** Administrating tenants only.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.profile_get_api_response_dto import ProfileGetAPIResponseDTO
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
    api_instance = visier.sdk.api.administration.ProfilesApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile to retrieve details for.

    try:
        # Retrieve the details of an analytic tenant profile
        api_response = api_instance.get_analytic_profile_detail(profile_id)
        print("The response of ProfilesApi->get_analytic_profile_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_analytic_profile_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile to retrieve details for. | 

### Return type

[**ProfileGetAPIResponseDTO**](ProfileGetAPIResponseDTO.md)

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

# **get_analytic_profiles**
> ProfilesGetAPIResponseDTO get_analytic_profiles()

Retrieve a list of analytic tenant profiles

Retrieve a list of profiles available for analytic tenants.   **Note:** Administrating tenants only.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.profiles_get_api_response_dto import ProfilesGetAPIResponseDTO
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
    api_instance = visier.sdk.api.administration.ProfilesApi(api_client)

    try:
        # Retrieve a list of analytic tenant profiles
        api_response = api_instance.get_analytic_profiles()
        print("The response of ProfilesApi->get_analytic_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_analytic_profiles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProfilesGetAPIResponseDTO**](ProfilesGetAPIResponseDTO.md)

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

# **get_analytic_user_profile**
> AllProfileAssignedForAccessibleTenantDTO get_analytic_user_profile(user_id)

Retrieve an administrating tenant user's analytic tenant profiles

Retrieve a specified user's assigned profiles for analytic tenants.   **Note:** Administrating tenants only.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.all_profile_assigned_for_accessible_tenant_dto import AllProfileAssignedForAccessibleTenantDTO
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
    api_instance = visier.sdk.api.administration.ProfilesApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user you want to retrieve.

    try:
        # Retrieve an administrating tenant user's analytic tenant profiles
        api_response = api_instance.get_analytic_user_profile(user_id)
        print("The response of ProfilesApi->get_analytic_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_analytic_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user you want to retrieve. | 

### Return type

[**AllProfileAssignedForAccessibleTenantDTO**](AllProfileAssignedForAccessibleTenantDTO.md)

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

# **get_profile_detail**
> ProfileGetAPIResponseDTO get_profile_detail(profile_id)

Retrieve the details of a profile

Get the details of a specific profile. For administrating tenants, this retrieves  the details of administrating tenant profiles.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.profile_get_api_response_dto import ProfileGetAPIResponseDTO
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
    api_instance = visier.sdk.api.administration.ProfilesApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile to retrieve details for.

    try:
        # Retrieve the details of a profile
        api_response = api_instance.get_profile_detail(profile_id)
        print("The response of ProfilesApi->get_profile_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_profile_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile to retrieve details for. | 

### Return type

[**ProfileGetAPIResponseDTO**](ProfileGetAPIResponseDTO.md)

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

# **get_user_profile**
> AllProfileAssignedForLocalTenantDTO get_user_profile(user_id)

Retrieve a user's profiles

Retrieve a specified user's assigned profiles. For administrating tenants,  this retrieves a user's administrating tenant profiles.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.all_profile_assigned_for_local_tenant_dto import AllProfileAssignedForLocalTenantDTO
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
    api_instance = visier.sdk.api.administration.ProfilesApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user you want to retrieve.

    try:
        # Retrieve a user's profiles
        api_response = api_instance.get_user_profile(user_id)
        print("The response of ProfilesApi->get_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user you want to retrieve. | 

### Return type

[**AllProfileAssignedForLocalTenantDTO**](AllProfileAssignedForLocalTenantDTO.md)

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

# **remove_analytic_profile**
> AccessibleTenantProfileRevokeResponseDTO remove_analytic_profile(profile_id, accessible_tenant_profile_revoke_request_dto)

Remove an analytic tenant profile from administrating tenant users

Remove an analytic tenant profile from a list of administrating tenant users for a list of analytic tenants.   **Note:** Administrating tenants only.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.accessible_tenant_profile_revoke_request_dto import AccessibleTenantProfileRevokeRequestDTO
from visier.sdk.api.administration.models.accessible_tenant_profile_revoke_response_dto import AccessibleTenantProfileRevokeResponseDTO
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
    api_instance = visier.sdk.api.administration.ProfilesApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile to remove.
    accessible_tenant_profile_revoke_request_dto = visier.sdk.api.administration.AccessibleTenantProfileRevokeRequestDTO() # AccessibleTenantProfileRevokeRequestDTO | 

    try:
        # Remove an analytic tenant profile from administrating tenant users
        api_response = api_instance.remove_analytic_profile(profile_id, accessible_tenant_profile_revoke_request_dto)
        print("The response of ProfilesApi->remove_analytic_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->remove_analytic_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile to remove. | 
 **accessible_tenant_profile_revoke_request_dto** | [**AccessibleTenantProfileRevokeRequestDTO**](AccessibleTenantProfileRevokeRequestDTO.md)|  | 

### Return type

[**AccessibleTenantProfileRevokeResponseDTO**](AccessibleTenantProfileRevokeResponseDTO.md)

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

# **remove_profile**
> LocalTenantProfileRevokeResponseDTO remove_profile(profile_id, local_tenant_profile_revoke_request_dto)

Remove a profile from a list of users

Remove a profile from a list of users. For administrating tenants, this  removes an administrating tenant profile from a list of users.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.local_tenant_profile_revoke_request_dto import LocalTenantProfileRevokeRequestDTO
from visier.sdk.api.administration.models.local_tenant_profile_revoke_response_dto import LocalTenantProfileRevokeResponseDTO
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
    api_instance = visier.sdk.api.administration.ProfilesApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile to remove to a list of users.
    local_tenant_profile_revoke_request_dto = visier.sdk.api.administration.LocalTenantProfileRevokeRequestDTO() # LocalTenantProfileRevokeRequestDTO | 

    try:
        # Remove a profile from a list of users
        api_response = api_instance.remove_profile(profile_id, local_tenant_profile_revoke_request_dto)
        print("The response of ProfilesApi->remove_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->remove_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile to remove to a list of users. | 
 **local_tenant_profile_revoke_request_dto** | [**LocalTenantProfileRevokeRequestDTO**](LocalTenantProfileRevokeRequestDTO.md)|  | 

### Return type

[**LocalTenantProfileRevokeResponseDTO**](LocalTenantProfileRevokeResponseDTO.md)

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

