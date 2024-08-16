# ConsolidatedAnalyticsJobRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_code** | **str** | The tenant code of the consolidated analytics tenant; for example, \&quot;WFF_j1r~CAa7s\&quot;. | [optional] 

## Example

```python
from visier.sdk.api.data_in.models.consolidated_analytics_job_request_dto import ConsolidatedAnalyticsJobRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ConsolidatedAnalyticsJobRequestDTO from a JSON string
consolidated_analytics_job_request_dto_instance = ConsolidatedAnalyticsJobRequestDTO.from_json(json)
# print the JSON string representation of the object
print(ConsolidatedAnalyticsJobRequestDTO.to_json())

# convert the object into a dict
consolidated_analytics_job_request_dto_dict = consolidated_analytics_job_request_dto_instance.to_dict()
# create an instance of ConsolidatedAnalyticsJobRequestDTO from a dict
consolidated_analytics_job_request_dto_from_dict = ConsolidatedAnalyticsJobRequestDTO.from_dict(consolidated_analytics_job_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


