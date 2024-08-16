# ExtractDataAndLoadDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_tenants** | **bool** | If \&quot;true\&quot;, runs an extraction job for all tenants and ignores the tenants field. | [optional] 
**batch_size_override** | **int** | The maximum amount of IDs the job can retrieve in each batch. | [optional] 
**connector_ids** | **List[str]** | The unique IDs of the connectors to run extraction jobs for. | [optional] 
**data_category_id** | **str** | The unique ID of the data category in which to generate objects. | [optional] 
**disable_artifact_generation** | **bool** | If \&quot;true\&quot;, doesn&#39;t generate objects after the extraction jobs succeeds. | [optional] 
**extract_to_time_override** | **str** | An epoch timestamp in milliseconds for the end time up to which to retrieve data. | [optional] 
**force_update_existing_artifacts** | **bool** | If \&quot;true\&quot; and &#x60;disableArtifactGeneration&#x60; is \&quot;false\&quot;, updates extractor artifacts, which may overwrite the artifacts&#39; manual overrides. Ignored if &#x60;disableArtifactGeneration&#x60; is \&quot;true\&quot;. | [optional] 
**last_extraction_time_offset_weeks** | **int** | The number of weeks from which to retrieve data. This overrides the last extraction date to retrieve more data. | [optional] 
**months_to_extract** | **int** | The number of months to retrieve snapshot data from. | [optional] 
**override_last_extraction_timestamp** | **str** | An epoch timestamp in milliseconds from which to retrieve data. This overrides the last extraction date to retrieve more data. | [optional] 
**publish_data_load_artifacts** | **bool** | If \&quot;true\&quot;, publishes the project to production. | [optional] 
**run_processing_job** | **bool** | If \&quot;true\&quot;, runs a processing job to generate a data version after the extraction job succeeds. | [optional] 
**sql_batch_size** | **int** | The maximum amount of SQL table records the job can retrieve in each batch. | [optional] 
**tenants** | **List[str]** | The unique IDs of the tenants to run an extraction job for. | [optional] 

## Example

```python
from visier.sdk.api.data_in.models.extract_data_and_load_dto import ExtractDataAndLoadDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractDataAndLoadDTO from a JSON string
extract_data_and_load_dto_instance = ExtractDataAndLoadDTO.from_json(json)
# print the JSON string representation of the object
print(ExtractDataAndLoadDTO.to_json())

# convert the object into a dict
extract_data_and_load_dto_dict = extract_data_and_load_dto_instance.to_dict()
# create an instance of ExtractDataAndLoadDTO from a dict
extract_data_and_load_dto_from_dict = ExtractDataAndLoadDTO.from_dict(extract_data_and_load_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


