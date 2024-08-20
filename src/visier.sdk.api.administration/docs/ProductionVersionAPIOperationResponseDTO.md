# ProductionVersionAPIOperationResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roll_back_to** | [**ProjectDTO**](ProjectDTO.md) | The project created by the &#x60;rollBackTo&#x60; operation. | [optional] 

## Example

```python
from visier.sdk.api.administration.models.production_version_api_operation_response_dto import ProductionVersionAPIOperationResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionVersionAPIOperationResponseDTO from a JSON string
production_version_api_operation_response_dto_instance = ProductionVersionAPIOperationResponseDTO.from_json(json)
# print the JSON string representation of the object
print(ProductionVersionAPIOperationResponseDTO.to_json())

# convert the object into a dict
production_version_api_operation_response_dto_dict = production_version_api_operation_response_dto_instance.to_dict()
# create an instance of ProductionVersionAPIOperationResponseDTO from a dict
production_version_api_operation_response_dto_from_dict = ProductionVersionAPIOperationResponseDTO.from_dict(production_version_api_operation_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


