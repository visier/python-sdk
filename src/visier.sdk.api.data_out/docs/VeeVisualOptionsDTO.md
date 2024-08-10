# VeeVisualOptionsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** | The pixel height of the rendered visualization. Default is 338. Valid values are between 90 and 900. | [optional] 
**width** | **int** | The pixel width of the rendered visualization. Default is 600. Valid values are between 160 and 1600. | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_visual_options_dto import VeeVisualOptionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeVisualOptionsDTO from a JSON string
vee_visual_options_dto_instance = VeeVisualOptionsDTO.from_json(json)
# print the JSON string representation of the object
print(VeeVisualOptionsDTO.to_json())

# convert the object into a dict
vee_visual_options_dto_dict = vee_visual_options_dto_instance.to_dict()
# create an instance of VeeVisualOptionsDTO from a dict
vee_visual_options_dto_from_dict = VeeVisualOptionsDTO.from_dict(vee_visual_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


