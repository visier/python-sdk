# DvExportStatus

The response structure for errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | Error classification. | [optional] 
**localized_message** | **str** | Localized error message describing the root cause of the error. | [optional] 
**message** | **str** | Not used. | [optional] 
**rci** | **str** | Optional root cause identifier. | [optional] 
**user_error** | **bool** | Indicates whether the error is a user error. | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.dv_export_status import DvExportStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DvExportStatus from a JSON string
dv_export_status_instance = DvExportStatus.from_json(json)
# print the JSON string representation of the object
print(DvExportStatus.to_json())

# convert the object into a dict
dv_export_status_dict = dv_export_status_instance.to_dict()
# create an instance of DvExportStatus from a dict
dv_export_status_from_dict = DvExportStatus.from_dict(dv_export_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


