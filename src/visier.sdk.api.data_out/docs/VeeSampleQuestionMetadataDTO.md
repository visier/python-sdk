# VeeSampleQuestionMetadataDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | A list of topics that the sample question relates to. | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_sample_question_metadata_dto import VeeSampleQuestionMetadataDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeSampleQuestionMetadataDTO from a JSON string
vee_sample_question_metadata_dto_instance = VeeSampleQuestionMetadataDTO.from_json(json)
# print the JSON string representation of the object
print(VeeSampleQuestionMetadataDTO.to_json())

# convert the object into a dict
vee_sample_question_metadata_dto_dict = vee_sample_question_metadata_dto_instance.to_dict()
# create an instance of VeeSampleQuestionMetadataDTO from a dict
vee_sample_question_metadata_dto_from_dict = VeeSampleQuestionMetadataDTO.from_dict(vee_sample_question_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


