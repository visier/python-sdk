# VeeFeedbackDTO

The request body fields to submit Vee feedback.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of how Vee should have answered the question or how Vee can improve the answer; for example, \&quot;Expected Headcount metric, but Vee returned Average Headcount\&quot;. | [optional] 
**is_approved** | **bool** | If &#x60;true&#x60;, Vee answered the question correctly. If &#x60;false&#x60;, Vee&#39;s answer was incorrect or lacked details. | [optional] 
**response** | [**VeeResponseDTO**](VeeResponseDTO.md) | Your feedback about Vee&#39;s answer. Include the response object from the &#x60;/question&#x60; call that you want to provide feedback about. | [optional] 

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


