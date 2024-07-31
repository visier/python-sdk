# QueryClarificationDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.query_clarification_dto import QueryClarificationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryClarificationDTO from a JSON string
query_clarification_dto_instance = QueryClarificationDTO.from_json(json)
# print the JSON string representation of the object
print(QueryClarificationDTO.to_json())

# convert the object into a dict
query_clarification_dto_dict = query_clarification_dto_instance.to_dict()
# create an instance of QueryClarificationDTO from a dict
query_clarification_dto_from_dict = QueryClarificationDTO.from_dict(query_clarification_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


