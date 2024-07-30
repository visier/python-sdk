# VeeVisualDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** |  | [optional] 
**image** | **str** |  | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_visual_dto import VeeVisualDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeVisualDTO from a JSON string
vee_visual_dto_instance = VeeVisualDTO.from_json(json)
# print the JSON string representation of the object
print(VeeVisualDTO.to_json())

# convert the object into a dict
vee_visual_dto_dict = vee_visual_dto_instance.to_dict()
# create an instance of VeeVisualDTO from a dict
vee_visual_dto_from_dict = VeeVisualDTO.from_dict(vee_visual_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


