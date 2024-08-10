# VeeSampleQuestionLibraryDTO

A list of sample questions to ask Vee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**questions** | [**List[VeeSampleQuestionDTO]**](VeeSampleQuestionDTO.md) | A list of sample questions to help your users start using Vee. | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_sample_question_library_dto import VeeSampleQuestionLibraryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeSampleQuestionLibraryDTO from a JSON string
vee_sample_question_library_dto_instance = VeeSampleQuestionLibraryDTO.from_json(json)
# print the JSON string representation of the object
print(VeeSampleQuestionLibraryDTO.to_json())

# convert the object into a dict
vee_sample_question_library_dto_dict = vee_sample_question_library_dto_instance.to_dict()
# create an instance of VeeSampleQuestionLibraryDTO from a dict
vee_sample_question_library_dto_from_dict = VeeSampleQuestionLibraryDTO.from_dict(vee_sample_question_library_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


