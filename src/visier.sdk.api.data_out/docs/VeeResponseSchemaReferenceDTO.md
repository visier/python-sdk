# VeeResponseSchemaReferenceDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**paths** | **List[str]** |  | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_response_schema_reference_dto import VeeResponseSchemaReferenceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeResponseSchemaReferenceDTO from a JSON string
vee_response_schema_reference_dto_instance = VeeResponseSchemaReferenceDTO.from_json(json)
# print the JSON string representation of the object
print(VeeResponseSchemaReferenceDTO.to_json())

# convert the object into a dict
vee_response_schema_reference_dto_dict = vee_response_schema_reference_dto_instance.to_dict()
# create an instance of VeeResponseSchemaReferenceDTO from a dict
vee_response_schema_reference_dto_from_dict = VeeResponseSchemaReferenceDTO.from_dict(vee_response_schema_reference_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


