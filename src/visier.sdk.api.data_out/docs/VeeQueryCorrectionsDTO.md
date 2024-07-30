# VeeQueryCorrectionsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clarifications** | [**List[QueryClarificationDTO]**](QueryClarificationDTO.md) |  | [optional] 
**warning** | **List[str]** |  | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_query_corrections_dto import VeeQueryCorrectionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeQueryCorrectionsDTO from a JSON string
vee_query_corrections_dto_instance = VeeQueryCorrectionsDTO.from_json(json)
# print the JSON string representation of the object
print(VeeQueryCorrectionsDTO.to_json())

# convert the object into a dict
vee_query_corrections_dto_dict = vee_query_corrections_dto_instance.to_dict()
# create an instance of VeeQueryCorrectionsDTO from a dict
vee_query_corrections_dto_from_dict = VeeQueryCorrectionsDTO.from_dict(vee_query_corrections_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


