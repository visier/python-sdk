# visier.sdk.api.administration.TenantsV2Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant**](TenantsV2Api.md#create_tenant) | **POST** /v2/admin/tenants | Add an analytic tenant
[**delete_tenant**](TenantsV2Api.md#delete_tenant) | **DELETE** /v2/admin/tenants/{tenantId} | Deprovision an analytic tenant
[**list_tenants**](TenantsV2Api.md#list_tenants) | **GET** /v2/admin/tenants | Retrieve a list of all analytic tenants
[**tenant_info**](TenantsV2Api.md#tenant_info) | **GET** /v2/admin/tenants/{tenantId} | Retrieve an analytic tenant&#39;s details
[**update_tenant**](TenantsV2Api.md#update_tenant) | **PUT** /v2/admin/tenants/{tenantId} | Update an analytic tenant


# **create_tenant**
> TenantManagementAPIUpdateResponseDTO create_tenant(tenant_management_api_update_request_dto)

Add an analytic tenant

Prior to processing and loading an analytic tenant's data files, you must provision, or create, that tenant. A  provisioned analytic tenant is automatically enabled. If the tenant's data is loaded after provisioning, that data  is immediately accessible by their users.   Create an analytic tenant and identify the  applications assigned to the tenant. Visier organizes content under a set of modules.   Contact Visier Support to determine the list of modules allocated to you.   **Note:** API requests that contain `homeAnalysisId`, `homeAnalysisByUserGroup`, `clickThroughLink`, or  `defaultCurrency` take longer to run because they require publishing a project to production.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.tenant_management_api_update_request_dto import TenantManagementAPIUpdateRequestDTO
from visier.sdk.api.administration.models.tenant_management_api_update_response_dto import TenantManagementAPIUpdateResponseDTO
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
    api_instance = visier.sdk.api.administration.TenantsV2Api(api_client)
    tenant_management_api_update_request_dto = visier.sdk.api.administration.TenantManagementAPIUpdateRequestDTO() # TenantManagementAPIUpdateRequestDTO | 

    try:
        # Add an analytic tenant
        api_response = api_instance.create_tenant(tenant_management_api_update_request_dto)
        print("The response of TenantsV2Api->create_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsV2Api->create_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_management_api_update_request_dto** | [**TenantManagementAPIUpdateRequestDTO**](TenantManagementAPIUpdateRequestDTO.md)|  | 

### Return type

[**TenantManagementAPIUpdateResponseDTO**](TenantManagementAPIUpdateResponseDTO.md)

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

# **delete_tenant**
> TenantStatusAPIDTO delete_tenant(tenant_id)

Deprovision an analytic tenant

<em>Warning! Deprovisioning an analytic tenant is not reversible.</em>  Before deprovisioning, you must disable an analytic tenant. For more information, see **`/v1/admin/tenants/{tenantId}/disable`**.   This API removes an analytic tenant permanently from the Visier system. If you are unsure whether an analytic tenant  may be re-enabled on any of the Visier modules at any time, you may instead want to disable the analytic tenant.   If successful, the response returns the status \"Deprovisioned\". This indicates that the tenant is scheduled for  deprovisioning, which may take several days to complete.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.tenant_status_apidto import TenantStatusAPIDTO
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
    api_instance = visier.sdk.api.administration.TenantsV2Api(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code.

    try:
        # Deprovision an analytic tenant
        api_response = api_instance.delete_tenant(tenant_id)
        print("The response of TenantsV2Api->delete_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsV2Api->delete_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code. | 

### Return type

[**TenantStatusAPIDTO**](TenantStatusAPIDTO.md)

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

# **list_tenants**
> TenantManagementAPIListResponseDTO list_tenants(mask_message, limit=limit, start=start)

Retrieve a list of all analytic tenants

Retrieve the full list of analytic tenants managed by you with their current states and the content  modules assigned to them, and all other relevant details for the tenants if requested.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.mask_message import MaskMessage
from visier.sdk.api.administration.models.tenant_management_api_list_response_dto import TenantManagementAPIListResponseDTO
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
    api_instance = visier.sdk.api.administration.TenantsV2Api(api_client)
    mask_message = visier.sdk.api.administration.MaskMessage() # MaskMessage | 
    limit = 56 # int | The maximum number of tenants to return. Default is 400. (optional)
    start = 56 # int | The starting index of the first tenant to return. Default is 0. (optional)

    try:
        # Retrieve a list of all analytic tenants
        api_response = api_instance.list_tenants(mask_message, limit=limit, start=start)
        print("The response of TenantsV2Api->list_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsV2Api->list_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mask_message** | [**MaskMessage**](MaskMessage.md)|  | 
 **limit** | **int**| The maximum number of tenants to return. Default is 400. | [optional] 
 **start** | **int**| The starting index of the first tenant to return. Default is 0. | [optional] 

### Return type

[**TenantManagementAPIListResponseDTO**](TenantManagementAPIListResponseDTO.md)

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

# **tenant_info**
> TenantManagementAPIGetResponseDTO tenant_info(tenant_id, mask_message)

Retrieve an analytic tenant's details

Retrieve the details for a specified analytic tenant. Doing so allows you to see the current state  of the tenant, the content modules assigned to it, and all other relevant details for the tenant.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.mask_message import MaskMessage
from visier.sdk.api.administration.models.tenant_management_api_get_response_dto import TenantManagementAPIGetResponseDTO
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
    api_instance = visier.sdk.api.administration.TenantsV2Api(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant to retrieve.
    mask_message = visier.sdk.api.administration.MaskMessage() # MaskMessage | 

    try:
        # Retrieve an analytic tenant's details
        api_response = api_instance.tenant_info(tenant_id, mask_message)
        print("The response of TenantsV2Api->tenant_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsV2Api->tenant_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant to retrieve. | 
 **mask_message** | [**MaskMessage**](MaskMessage.md)|  | 

### Return type

[**TenantManagementAPIGetResponseDTO**](TenantManagementAPIGetResponseDTO.md)

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

# **update_tenant**
> TenantManagementAPIUpdateResponseDTO update_tenant(tenant_id, tenant_management_api_update_request_dto)

Update an analytic tenant

You may need to update analytic tenants as they grow and as your organization upgrades the content available to them.  You may also encounter a scenario where an analytic tenant transitions across different industries. To make updates  to your tenants, use this API.   * To ensure that the analytic tenant receives accurate benchmarks and predictive functionality, update their industry code in the Visier system.  * To programmatically assign the Home analysis that analytic tenants see at login, use this API to set the default Home analysis for a tenant and specific user groups of that tenant.   You can use this API to update any field on an analytic tenant, except `tenantCode`.   **Note:** API requests that contain `homeAnalysisId`, `homeAnalysisByUserGroup`, `clickThroughLink`, or  `defaultCurrency` take longer to run because they require publishing a project to production.

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.tenant_management_api_update_request_dto import TenantManagementAPIUpdateRequestDTO
from visier.sdk.api.administration.models.tenant_management_api_update_response_dto import TenantManagementAPIUpdateResponseDTO
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
    api_instance = visier.sdk.api.administration.TenantsV2Api(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_management_api_update_request_dto = visier.sdk.api.administration.TenantManagementAPIUpdateRequestDTO() # TenantManagementAPIUpdateRequestDTO | 

    try:
        # Update an analytic tenant
        api_response = api_instance.update_tenant(tenant_id, tenant_management_api_update_request_dto)
        print("The response of TenantsV2Api->update_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsV2Api->update_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_management_api_update_request_dto** | [**TenantManagementAPIUpdateRequestDTO**](TenantManagementAPIUpdateRequestDTO.md)|  | 

### Return type

[**TenantManagementAPIUpdateResponseDTO**](TenantManagementAPIUpdateResponseDTO.md)

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

