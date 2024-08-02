# TargetProjectForTenantsListDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_project_for_tenants** | [**List[TargetProjectForTenantDTO]**](TargetProjectForTenantDTO.md) | Administrating tenants can specify the tenants and projects in which to make assignments to users. Specify one &#x60;projectId&#x60; per &#x60;tenantCode&#x60;.  If omitted, the request is immediately published to production or applied to the &#x60;ProjectID&#x60; in the request header, if available, for the administrating tenant or TargetTenantID, if available. | [optional] 

## Example

```python
from visier.sdk.api.administration.models.target_project_for_tenants_list_dto import TargetProjectForTenantsListDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TargetProjectForTenantsListDTO from a JSON string
target_project_for_tenants_list_dto_instance = TargetProjectForTenantsListDTO.from_json(json)
# print the JSON string representation of the object
print(TargetProjectForTenantsListDTO.to_json())

# convert the object into a dict
target_project_for_tenants_list_dto_dict = target_project_for_tenants_list_dto_instance.to_dict()
# create an instance of TargetProjectForTenantsListDTO from a dict
target_project_for_tenants_list_dto_from_dict = TargetProjectForTenantsListDTO.from_dict(target_project_for_tenants_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


