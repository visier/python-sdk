# CapabilityGroupDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | **str** |  | [optional] 
**api_access_level** | **str** |  | [optional] 
**api_view_level** | **str** |  | [optional] 
**group** | **str** |  | [optional] 
**view_level** | **str** |  | [optional] 

## Example

```python
from visier.sdk.api.authentication.models.capability_group_dto import CapabilityGroupDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilityGroupDTO from a JSON string
capability_group_dto_instance = CapabilityGroupDTO.from_json(json)
# print the JSON string representation of the object
print(CapabilityGroupDTO.to_json())

# convert the object into a dict
capability_group_dto_dict = capability_group_dto_instance.to_dict()
# create an instance of CapabilityGroupDTO from a dict
capability_group_dto_from_dict = CapabilityGroupDTO.from_dict(capability_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


