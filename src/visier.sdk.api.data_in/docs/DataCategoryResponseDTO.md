# DataCategoryResponseDTO

The data category's UUID and display name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The UUID of the data category. | [optional] 
**name** | **str** | The display name of the data category. | [optional] 

## Example

```python
from visier.sdk.api.data_in.models.data_category_response_dto import DataCategoryResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataCategoryResponseDTO from a JSON string
data_category_response_dto_instance = DataCategoryResponseDTO.from_json(json)
# print the JSON string representation of the object
print(DataCategoryResponseDTO.to_json())

# convert the object into a dict
data_category_response_dto_dict = data_category_response_dto_instance.to_dict()
# create an instance of DataCategoryResponseDTO from a dict
data_category_response_dto_from_dict = DataCategoryResponseDTO.from_dict(data_category_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


