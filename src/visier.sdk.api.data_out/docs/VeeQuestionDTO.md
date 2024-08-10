# VeeQuestionDTO

The request body fields to ask Vee a question.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_state** | [**VeeConversationStateDTO**](VeeConversationStateDTO.md) | The unique identifier of the conversation with Vee. If empty, starts a new conversation with Vee. If asking a follow-up question or continuing a conversation with Vee, specify the &#x60;conversationState&#x60; object from the question&#39;s response. To submit feedback about Vee&#39;s answer, copy the entire response into your &#x60;/feedback&#x60; call. | [optional] 
**options** | [**VeeOptionsDTO**](VeeOptionsDTO.md) | Options to specify how Vee should respond to a question. | [optional] 
**question** | **str** | The question to ask Vee. If asking a follow-up question or continuing a conversation with Vee, specify the &#x60;conversationState&#x60; object from the question&#39;s response. | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_question_dto import VeeQuestionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeQuestionDTO from a JSON string
vee_question_dto_instance = VeeQuestionDTO.from_json(json)
# print the JSON string representation of the object
print(VeeQuestionDTO.to_json())

# convert the object into a dict
vee_question_dto_dict = vee_question_dto_instance.to_dict()
# create an instance of VeeQuestionDTO from a dict
vee_question_dto_from_dict = VeeQuestionDTO.from_dict(vee_question_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


