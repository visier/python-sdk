# VeeCorrectionsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clarifications** | [**List[VeeClarificationDTO]**](VeeClarificationDTO.md) | A list of clarifying questions if Vee needs more context to answer your question; for example, if asking about someone named Adam, Vee might clarify which Adam by asking for Adam&#39;s email address. | [optional] 
**warning** | **List[str]** | A list of warnings from Vee that accompanies an unsure answer; for example, Vee might return a close match warning if Vee finds multiple employees named Adam that relate to your question. | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_corrections_dto import VeeCorrectionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeCorrectionsDTO from a JSON string
vee_corrections_dto_instance = VeeCorrectionsDTO.from_json(json)
# print the JSON string representation of the object
print(VeeCorrectionsDTO.to_json())

# convert the object into a dict
vee_corrections_dto_dict = vee_corrections_dto_instance.to_dict()
# create an instance of VeeCorrectionsDTO from a dict
vee_corrections_dto_from_dict = VeeCorrectionsDTO.from_dict(vee_corrections_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


