# UploadToInclude


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_all** | **bool** | If &#x60;true&#x60;, all data uploads are included for the analytic tenant. | [optional] 
**max_upload_time** | **str** | An ISO8601 time for the latest upload time. If defined, omit &#x60;uploadTimes&#x60;. If omitted and &#x60;minUploadTime&#x60; is defined, includes files up to latest time available. | [optional] 
**min_upload_time** | **str** | An ISO8601 time for the earliest upload time. If defined, omit &#x60;uploadTimes&#x60;. If omitted and &#x60;maxUploadTime&#x60; is defined, includes files up to earliest time available. | [optional] 
**sources** | **List[str]** | A comma-separated list of strings representing the object name of each source to include. If &#x60;uploadTimes&#x60; is omitted, includes files for the given sources for all &#x60;uploadTimes&#x60;. | [optional] 
**tenant_code** | **str** | The tenant code of the analytic tenant you are including a data upload for. | [optional] 
**upload_times** | **List[str]** | A comma-separated list of ISO8601 time strings representing the upload time of each data upload to include. | [optional] 

## Example

```python
from visier.sdk.api.data_in.models.upload_to_include import UploadToInclude

# TODO update the JSON string below
json = "{}"
# create an instance of UploadToInclude from a JSON string
upload_to_include_instance = UploadToInclude.from_json(json)
# print the JSON string representation of the object
print(UploadToInclude.to_json())

# convert the object into a dict
upload_to_include_dict = upload_to_include_instance.to_dict()
# create an instance of UploadToInclude from a dict
upload_to_include_from_dict = UploadToInclude.from_dict(upload_to_include_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


