# ServiceNowV2AuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_domain** | **str** |  | [optional] 
**auth_code** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**host_domain_name** | **str** |  | [optional] 

## Example

```python
from visier.sdk.api.data_in.models.service_now_v2_auth_params_dto import ServiceNowV2AuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceNowV2AuthParamsDTO from a JSON string
service_now_v2_auth_params_dto_instance = ServiceNowV2AuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(ServiceNowV2AuthParamsDTO.to_json())

# convert the object into a dict
service_now_v2_auth_params_dto_dict = service_now_v2_auth_params_dto_instance.to_dict()
# create an instance of ServiceNowV2AuthParamsDTO from a dict
service_now_v2_auth_params_dto_from_dict = ServiceNowV2AuthParamsDTO.from_dict(service_now_v2_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


