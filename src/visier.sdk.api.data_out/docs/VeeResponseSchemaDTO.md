# VeeResponseSchemaDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concepts** | [**List[VeeResponseSchemaReferenceDTO]**](VeeResponseSchemaReferenceDTO.md) |  | [optional] 
**dimensions** | [**List[VeeResponseSchemaReferenceDTO]**](VeeResponseSchemaReferenceDTO.md) |  | [optional] 
**metrics** | **List[str]** |  | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_response_schema_dto import VeeResponseSchemaDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeResponseSchemaDTO from a JSON string
vee_response_schema_dto_instance = VeeResponseSchemaDTO.from_json(json)
# print the JSON string representation of the object
print(VeeResponseSchemaDTO.to_json())

# convert the object into a dict
vee_response_schema_dto_dict = vee_response_schema_dto_instance.to_dict()
# create an instance of VeeResponseSchemaDTO from a dict
vee_response_schema_dto_from_dict = VeeResponseSchemaDTO.from_dict(vee_response_schema_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


