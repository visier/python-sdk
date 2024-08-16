# ProcessingJobRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_tenants** | **bool** | If &#x60;true&#x60;, runs processing jobs for all accessible analytic tenants. Default is &#x60;false&#x60;. | [optional] 
**data_category_id** | **str** | The unique identifier of the data category to run the job. If omitted, runs a job using the primary data category.  To retrieve a list of all data categories, see &#x60;GET /v1/op/data/categories&#x60;. | [optional] 
**publish_to_production** | **bool** | If &#x60;true&#x60;, publishes the generated data version to production. Default is &#x60;false&#x60;. | [optional] 
**tenants** | **List[str]** | The tenant codes of the tenants to run processing jobs for. If omitted, runs a processing job for the tenant associated with the user who made the API request. | [optional] 

## Example

```python
from visier.sdk.api.data_in.models.processing_job_request_dto import ProcessingJobRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingJobRequestDTO from a JSON string
processing_job_request_dto_instance = ProcessingJobRequestDTO.from_json(json)
# print the JSON string representation of the object
print(ProcessingJobRequestDTO.to_json())

# convert the object into a dict
processing_job_request_dto_dict = processing_job_request_dto_instance.to_dict()
# create an instance of ProcessingJobRequestDTO from a dict
processing_job_request_dto_from_dict = ProcessingJobRequestDTO.from_dict(processing_job_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


