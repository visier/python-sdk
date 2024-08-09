# VeeResponseDTO

Server Response DTOs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_url** | **str** |  | [optional] 
**corrections** | [**VeeQueryCorrectionsDTO**](VeeQueryCorrectionsDTO.md) |  | [optional] 
**data** | [**VeeDataDTO**](VeeDataDTO.md) |  | [optional] 
**narrative** | **str** |  | [optional] 
**reworded_question** | **str** |  | [optional] 
**var_schema** | [**VeeResponseSchemaDTO**](VeeResponseSchemaDTO.md) |  | [optional] 
**status_code** | [**VeeStatusCodeDTO**](VeeStatusCodeDTO.md) |  | [optional] 
**thread_state** | [**VeeThreadStateDTO**](VeeThreadStateDTO.md) |  | [optional] 
**visual** | [**VeeVisualDTO**](VeeVisualDTO.md) |  | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_response_dto import VeeResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeResponseDTO from a JSON string
vee_response_dto_instance = VeeResponseDTO.from_json(json)
# print the JSON string representation of the object
print(VeeResponseDTO.to_json())

# convert the object into a dict
vee_response_dto_dict = vee_response_dto_instance.to_dict()
# create an instance of VeeResponseDTO from a dict
vee_response_dto_from_dict = VeeResponseDTO.from_dict(vee_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


