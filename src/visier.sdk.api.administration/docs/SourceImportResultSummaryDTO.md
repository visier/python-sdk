# SourceImportResultSummaryDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** | The number of imported sources that were newly created in the target tenant. | [optional] 
**deleted** | **int** | The number of imported sources that existed in the target tenant prior to the import, and were deleted during the import. | [optional] 
**ignored** | **int** | The number of imported sources that already existed and were ignored in the target tenant. | [optional] 
**updated** | **int** | The number of imported sources that already existed and were updated in the target tenant. | [optional] 

## Example

```python
from visier.sdk.api.administration.models.source_import_result_summary_dto import SourceImportResultSummaryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SourceImportResultSummaryDTO from a JSON string
source_import_result_summary_dto_instance = SourceImportResultSummaryDTO.from_json(json)
# print the JSON string representation of the object
print(SourceImportResultSummaryDTO.to_json())

# convert the object into a dict
source_import_result_summary_dto_dict = source_import_result_summary_dto_instance.to_dict()
# create an instance of SourceImportResultSummaryDTO from a dict
source_import_result_summary_dto_from_dict = SourceImportResultSummaryDTO.from_dict(source_import_result_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


