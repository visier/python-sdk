# SourcesAPIPutResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**SourceImportResultSummaryDTO**](SourceImportResultSummaryDTO.md) | A summary of the changes made to the sources during the PUT operation. | [optional] 

## Example

```python
from visier.sdk.api.administration.models.sources_api_put_response_dto import SourcesAPIPutResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SourcesAPIPutResponseDTO from a JSON string
sources_api_put_response_dto_instance = SourcesAPIPutResponseDTO.from_json(json)
# print the JSON string representation of the object
print(SourcesAPIPutResponseDTO.to_json())

# convert the object into a dict
sources_api_put_response_dto_dict = sources_api_put_response_dto_instance.to_dict()
# create an instance of SourcesAPIPutResponseDTO from a dict
sources_api_put_response_dto_from_dict = SourcesAPIPutResponseDTO.from_dict(sources_api_put_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


