# VeeClarificationDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | If Vee needs more context to answer your question, the follow-up question should address this clarification. | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_clarification_dto import VeeClarificationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeClarificationDTO from a JSON string
vee_clarification_dto_instance = VeeClarificationDTO.from_json(json)
# print the JSON string representation of the object
print(VeeClarificationDTO.to_json())

# convert the object into a dict
vee_clarification_dto_dict = vee_clarification_dto_instance.to_dict()
# create an instance of VeeClarificationDTO from a dict
vee_clarification_dto_from_dict = VeeClarificationDTO.from_dict(vee_clarification_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


