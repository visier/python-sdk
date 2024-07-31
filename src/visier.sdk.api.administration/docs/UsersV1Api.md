# visier.sdk.api.administration.UsersV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](UsersV1Api.md#add_user) | **POST** /v1/admin/users | Add a user
[**add_users_to_user_group**](UsersV1Api.md#add_users_to_user_group) | **PUT** /v1/admin/user-groups/users | Assign users to user groups
[**assign_permissions**](UsersV1Api.md#assign_permissions) | **PUT** /v1/admin/permissions/users | Assign permissions to users
[**assign_permissions_to_user_groups**](UsersV1Api.md#assign_permissions_to_user_groups) | **PUT** /v1/admin/user-groups/permissions | Assign permissions to user groups
[**delete_user**](UsersV1Api.md#delete_user) | **DELETE** /v1/admin/users/{userId} | Delete a user
[**get_all_permissions_xlsx**](UsersV1Api.md#get_all_permissions_xlsx) | **GET** /v1/admin/users/reports/permissions-list | Retrieve a list of all permissions in XLSX format
[**get_all_user_groups**](UsersV1Api.md#get_all_user_groups) | **GET** /v1/admin/user-groups | Retrieve a list of all user groups
[**get_all_users**](UsersV1Api.md#get_all_users) | **GET** /v1/admin/users | Retrieve a list of all users
[**get_application_logs_xlsx**](UsersV1Api.md#get_application_logs_xlsx) | **GET** /v1/admin/users/reports/application-logs | Retrieve the Application Logs
[**get_data_security_report_xlsx**](UsersV1Api.md#get_data_security_report_xlsx) | **GET** /v1/admin/users/{userId}/reports/data-security | Retrieve the Data Security Report
[**get_permission_assigned_users**](UsersV1Api.md#get_permission_assigned_users) | **GET** /v1/admin/permissions/{permissionId}/users | Retrieve users that are assigned a specific permission
[**get_profile_assignments_xlsx**](UsersV1Api.md#get_profile_assignments_xlsx) | **GET** /v1/admin/users/reports/profile-assignments | Retrieve user profile assignments in XLSX format
[**get_user_detail**](UsersV1Api.md#get_user_detail) | **GET** /v1/admin/users/{userId} | Retrieve a user&#39;s details
[**get_user_group_users**](UsersV1Api.md#get_user_group_users) | **GET** /v1/admin/user-groups/{userGroupId}/users | Retrieve a list of user group users
[**get_user_permissions_xlsx**](UsersV1Api.md#get_user_permissions_xlsx) | **GET** /v1/admin/users/reports/permission-assignments | Retrieve user permissions in XLSX format
[**remove_permissions**](UsersV1Api.md#remove_permissions) | **DELETE** /v1/admin/permissions/users | Remove permissions from users
[**remove_users_from_user_group**](UsersV1Api.md#remove_users_from_user_group) | **DELETE** /v1/admin/user-groups/users | Remove users from user groups
[**revoke_permissions_from_user_groups**](UsersV1Api.md#revoke_permissions_from_user_groups) | **DELETE** /v1/admin/user-groups/permissions | Remove permissions from user groups
[**update_user**](UsersV1Api.md#update_user) | **PUT** /v1/admin/users/{userId} | Update a user


# **add_user**
> UserCreationAPIResponseDTO add_user(user_creation_api_request_dto, tenant_code=tenant_code)

Add a user

Create a new user. Administrating tenant users can specify the tenant in which to add a user.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.user_creation_api_request_dto import UserCreationAPIRequestDTO
from visier.sdk.api.administration.models.user_creation_api_response_dto import UserCreationAPIResponseDTO
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    user_creation_api_request_dto = visier.sdk.api.administration.UserCreationAPIRequestDTO() # UserCreationAPIRequestDTO | 
    tenant_code = 'tenant_code_example' # str | Specify the tenant to create a user in. (optional)

    try:
        # Add a user
        api_response = api_instance.add_user(user_creation_api_request_dto, tenant_code=tenant_code)
        print("The response of UsersV1Api->add_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->add_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_creation_api_request_dto** | [**UserCreationAPIRequestDTO**](UserCreationAPIRequestDTO.md)|  | 
 **tenant_code** | **str**| Specify the tenant to create a user in. | [optional] 

### Return type

[**UserCreationAPIResponseDTO**](UserCreationAPIResponseDTO.md)

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

# **add_users_to_user_group**
> SecurityAssignmentResponseDTO add_users_to_user_group(users_to_user_groups_request_dto, project_id=project_id, target_tenant_id=target_tenant_id)

Assign users to user groups

This API allows you to assign users to specific user groups.   To assign users to user groups in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can assign users to user groups in analytic tenants by providing a tenant code and project ID in the request body.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.security_assignment_response_dto import SecurityAssignmentResponseDTO
from visier.sdk.api.administration.models.users_to_user_groups_request_dto import UsersToUserGroupsRequestDTO
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    users_to_user_groups_request_dto = visier.sdk.api.administration.UsersToUserGroupsRequestDTO() # UsersToUserGroupsRequestDTO | 
    project_id = 'project_id_example' # str | Optionally, specify a project in which to make the request. If omitted, the request uses the production version. (optional)
    target_tenant_id = 'target_tenant_id_example' # str | Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant. (optional)

    try:
        # Assign users to user groups
        api_response = api_instance.add_users_to_user_group(users_to_user_groups_request_dto, project_id=project_id, target_tenant_id=target_tenant_id)
        print("The response of UsersV1Api->add_users_to_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->add_users_to_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_to_user_groups_request_dto** | [**UsersToUserGroupsRequestDTO**](UsersToUserGroupsRequestDTO.md)|  | 
 **project_id** | **str**| Optionally, specify a project in which to make the request. If omitted, the request uses the production version. | [optional] 
 **target_tenant_id** | **str**| Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you&#39;re logged into. If omitted, the request uses the administrating tenant as the login tenant. | [optional] 

### Return type

[**SecurityAssignmentResponseDTO**](SecurityAssignmentResponseDTO.md)

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

# **assign_permissions**
> AssignRevokePermissionsResponseDTO assign_permissions(assign_revoke_permissions_request_dto, project_id=project_id, target_tenant_id=target_tenant_id)

Assign permissions to users

This API allows you to assign a permission to specific users. Administrating tenant users can assign permissions  to users in the administrating tenant and in the analytic tenants those users belong to.   To assign permissions to users in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can assign permissions to users in analytic tenants by providing a tenant code and project ID in the request body.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.assign_revoke_permissions_request_dto import AssignRevokePermissionsRequestDTO
from visier.sdk.api.administration.models.assign_revoke_permissions_response_dto import AssignRevokePermissionsResponseDTO
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    assign_revoke_permissions_request_dto = visier.sdk.api.administration.AssignRevokePermissionsRequestDTO() # AssignRevokePermissionsRequestDTO | 
    project_id = 'project_id_example' # str | Optionally, specify a project in which to make the request. If omitted, the request uses the production version. (optional)
    target_tenant_id = 'target_tenant_id_example' # str | Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant. (optional)

    try:
        # Assign permissions to users
        api_response = api_instance.assign_permissions(assign_revoke_permissions_request_dto, project_id=project_id, target_tenant_id=target_tenant_id)
        print("The response of UsersV1Api->assign_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->assign_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_revoke_permissions_request_dto** | [**AssignRevokePermissionsRequestDTO**](AssignRevokePermissionsRequestDTO.md)|  | 
 **project_id** | **str**| Optionally, specify a project in which to make the request. If omitted, the request uses the production version. | [optional] 
 **target_tenant_id** | **str**| Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you&#39;re logged into. If omitted, the request uses the administrating tenant as the login tenant. | [optional] 

### Return type

[**AssignRevokePermissionsResponseDTO**](AssignRevokePermissionsResponseDTO.md)

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

# **assign_permissions_to_user_groups**
> PermissionsToUserGroupForTenantDTO assign_permissions_to_user_groups(permissions_to_user_groups_request_dto, project_id=project_id, target_tenant_id=target_tenant_id)

Assign permissions to user groups

This API allows you to assign a permission to specific user groups. This assigns the permission to all users in the user group.   To assign permissions to user groups in a project, provide a project UUID in the `ProjectID` request header.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.permissions_to_user_group_for_tenant_dto import PermissionsToUserGroupForTenantDTO
from visier.sdk.api.administration.models.permissions_to_user_groups_request_dto import PermissionsToUserGroupsRequestDTO
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    permissions_to_user_groups_request_dto = visier.sdk.api.administration.PermissionsToUserGroupsRequestDTO() # PermissionsToUserGroupsRequestDTO | 
    project_id = 'project_id_example' # str | Optionally, specify a project in which to make the request. If omitted, the request uses the production version. (optional)
    target_tenant_id = 'target_tenant_id_example' # str | Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant. (optional)

    try:
        # Assign permissions to user groups
        api_response = api_instance.assign_permissions_to_user_groups(permissions_to_user_groups_request_dto, project_id=project_id, target_tenant_id=target_tenant_id)
        print("The response of UsersV1Api->assign_permissions_to_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->assign_permissions_to_user_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissions_to_user_groups_request_dto** | [**PermissionsToUserGroupsRequestDTO**](PermissionsToUserGroupsRequestDTO.md)|  | 
 **project_id** | **str**| Optionally, specify a project in which to make the request. If omitted, the request uses the production version. | [optional] 
 **target_tenant_id** | **str**| Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you&#39;re logged into. If omitted, the request uses the administrating tenant as the login tenant. | [optional] 

### Return type

[**PermissionsToUserGroupForTenantDTO**](PermissionsToUserGroupForTenantDTO.md)

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

# **delete_user**
> object delete_user(user_id, tenant_code=tenant_code)

Delete a user

Delete an existing user. Administrating tenant users can specify the tenant from which to delete a user.

### Example


```python
import visier.sdk.api.administration
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    user_id = 'user_id_example' # str | The ID of the user you want to delete.
    tenant_code = 'tenant_code_example' # str | Specify the tenant to delete a user in. (optional)

    try:
        # Delete a user
        api_response = api_instance.delete_user(user_id, tenant_code=tenant_code)
        print("The response of UsersV1Api->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user you want to delete. | 
 **tenant_code** | **str**| Specify the tenant to delete a user in. | [optional] 

### Return type

**object**

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

# **get_all_permissions_xlsx**
> bytearray get_all_permissions_xlsx(tenant_code=tenant_code)

Retrieve a list of all permissions in XLSX format

This API allows you to export the list of permissions in a tenant. This report includes the permission name,  permission description, and permission ID for all permissions in the tenant.   Administrating tenant users can export permissions lists for the administrating tenant and the analytic tenants  those users belong to.

### Example


```python
import visier.sdk.api.administration
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve permissions from. (optional)

    try:
        # Retrieve a list of all permissions in XLSX format
        api_response = api_instance.get_all_permissions_xlsx(tenant_code=tenant_code)
        print("The response of UsersV1Api->get_all_permissions_xlsx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->get_all_permissions_xlsx: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_code** | **str**| Specify the tenant to retrieve permissions from. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An XLSX file. |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user_groups**
> UserGroupsGetAPIResponseDTO get_all_user_groups(tenant_code=tenant_code, limit=limit, start=start, project_id=project_id, target_tenant_id=target_tenant_id)

Retrieve a list of all user groups

This API allows you to retrieve the full list of user groups in a tenant.   To specify the project in which to retrieve user groups for a tenant, provide a project UUID in the `ProjectID` request header. If omitted, the request retrieves user information from production.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.user_groups_get_api_response_dto import UserGroupsGetAPIResponseDTO
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve the list of user groups from. (optional)
    limit = 56 # int | The number of results to return. The maximum number of users to retrieve is 1000. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. (optional)
    project_id = 'project_id_example' # str | Optionally, specify a project in which to make the request. If omitted, the request uses the production version. (optional)
    target_tenant_id = 'target_tenant_id_example' # str | Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant. (optional)

    try:
        # Retrieve a list of all user groups
        api_response = api_instance.get_all_user_groups(tenant_code=tenant_code, limit=limit, start=start, project_id=project_id, target_tenant_id=target_tenant_id)
        print("The response of UsersV1Api->get_all_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->get_all_user_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_code** | **str**| Specify the tenant to retrieve the list of user groups from. | [optional] 
 **limit** | **int**| The number of results to return. The maximum number of users to retrieve is 1000. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. | [optional] 
 **project_id** | **str**| Optionally, specify a project in which to make the request. If omitted, the request uses the production version. | [optional] 
 **target_tenant_id** | **str**| Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you&#39;re logged into. If omitted, the request uses the administrating tenant as the login tenant. | [optional] 

### Return type

[**UserGroupsGetAPIResponseDTO**](UserGroupsGetAPIResponseDTO.md)

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

# **get_all_users**
> AllUsersGetAPIResponseDTO get_all_users(tenant_code=tenant_code, assigned_profiles=assigned_profiles, assigned_permissions=assigned_permissions, assigned_user_groups=assigned_user_groups, limit=limit, start=start, project_id=project_id, target_tenant_id=target_tenant_id)

Retrieve a list of all users

This API allows you to retrieve the full list of users and their current states.   To specify the project in which to retrieve user information, provide a project UUID in the `ProjectID` request header. If omitted, the request retrieves user information from production.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.all_users_get_api_response_dto import AllUsersGetAPIResponseDTO
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve a list of users from. (optional)
    assigned_profiles = True # bool | If true, the response returns a list of the user's assigned profiles. (optional)
    assigned_permissions = True # bool | If true, the response returns the user's assigned permissions. (optional)
    assigned_user_groups = True # bool | If true, the response returns the user's assigned user groups. (optional)
    limit = 56 # int | The number of results to return. The maximum number of users to retrieve is 1000. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)
    project_id = 'project_id_example' # str | Optionally, specify a project in which to make the request. If omitted, the request uses the production version. (optional)
    target_tenant_id = 'target_tenant_id_example' # str | Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant. (optional)

    try:
        # Retrieve a list of all users
        api_response = api_instance.get_all_users(tenant_code=tenant_code, assigned_profiles=assigned_profiles, assigned_permissions=assigned_permissions, assigned_user_groups=assigned_user_groups, limit=limit, start=start, project_id=project_id, target_tenant_id=target_tenant_id)
        print("The response of UsersV1Api->get_all_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->get_all_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_code** | **str**| Specify the tenant to retrieve a list of users from. | [optional] 
 **assigned_profiles** | **bool**| If true, the response returns a list of the user&#39;s assigned profiles. | [optional] 
 **assigned_permissions** | **bool**| If true, the response returns the user&#39;s assigned permissions. | [optional] 
 **assigned_user_groups** | **bool**| If true, the response returns the user&#39;s assigned user groups. | [optional] 
 **limit** | **int**| The number of results to return. The maximum number of users to retrieve is 1000. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 
 **project_id** | **str**| Optionally, specify a project in which to make the request. If omitted, the request uses the production version. | [optional] 
 **target_tenant_id** | **str**| Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you&#39;re logged into. If omitted, the request uses the administrating tenant as the login tenant. | [optional] 

### Return type

[**AllUsersGetAPIResponseDTO**](AllUsersGetAPIResponseDTO.md)

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

# **get_application_logs_xlsx**
> bytearray get_application_logs_xlsx(start_time=start_time, end_time=end_time, tenant_code=tenant_code)

Retrieve the Application Logs

This API allows you to export the Application Logs for a tenant. The Application Logs track information about your  users and how they are using the application. Performing regular audits will help you identify potential security  issues and keep your data safe. As part of user management, download the Application Logs to monitor user activity  and logon events to ensure your users are performing authorized activities.   Administrating tenant users can export application logs for the administrating tenant and the analytic tenants  those users belong to.

### Example


```python
import visier.sdk.api.administration
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    start_time = 'start_time_example' # str | An inclusive date-time to start retrieving Application Logs from. (optional)
    end_time = 'end_time_example' # str | An exclusive date-time to stop retrieving Application Logs from. (optional)
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve Application Logs from. (optional)

    try:
        # Retrieve the Application Logs
        api_response = api_instance.get_application_logs_xlsx(start_time=start_time, end_time=end_time, tenant_code=tenant_code)
        print("The response of UsersV1Api->get_application_logs_xlsx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->get_application_logs_xlsx: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **str**| An inclusive date-time to start retrieving Application Logs from. | [optional] 
 **end_time** | **str**| An exclusive date-time to stop retrieving Application Logs from. | [optional] 
 **tenant_code** | **str**| Specify the tenant to retrieve Application Logs from. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An XLSX file. |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_security_report_xlsx**
> bytearray get_data_security_report_xlsx(user_id, tenant_code=tenant_code)

Retrieve the Data Security Report

This API allows you to export the data security report of a user. The Data Security Report provides information  about a specific user to see which populations and properties that user has access to as a result of the  permissions assigned to them.   Administrating tenant users can export the report for users in the administrating tenant and the analytic  tenants those users belong to.

### Example


```python
import visier.sdk.api.administration
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    user_id = 'user_id_example' # str | The ID of the user to retrieve the report for.
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve the Data Security Report from. (optional)

    try:
        # Retrieve the Data Security Report
        api_response = api_instance.get_data_security_report_xlsx(user_id, tenant_code=tenant_code)
        print("The response of UsersV1Api->get_data_security_report_xlsx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->get_data_security_report_xlsx: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to retrieve the report for. | 
 **tenant_code** | **str**| Specify the tenant to retrieve the Data Security Report from. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An XLSX file. |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permission_assigned_users**
> PermissionAssignedUsersDTO get_permission_assigned_users(permission_id, include_user_groups=include_user_groups, tenant_filter=tenant_filter, limit=limit, start=start, project_id=project_id, target_tenant_id=target_tenant_id)

Retrieve users that are assigned a specific permission

This API allows you to retrieve all the users that are assigned a specified permission. You must know the ID  of the permission you want to retrieve users for.   To specify the project in which to retrieve users assigned to a specific permission for the login tenant, provide  a project UUID in the `ProjectID` request header. If omitted, the request retrieves users assigned to a specific permission from production.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.permission_assigned_users_dto import PermissionAssignedUsersDTO
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    permission_id = 'permission_id_example' # str | The unique identifier of the permission you want to retrieve users for.
    include_user_groups = True # bool | If `true`, the response returns a list of all users that are assigned the permission, including users that are  assigned the permission through a user group.  If `false`, the response returns a list of the users that are directly assigned the permission. (optional)
    tenant_filter = 'tenant_filter_example' # str | Specify the tenant to retrieve the list of users from. (optional)
    limit = 56 # int | The number of results to return. The maximum number of tenants to retrieve is 100. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)
    project_id = 'project_id_example' # str | Optionally, specify a project in which to make the request. If omitted, the request uses the production version. (optional)
    target_tenant_id = 'target_tenant_id_example' # str | Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant. (optional)

    try:
        # Retrieve users that are assigned a specific permission
        api_response = api_instance.get_permission_assigned_users(permission_id, include_user_groups=include_user_groups, tenant_filter=tenant_filter, limit=limit, start=start, project_id=project_id, target_tenant_id=target_tenant_id)
        print("The response of UsersV1Api->get_permission_assigned_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->get_permission_assigned_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_id** | **str**| The unique identifier of the permission you want to retrieve users for. | 
 **include_user_groups** | **bool**| If &#x60;true&#x60;, the response returns a list of all users that are assigned the permission, including users that are  assigned the permission through a user group.  If &#x60;false&#x60;, the response returns a list of the users that are directly assigned the permission. | [optional] 
 **tenant_filter** | **str**| Specify the tenant to retrieve the list of users from. | [optional] 
 **limit** | **int**| The number of results to return. The maximum number of tenants to retrieve is 100. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 
 **project_id** | **str**| Optionally, specify a project in which to make the request. If omitted, the request uses the production version. | [optional] 
 **target_tenant_id** | **str**| Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you&#39;re logged into. If omitted, the request uses the administrating tenant as the login tenant. | [optional] 

### Return type

[**PermissionAssignedUsersDTO**](PermissionAssignedUsersDTO.md)

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

# **get_profile_assignments_xlsx**
> bytearray get_profile_assignments_xlsx(tenant_code=tenant_code)

Retrieve user profile assignments in XLSX format

This API allows you to export the profiles assigned to each user. This report details the profiles assigned to  each user and the profile validity period.   Administrating tenant users can export profile assignments for the administrating tenant and the analytic tenants  those users belong to.

### Example


```python
import visier.sdk.api.administration
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve profile assignments from. (optional)

    try:
        # Retrieve user profile assignments in XLSX format
        api_response = api_instance.get_profile_assignments_xlsx(tenant_code=tenant_code)
        print("The response of UsersV1Api->get_profile_assignments_xlsx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->get_profile_assignments_xlsx: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_code** | **str**| Specify the tenant to retrieve profile assignments from. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An XLSX file. |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_detail**
> UserGetAPIResponseDTO get_user_detail(user_id, tenant_code=tenant_code, assigned_profiles=assigned_profiles, assigned_permissions=assigned_permissions, assigned_user_groups=assigned_user_groups, project_id=project_id, target_tenant_id=target_tenant_id)

Retrieve a user's details

This API allows you to retrieve all details for a specified user.   To specify the project in which to retrieve user information, provide a project UUID in the `ProjectID` request header. If omitted, the request retrieves user information from production.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.user_get_api_response_dto import UserGetAPIResponseDTO
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    user_id = 'user_id_example' # str | The ID of the user you want to retrieve.
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve a user from. (optional)
    assigned_profiles = True # bool | If true, the response returns a list of the user's assigned profiles. (optional)
    assigned_permissions = True # bool | If true, the response returns the user's assigned permissions. (optional)
    assigned_user_groups = True # bool | If true, the response returns the user's assigned user groups. (optional)
    project_id = 'project_id_example' # str | Optionally, specify a project in which to make the request. If omitted, the request uses the production version. (optional)
    target_tenant_id = 'target_tenant_id_example' # str | Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant. (optional)

    try:
        # Retrieve a user's details
        api_response = api_instance.get_user_detail(user_id, tenant_code=tenant_code, assigned_profiles=assigned_profiles, assigned_permissions=assigned_permissions, assigned_user_groups=assigned_user_groups, project_id=project_id, target_tenant_id=target_tenant_id)
        print("The response of UsersV1Api->get_user_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->get_user_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user you want to retrieve. | 
 **tenant_code** | **str**| Specify the tenant to retrieve a user from. | [optional] 
 **assigned_profiles** | **bool**| If true, the response returns a list of the user&#39;s assigned profiles. | [optional] 
 **assigned_permissions** | **bool**| If true, the response returns the user&#39;s assigned permissions. | [optional] 
 **assigned_user_groups** | **bool**| If true, the response returns the user&#39;s assigned user groups. | [optional] 
 **project_id** | **str**| Optionally, specify a project in which to make the request. If omitted, the request uses the production version. | [optional] 
 **target_tenant_id** | **str**| Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you&#39;re logged into. If omitted, the request uses the administrating tenant as the login tenant. | [optional] 

### Return type

[**UserGetAPIResponseDTO**](UserGetAPIResponseDTO.md)

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

# **get_user_group_users**
> UserGroupsUsersDTO get_user_group_users(user_group_id, tenant_filter=tenant_filter, limit=limit, start=start, project_id=project_id, target_tenant_id=target_tenant_id)

Retrieve a list of user group users

This API allows you to retrieve the list of users explicitly assigned to a user group. Users that are implicitly  included in the user group through the user group's dynamic filters are not returned by this endpoint.   To specify the project in which to retrieve user group users for the login tenant, provide  a project UUID in the `ProjectID` request header. If omitted, the request retrieves user group users from production.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.user_groups_users_dto import UserGroupsUsersDTO
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    user_group_id = 'user_group_id_example' # str | The ID of user group.
    tenant_filter = 'tenant_filter_example' # str | Specifies the tenant to retrieve the list of users from. (optional)
    limit = 56 # int | The number of results to return. The maximum number of tenants to retrieve is 100. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)
    project_id = 'project_id_example' # str | Optionally, specify a project in which to make the request. If omitted, the request uses the production version. (optional)
    target_tenant_id = 'target_tenant_id_example' # str | Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant. (optional)

    try:
        # Retrieve a list of user group users
        api_response = api_instance.get_user_group_users(user_group_id, tenant_filter=tenant_filter, limit=limit, start=start, project_id=project_id, target_tenant_id=target_tenant_id)
        print("The response of UsersV1Api->get_user_group_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->get_user_group_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| The ID of user group. | 
 **tenant_filter** | **str**| Specifies the tenant to retrieve the list of users from. | [optional] 
 **limit** | **int**| The number of results to return. The maximum number of tenants to retrieve is 100. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 
 **project_id** | **str**| Optionally, specify a project in which to make the request. If omitted, the request uses the production version. | [optional] 
 **target_tenant_id** | **str**| Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you&#39;re logged into. If omitted, the request uses the administrating tenant as the login tenant. | [optional] 

### Return type

[**UserGroupsUsersDTO**](UserGroupsUsersDTO.md)

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

# **get_user_permissions_xlsx**
> bytearray get_user_permissions_xlsx(tenant_code=tenant_code)

Retrieve user permissions in XLSX format

This API allows you to export the user permission assignments for a tenant. The permission assignments report  provides a summary of the permissions your users have been assigned and how each permission is being used across  your user base, as well as the users that do not have any permissions assigned to them.   Administrating tenant users can export permission assignments for the administrating tenant and the analytic  tenants those users belong to.

### Example


```python
import visier.sdk.api.administration
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve the permission assignments report from. (optional)

    try:
        # Retrieve user permissions in XLSX format
        api_response = api_instance.get_user_permissions_xlsx(tenant_code=tenant_code)
        print("The response of UsersV1Api->get_user_permissions_xlsx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->get_user_permissions_xlsx: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_code** | **str**| Specify the tenant to retrieve the permission assignments report from. | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-excel, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An XLSX file. |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_permissions**
> AssignRevokePermissionsResponseDTO remove_permissions(assign_revoke_permissions_request_dto, project_id=project_id, target_tenant_id=target_tenant_id)

Remove permissions from users

This API allows you to remove a permission from specific users. Administrating tenant users can remove permissions  from users in the administrating tenant and in the analytic tenants those users belong to.   To remove permission from users in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can remove permissions from users in analytic tenants by providing a tenant code and project ID in the request body.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.assign_revoke_permissions_request_dto import AssignRevokePermissionsRequestDTO
from visier.sdk.api.administration.models.assign_revoke_permissions_response_dto import AssignRevokePermissionsResponseDTO
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    assign_revoke_permissions_request_dto = visier.sdk.api.administration.AssignRevokePermissionsRequestDTO() # AssignRevokePermissionsRequestDTO | 
    project_id = 'project_id_example' # str | Optionally, specify a project in which to make the request. If omitted, the request uses the production version. (optional)
    target_tenant_id = 'target_tenant_id_example' # str | Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant. (optional)

    try:
        # Remove permissions from users
        api_response = api_instance.remove_permissions(assign_revoke_permissions_request_dto, project_id=project_id, target_tenant_id=target_tenant_id)
        print("The response of UsersV1Api->remove_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->remove_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_revoke_permissions_request_dto** | [**AssignRevokePermissionsRequestDTO**](AssignRevokePermissionsRequestDTO.md)|  | 
 **project_id** | **str**| Optionally, specify a project in which to make the request. If omitted, the request uses the production version. | [optional] 
 **target_tenant_id** | **str**| Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you&#39;re logged into. If omitted, the request uses the administrating tenant as the login tenant. | [optional] 

### Return type

[**AssignRevokePermissionsResponseDTO**](AssignRevokePermissionsResponseDTO.md)

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

# **remove_users_from_user_group**
> SecurityAssignmentResponseDTO remove_users_from_user_group(users_to_user_groups_request_dto, project_id=project_id, target_tenant_id=target_tenant_id)

Remove users from user groups

This API allows you to remove users from specific user groups.   To remove users from user groups in a project for the administrating tenant, provide a project UUID in the `ProjectID` request header.  Administrating tenants can remove users to user groups in analytic tenants by providing a tenant code and project ID in the request body.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.security_assignment_response_dto import SecurityAssignmentResponseDTO
from visier.sdk.api.administration.models.users_to_user_groups_request_dto import UsersToUserGroupsRequestDTO
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    users_to_user_groups_request_dto = visier.sdk.api.administration.UsersToUserGroupsRequestDTO() # UsersToUserGroupsRequestDTO | 
    project_id = 'project_id_example' # str | Optionally, specify a project in which to make the request. If omitted, the request uses the production version. (optional)
    target_tenant_id = 'target_tenant_id_example' # str | Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant. (optional)

    try:
        # Remove users from user groups
        api_response = api_instance.remove_users_from_user_group(users_to_user_groups_request_dto, project_id=project_id, target_tenant_id=target_tenant_id)
        print("The response of UsersV1Api->remove_users_from_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->remove_users_from_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_to_user_groups_request_dto** | [**UsersToUserGroupsRequestDTO**](UsersToUserGroupsRequestDTO.md)|  | 
 **project_id** | **str**| Optionally, specify a project in which to make the request. If omitted, the request uses the production version. | [optional] 
 **target_tenant_id** | **str**| Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you&#39;re logged into. If omitted, the request uses the administrating tenant as the login tenant. | [optional] 

### Return type

[**SecurityAssignmentResponseDTO**](SecurityAssignmentResponseDTO.md)

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

# **revoke_permissions_from_user_groups**
> PermissionsToUserGroupForTenantDTO revoke_permissions_from_user_groups(permissions_to_user_groups_request_dto, project_id=project_id, target_tenant_id=target_tenant_id)

Remove permissions from user groups

This API allows you to remove a permission from specific user groups.   To remove permissions from user groups in a project, provide a project UUID in the `ProjectID` request header.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.permissions_to_user_group_for_tenant_dto import PermissionsToUserGroupForTenantDTO
from visier.sdk.api.administration.models.permissions_to_user_groups_request_dto import PermissionsToUserGroupsRequestDTO
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    permissions_to_user_groups_request_dto = visier.sdk.api.administration.PermissionsToUserGroupsRequestDTO() # PermissionsToUserGroupsRequestDTO | 
    project_id = 'project_id_example' # str | Optionally, specify a project in which to make the request. If omitted, the request uses the production version. (optional)
    target_tenant_id = 'target_tenant_id_example' # str | Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you're logged into. If omitted, the request uses the administrating tenant as the login tenant. (optional)

    try:
        # Remove permissions from user groups
        api_response = api_instance.revoke_permissions_from_user_groups(permissions_to_user_groups_request_dto, project_id=project_id, target_tenant_id=target_tenant_id)
        print("The response of UsersV1Api->revoke_permissions_from_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->revoke_permissions_from_user_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissions_to_user_groups_request_dto** | [**PermissionsToUserGroupsRequestDTO**](PermissionsToUserGroupsRequestDTO.md)|  | 
 **project_id** | **str**| Optionally, specify a project in which to make the request. If omitted, the request uses the production version. | [optional] 
 **target_tenant_id** | **str**| Optionally, specify the tenant that you want to execute the API call on. This defines the tenant that you&#39;re logged into. If omitted, the request uses the administrating tenant as the login tenant. | [optional] 

### Return type

[**PermissionsToUserGroupForTenantDTO**](PermissionsToUserGroupForTenantDTO.md)

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

# **update_user**
> UserUpdateAPIRequestDTO update_user(user_id, user_update_api_request_dto, tenant_code=tenant_code)

Update a user

Update an existing user's information, such as their display name or if the user is enabled in Visier.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.user_update_api_request_dto import UserUpdateAPIRequestDTO
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
    api_instance = visier.sdk.api.administration.UsersV1Api(api_client)
    user_id = 'user_id_example' # str | The ID of the user you want to update.
    user_update_api_request_dto = visier.sdk.api.administration.UserUpdateAPIRequestDTO() # UserUpdateAPIRequestDTO | 
    tenant_code = 'tenant_code_example' # str | Specify the tenant to update a user in. (optional)

    try:
        # Update a user
        api_response = api_instance.update_user(user_id, user_update_api_request_dto, tenant_code=tenant_code)
        print("The response of UsersV1Api->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user you want to update. | 
 **user_update_api_request_dto** | [**UserUpdateAPIRequestDTO**](UserUpdateAPIRequestDTO.md)|  | 
 **tenant_code** | **str**| Specify the tenant to update a user in. | [optional] 

### Return type

[**UserUpdateAPIRequestDTO**](UserUpdateAPIRequestDTO.md)

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

