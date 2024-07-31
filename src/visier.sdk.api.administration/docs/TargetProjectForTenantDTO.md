# TargetProjectForTenantDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The project in which to make changes for the tenant. | [optional] 
**tenant_code** | **str** | The tenant code. | [optional] 

## Example

```python
from visier.sdk.api.administration.models.target_project_for_tenant_dto import TargetProjectForTenantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TargetProjectForTenantDTO from a JSON string
target_project_for_tenant_dto_instance = TargetProjectForTenantDTO.from_json(json)
# print the JSON string representation of the object
print(TargetProjectForTenantDTO.to_json())

# convert the object into a dict
target_project_for_tenant_dto_dict = target_project_for_tenant_dto_instance.to_dict()
# create an instance of TargetProjectForTenantDTO from a dict
target_project_for_tenant_dto_from_dict = TargetProjectForTenantDTO.from_dict(target_project_for_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


