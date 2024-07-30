# JobStatusWithStartTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | The unique ID of the job. | [optional] 
**job_type** | **str** | The type of the job, such as a processing job or receiving job. | [optional] 
**start_time** | **str** | The time that the job started. | [optional] 
**status** | **str** | The status of the job, such as Running or Completed. | [optional] 
**tenant** | **str** | The tenant code. | [optional] 

## Example

```python
from visier.sdk.api.data_in.models.job_status_with_start_time import JobStatusWithStartTime

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatusWithStartTime from a JSON string
job_status_with_start_time_instance = JobStatusWithStartTime.from_json(json)
# print the JSON string representation of the object
print(JobStatusWithStartTime.to_json())

# convert the object into a dict
job_status_with_start_time_dict = job_status_with_start_time_instance.to_dict()
# create an instance of JobStatusWithStartTime from a dict
job_status_with_start_time_from_dict = JobStatusWithStartTime.from_dict(job_status_with_start_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


