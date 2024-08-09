# VeeSampleQuestionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**VeeSampleQuestionMetadataDTO**](VeeSampleQuestionMetadataDTO.md) | Details about the sample question, such as what categories the question belongs to. | [optional] 
**question** | **str** | A question in plain language. | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_sample_question_dto import VeeSampleQuestionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeSampleQuestionDTO from a JSON string
vee_sample_question_dto_instance = VeeSampleQuestionDTO.from_json(json)
# print the JSON string representation of the object
print(VeeSampleQuestionDTO.to_json())

# convert the object into a dict
vee_sample_question_dto_dict = vee_sample_question_dto_instance.to_dict()
# create an instance of VeeSampleQuestionDTO from a dict
vee_sample_question_dto_from_dict = VeeSampleQuestionDTO.from_dict(vee_sample_question_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


