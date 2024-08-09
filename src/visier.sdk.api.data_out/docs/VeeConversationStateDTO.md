# VeeConversationStateDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question_state** | **List[str]** | The unique identifier of the conversation with Vee. | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_conversation_state_dto import VeeConversationStateDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeConversationStateDTO from a JSON string
vee_conversation_state_dto_instance = VeeConversationStateDTO.from_json(json)
# print the JSON string representation of the object
print(VeeConversationStateDTO.to_json())

# convert the object into a dict
vee_conversation_state_dto_dict = vee_conversation_state_dto_instance.to_dict()
# create an instance of VeeConversationStateDTO from a dict
vee_conversation_state_dto_from_dict = VeeConversationStateDTO.from_dict(vee_conversation_state_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


