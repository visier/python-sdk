# VeeDataDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** |  | [optional] 
**data_json** | **str** |  | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_data_dto import VeeDataDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeDataDTO from a JSON string
vee_data_dto_instance = VeeDataDTO.from_json(json)
# print the JSON string representation of the object
print(VeeDataDTO.to_json())

# convert the object into a dict
vee_data_dto_dict = vee_data_dto_instance.to_dict()
# create an instance of VeeDataDTO from a dict
vee_data_dto_from_dict = VeeDataDTO.from_dict(vee_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


