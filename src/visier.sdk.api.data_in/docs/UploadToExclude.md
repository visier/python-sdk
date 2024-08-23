# UploadToExclude


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_all** | **bool** | If &#x60;true&#x60;, all data uploads are excluded for the analytic tenant. | [optional] 
**max_upload_time** | **str** | An ISO8601 time such as &#x60;\&quot;2001-10-25T13:45:35.999\&quot;&#x60; for the latest upload time. If defined, omit &#x60;uploadTimes&#x60;. If omitted and &#x60;minUploadTime&#x60; is defined, excludes files up to latest time available. | [optional] 
**min_upload_time** | **str** | An ISO8601 time such as &#x60;\&quot;2001-10-25T13:45:35.999\&quot;&#x60; for the earliest upload time. If defined, omit &#x60;uploadTimes&#x60;. If omitted and &#x60;maxUploadTime&#x60; is defined, excludes files up to earliest time available. | [optional] 
**sources** | **List[str]** | A comma-separated list of strings representing the object name of each source to exclude. If &#x60;uploadTimes&#x60; is omitted, excludes files for the given sources for all &#x60;uploadTimes&#x60;. | [optional] 
**tenant_code** | **str** | The tenant code of the analytic tenant you are excluding a data upload for. | [optional] 
**upload_times** | **List[str]** | A comma-separated list of ISO8601 time strings such as &#x60;\&quot;2001-10-25T13:45:35.999\&quot;&#x60; representing the upload time of each data upload to exclude. | [optional] 

## Example

```python
from visier.sdk.api.data_in.models.upload_to_exclude import UploadToExclude

# TODO update the JSON string below
json = "{}"
# create an instance of UploadToExclude from a JSON string
upload_to_exclude_instance = UploadToExclude.from_json(json)
# print the JSON string representation of the object
print(UploadToExclude.to_json())

# convert the object into a dict
upload_to_exclude_dict = upload_to_exclude_instance.to_dict()
# create an instance of UploadToExclude from a dict
upload_to_exclude_from_dict = UploadToExclude.from_dict(upload_to_exclude_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


