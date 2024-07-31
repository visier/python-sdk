# JobStatusListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_status** | [**List[JobStatusWithStartTime]**](JobStatusWithStartTime.md) | The specific status to restrict the list of jobs to. | [optional] 
**query_end_time** | **str** | The end time from which to retrieve job statuses. | [optional] 
**query_start_time** | **str** | The start time from which to retrieve job statuses. | [optional] 

## Example

```python
from visier.sdk.api.data_in.models.job_status_list_response import JobStatusListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatusListResponse from a JSON string
job_status_list_response_instance = JobStatusListResponse.from_json(json)
# print the JSON string representation of the object
print(JobStatusListResponse.to_json())

# convert the object into a dict
job_status_list_response_dict = job_status_list_response_instance.to_dict()
# create an instance of JobStatusListResponse from a dict
job_status_list_response_from_dict = JobStatusListResponse.from_dict(job_status_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


