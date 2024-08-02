# visier.sdk.api.administration.ConsolidatedAnalyticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_excluded_sources**](ConsolidatedAnalyticsApi.md#add_excluded_sources) | **PATCH** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/excluded-sources | Add excluded sources to a consolidated analytics tenant
[**add_source_tenants**](ConsolidatedAnalyticsApi.md#add_source_tenants) | **PATCH** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/source-tenants | Add source tenants to a consolidated analytics tenant
[**create_tenant**](ConsolidatedAnalyticsApi.md#create_tenant) | **POST** /v1alpha/admin/consolidated-analytics/tenants | Create a consolidated analytics tenant
[**list_excluded_sources**](ConsolidatedAnalyticsApi.md#list_excluded_sources) | **GET** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/excluded-sources | Retrieve a consolidated analytics tenant&#39;s excluded sources
[**list_source_tenants**](ConsolidatedAnalyticsApi.md#list_source_tenants) | **GET** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/source-tenants | Retrieve a consolidated analytics tenant&#39;s source tenants
[**list_tenants**](ConsolidatedAnalyticsApi.md#list_tenants) | **GET** /v1alpha/admin/consolidated-analytics/tenants | Retrieve a list of all consolidated analytics tenants
[**list_tenants_with_details**](ConsolidatedAnalyticsApi.md#list_tenants_with_details) | **GET** /v1alpha/admin/consolidated-analytics/tenants-with-details | Retrieve the details of all consolidated analytics tenants
[**remove_excluded_sources**](ConsolidatedAnalyticsApi.md#remove_excluded_sources) | **DELETE** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/excluded-sources | Remove excluded sources from a consolidated analytics tenants
[**remove_source_tenants**](ConsolidatedAnalyticsApi.md#remove_source_tenants) | **DELETE** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/source-tenants | Remove source tenants from a consolidated analytics tenants
[**set_excluded_sources**](ConsolidatedAnalyticsApi.md#set_excluded_sources) | **PUT** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/excluded-sources | Set a consolidated analytics tenant&#39;s excluded sources
[**set_source_tenants**](ConsolidatedAnalyticsApi.md#set_source_tenants) | **PUT** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/source-tenants | Set a consolidated analytics tenant&#39;s source tenants


# **add_excluded_sources**
> ConsolidatedAnalyticsAPIExcludedSourceListDTO add_excluded_sources(tenant_id, excluded_sources_body)

Add excluded sources to a consolidated analytics tenant

Add excluded sources to the list of excluded sources for a consolidated analytics tenant.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.consolidated_analytics_api_excluded_source_list_dto import ConsolidatedAnalyticsAPIExcludedSourceListDTO
from visier.sdk.api.administration.models.excluded_sources_body import ExcludedSourcesBody
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
    api_instance = visier.sdk.api.administration.ConsolidatedAnalyticsApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    excluded_sources_body = visier.sdk.api.administration.ExcludedSourcesBody() # ExcludedSourcesBody | 

    try:
        # Add excluded sources to a consolidated analytics tenant
        api_response = api_instance.add_excluded_sources(tenant_id, excluded_sources_body)
        print("The response of ConsolidatedAnalyticsApi->add_excluded_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsApi->add_excluded_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 
 **excluded_sources_body** | [**ExcludedSourcesBody**](ExcludedSourcesBody.md)|  | 

### Return type

[**ConsolidatedAnalyticsAPIExcludedSourceListDTO**](ConsolidatedAnalyticsAPIExcludedSourceListDTO.md)

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

# **add_source_tenants**
> ConsolidatedAnalyticsAPISourceTenantListDTO add_source_tenants(tenant_id, tenant_code_body, limit=limit)

Add source tenants to a consolidated analytics tenant

Add source tenants to the list of source tenants for a consolidated analytics tenant.   If successful, the response returns an updated list of source tenants.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.consolidated_analytics_api_source_tenant_list_dto import ConsolidatedAnalyticsAPISourceTenantListDTO
from visier.sdk.api.administration.models.tenant_code_body import TenantCodeBody
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
    api_instance = visier.sdk.api.administration.ConsolidatedAnalyticsApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    tenant_code_body = visier.sdk.api.administration.TenantCodeBody() # TenantCodeBody | 
    limit = 56 # int | The maximum number of source tenants to return. The maximum value is 1000. Default is 400. (optional)

    try:
        # Add source tenants to a consolidated analytics tenant
        api_response = api_instance.add_source_tenants(tenant_id, tenant_code_body, limit=limit)
        print("The response of ConsolidatedAnalyticsApi->add_source_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsApi->add_source_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 
 **tenant_code_body** | [**TenantCodeBody**](TenantCodeBody.md)|  | 
 **limit** | **int**| The maximum number of source tenants to return. The maximum value is 1000. Default is 400. | [optional] 

### Return type

[**ConsolidatedAnalyticsAPISourceTenantListDTO**](ConsolidatedAnalyticsAPISourceTenantListDTO.md)

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

# **create_tenant**
> ConsolidatedAnalyticsAPITenantCreateRequestDTO create_tenant(consolidated_analytics_api_tenant_create_request_dto)

Create a consolidated analytics tenant

Create a consolidated analytics tenant.   A new CA tenant has no source tenants and no excluded sources.   **Note:** CA tenant codes must have a prefix of CA. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.consolidated_analytics_api_tenant_create_request_dto import ConsolidatedAnalyticsAPITenantCreateRequestDTO
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
    api_instance = visier.sdk.api.administration.ConsolidatedAnalyticsApi(api_client)
    consolidated_analytics_api_tenant_create_request_dto = visier.sdk.api.administration.ConsolidatedAnalyticsAPITenantCreateRequestDTO() # ConsolidatedAnalyticsAPITenantCreateRequestDTO | 

    try:
        # Create a consolidated analytics tenant
        api_response = api_instance.create_tenant(consolidated_analytics_api_tenant_create_request_dto)
        print("The response of ConsolidatedAnalyticsApi->create_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsApi->create_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consolidated_analytics_api_tenant_create_request_dto** | [**ConsolidatedAnalyticsAPITenantCreateRequestDTO**](ConsolidatedAnalyticsAPITenantCreateRequestDTO.md)|  | 

### Return type

[**ConsolidatedAnalyticsAPITenantCreateRequestDTO**](ConsolidatedAnalyticsAPITenantCreateRequestDTO.md)

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

# **list_excluded_sources**
> ConsolidatedAnalyticsAPIExcludedSourceListDTO list_excluded_sources(tenant_id)

Retrieve a consolidated analytics tenant's excluded sources

Retrieve a CA tenant's excluded sources.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.consolidated_analytics_api_excluded_source_list_dto import ConsolidatedAnalyticsAPIExcludedSourceListDTO
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
    api_instance = visier.sdk.api.administration.ConsolidatedAnalyticsApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.

    try:
        # Retrieve a consolidated analytics tenant's excluded sources
        api_response = api_instance.list_excluded_sources(tenant_id)
        print("The response of ConsolidatedAnalyticsApi->list_excluded_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsApi->list_excluded_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 

### Return type

[**ConsolidatedAnalyticsAPIExcludedSourceListDTO**](ConsolidatedAnalyticsAPIExcludedSourceListDTO.md)

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

# **list_source_tenants**
> ConsolidatedAnalyticsAPISourceTenantListDTO list_source_tenants(tenant_id, limit=limit, start=start)

Retrieve a consolidated analytics tenant's source tenants

Retrieve a CA tenant's source tenants.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.consolidated_analytics_api_source_tenant_list_dto import ConsolidatedAnalyticsAPISourceTenantListDTO
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
    api_instance = visier.sdk.api.administration.ConsolidatedAnalyticsApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    limit = 56 # int | The maximum number of source tenants to return. The maximum value is 1000. Default is 400. (optional)
    start = 56 # int | The starting index of the first source tenant to return. Default is 0. (optional)

    try:
        # Retrieve a consolidated analytics tenant's source tenants
        api_response = api_instance.list_source_tenants(tenant_id, limit=limit, start=start)
        print("The response of ConsolidatedAnalyticsApi->list_source_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsApi->list_source_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 
 **limit** | **int**| The maximum number of source tenants to return. The maximum value is 1000. Default is 400. | [optional] 
 **start** | **int**| The starting index of the first source tenant to return. Default is 0. | [optional] 

### Return type

[**ConsolidatedAnalyticsAPISourceTenantListDTO**](ConsolidatedAnalyticsAPISourceTenantListDTO.md)

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
> ConsolidatedAnalyticsAPITenantListResponseDTO list_tenants(limit=limit, start=start)

Retrieve a list of all consolidated analytics tenants

Retrieve the full list of consolidated analytics tenants in your administrating tenant.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.consolidated_analytics_api_tenant_list_response_dto import ConsolidatedAnalyticsAPITenantListResponseDTO
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
    api_instance = visier.sdk.api.administration.ConsolidatedAnalyticsApi(api_client)
    limit = 56 # int | The maximum number of tenants to return. The maximum value is 1000. Default is 400. (optional)
    start = 56 # int | The starting index of the first tenant to return. Default is 0. (optional)

    try:
        # Retrieve a list of all consolidated analytics tenants
        api_response = api_instance.list_tenants(limit=limit, start=start)
        print("The response of ConsolidatedAnalyticsApi->list_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsApi->list_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of tenants to return. The maximum value is 1000. Default is 400. | [optional] 
 **start** | **int**| The starting index of the first tenant to return. Default is 0. | [optional] 

### Return type

[**ConsolidatedAnalyticsAPITenantListResponseDTO**](ConsolidatedAnalyticsAPITenantListResponseDTO.md)

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

# **list_tenants_with_details**
> ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO list_tenants_with_details(limit=limit, start=start)

Retrieve the details of all consolidated analytics tenants

Retrieve the full list of consolidated analytics tenants and their details in your administrating tenant.   **Note:** If your consolidated analytics tenants have thousands of source tenants, we recommend that you use the `GET /admin/consolidated-analytics/tenants` endpoint to get all CA tenants and then use the `GET /admin/consolidated-analytics/tenants/{tenantId}/source-tenants` and `GET /admin/consolidated-analytics/tenants/{tenantId}/excluded-sources` endpoints to retrieve information about specific CA tenants.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.consolidated_analytics_api_tenant_with_details_list_response_dto import ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO
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
    api_instance = visier.sdk.api.administration.ConsolidatedAnalyticsApi(api_client)
    limit = 56 # int | The maximum number of tenants to return. The maximum value is 1000. Default is 400. (optional)
    start = 56 # int | The starting index of the first tenant to return. Default is 0. (optional)

    try:
        # Retrieve the details of all consolidated analytics tenants
        api_response = api_instance.list_tenants_with_details(limit=limit, start=start)
        print("The response of ConsolidatedAnalyticsApi->list_tenants_with_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsApi->list_tenants_with_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of tenants to return. The maximum value is 1000. Default is 400. | [optional] 
 **start** | **int**| The starting index of the first tenant to return. Default is 0. | [optional] 

### Return type

[**ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO**](ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO.md)

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

# **remove_excluded_sources**
> ConsolidatedAnalyticsAPIExcludedSourceListDTO remove_excluded_sources(tenant_id, excluded_sources_body)

Remove excluded sources from a consolidated analytics tenants

Remove excluded sources from the list of excluded sources for a consolidated analytics tenant.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.consolidated_analytics_api_excluded_source_list_dto import ConsolidatedAnalyticsAPIExcludedSourceListDTO
from visier.sdk.api.administration.models.excluded_sources_body import ExcludedSourcesBody
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
    api_instance = visier.sdk.api.administration.ConsolidatedAnalyticsApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    excluded_sources_body = visier.sdk.api.administration.ExcludedSourcesBody() # ExcludedSourcesBody | 

    try:
        # Remove excluded sources from a consolidated analytics tenants
        api_response = api_instance.remove_excluded_sources(tenant_id, excluded_sources_body)
        print("The response of ConsolidatedAnalyticsApi->remove_excluded_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsApi->remove_excluded_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 
 **excluded_sources_body** | [**ExcludedSourcesBody**](ExcludedSourcesBody.md)|  | 

### Return type

[**ConsolidatedAnalyticsAPIExcludedSourceListDTO**](ConsolidatedAnalyticsAPIExcludedSourceListDTO.md)

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

# **remove_source_tenants**
> ConsolidatedAnalyticsAPISourceTenantListDTO remove_source_tenants(tenant_id, tenant_code_body, limit=limit)

Remove source tenants from a consolidated analytics tenants

Remove source tenants from the list of source tenants for a consolidated analytics tenant.   If successful, the response returns an updated list of source tenants.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.consolidated_analytics_api_source_tenant_list_dto import ConsolidatedAnalyticsAPISourceTenantListDTO
from visier.sdk.api.administration.models.tenant_code_body import TenantCodeBody
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
    api_instance = visier.sdk.api.administration.ConsolidatedAnalyticsApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    tenant_code_body = visier.sdk.api.administration.TenantCodeBody() # TenantCodeBody | 
    limit = 56 # int | The maximum number of source tenants to return. The maximum value is 1000. Default is 400. (optional)

    try:
        # Remove source tenants from a consolidated analytics tenants
        api_response = api_instance.remove_source_tenants(tenant_id, tenant_code_body, limit=limit)
        print("The response of ConsolidatedAnalyticsApi->remove_source_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsApi->remove_source_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 
 **tenant_code_body** | [**TenantCodeBody**](TenantCodeBody.md)|  | 
 **limit** | **int**| The maximum number of source tenants to return. The maximum value is 1000. Default is 400. | [optional] 

### Return type

[**ConsolidatedAnalyticsAPISourceTenantListDTO**](ConsolidatedAnalyticsAPISourceTenantListDTO.md)

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

# **set_excluded_sources**
> ConsolidatedAnalyticsAPIExcludedSourceListDTO set_excluded_sources(tenant_id, excluded_sources_body)

Set a consolidated analytics tenant's excluded sources

Define the excluded sources for a consolidated analytics tenant.   After you create a CA tenant, you may optionally define a list of excluded sources. The excluded sources are the sources whose data is excluded from the CA tenant.  You can also use this API to replace the list of excluded sources for an existing CA tenant.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.consolidated_analytics_api_excluded_source_list_dto import ConsolidatedAnalyticsAPIExcludedSourceListDTO
from visier.sdk.api.administration.models.excluded_sources_body import ExcludedSourcesBody
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
    api_instance = visier.sdk.api.administration.ConsolidatedAnalyticsApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    excluded_sources_body = visier.sdk.api.administration.ExcludedSourcesBody() # ExcludedSourcesBody | 

    try:
        # Set a consolidated analytics tenant's excluded sources
        api_response = api_instance.set_excluded_sources(tenant_id, excluded_sources_body)
        print("The response of ConsolidatedAnalyticsApi->set_excluded_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsApi->set_excluded_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 
 **excluded_sources_body** | [**ExcludedSourcesBody**](ExcludedSourcesBody.md)|  | 

### Return type

[**ConsolidatedAnalyticsAPIExcludedSourceListDTO**](ConsolidatedAnalyticsAPIExcludedSourceListDTO.md)

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

# **set_source_tenants**
> ConsolidatedAnalyticsAPISourceTenantListDTO set_source_tenants(tenant_id, tenant_code_body, limit=limit)

Set a consolidated analytics tenant's source tenants

Define the source tenants for a consolidated analytics tenant.   After you create a CA tenant, you must define a list of its source tenants. The source tenants are the tenants whose data is aggregated in the CA tenant.  You can also use this API to replace the list of source tenants for an existing CA tenant.   If successful, the response returns an updated list of source tenants.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.sdk.api.administration
from visier.sdk.api.administration.models.consolidated_analytics_api_source_tenant_list_dto import ConsolidatedAnalyticsAPISourceTenantListDTO
from visier.sdk.api.administration.models.tenant_code_body import TenantCodeBody
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
    api_instance = visier.sdk.api.administration.ConsolidatedAnalyticsApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    tenant_code_body = visier.sdk.api.administration.TenantCodeBody() # TenantCodeBody | 
    limit = 56 # int | The maximum number of source tenants to return. The maximum value is 1000. Default is 400. (optional)

    try:
        # Set a consolidated analytics tenant's source tenants
        api_response = api_instance.set_source_tenants(tenant_id, tenant_code_body, limit=limit)
        print("The response of ConsolidatedAnalyticsApi->set_source_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsApi->set_source_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 
 **tenant_code_body** | [**TenantCodeBody**](TenantCodeBody.md)|  | 
 **limit** | **int**| The maximum number of source tenants to return. The maximum value is 1000. Default is 400. | [optional] 

### Return type

[**ConsolidatedAnalyticsAPISourceTenantListDTO**](ConsolidatedAnalyticsAPISourceTenantListDTO.md)

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

