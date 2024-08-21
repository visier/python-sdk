# SourcesAPIOperationRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The operation to perform. Valid values:  * &#x60;exportSources&#x60;: Export all sources from the tenant. If successful, a ZIP file is returned containing a compressed JSON file with the sources. | [optional] 

## Example

```python
from visier.sdk.api.administration.models.sources_api_operation_request_dto import SourcesAPIOperationRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SourcesAPIOperationRequestDTO from a JSON string
sources_api_operation_request_dto_instance = SourcesAPIOperationRequestDTO.from_json(json)
# print the JSON string representation of the object
print(SourcesAPIOperationRequestDTO.to_json())

# convert the object into a dict
sources_api_operation_request_dto_dict = sources_api_operation_request_dto_instance.to_dict()
# create an instance of SourcesAPIOperationRequestDTO from a dict
sources_api_operation_request_dto_from_dict = SourcesAPIOperationRequestDTO.from_dict(sources_api_operation_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


