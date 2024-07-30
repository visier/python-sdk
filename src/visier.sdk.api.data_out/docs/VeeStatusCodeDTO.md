# VeeStatusCodeDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **str** |  | [optional] 
**status_msg** | **str** |  | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_status_code_dto import VeeStatusCodeDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeStatusCodeDTO from a JSON string
vee_status_code_dto_instance = VeeStatusCodeDTO.from_json(json)
# print the JSON string representation of the object
print(VeeStatusCodeDTO.to_json())

# convert the object into a dict
vee_status_code_dto_dict = vee_status_code_dto_instance.to_dict()
# create an instance of VeeStatusCodeDTO from a dict
vee_status_code_dto_from_dict = VeeStatusCodeDTO.from_dict(vee_status_code_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


