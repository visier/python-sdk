# VeeFeedbackDTO

Query feedback DTOs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**is_approved** | **bool** |  | [optional] 
**response** | [**VeeResponseDTO**](VeeResponseDTO.md) |  | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_feedback_dto import VeeFeedbackDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeFeedbackDTO from a JSON string
vee_feedback_dto_instance = VeeFeedbackDTO.from_json(json)
# print the JSON string representation of the object
print(VeeFeedbackDTO.to_json())

# convert the object into a dict
vee_feedback_dto_dict = vee_feedback_dto_instance.to_dict()
# create an instance of VeeFeedbackDTO from a dict
vee_feedback_dto_from_dict = VeeFeedbackDTO.from_dict(vee_feedback_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


