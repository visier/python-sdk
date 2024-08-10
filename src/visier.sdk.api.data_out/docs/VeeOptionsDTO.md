# VeeOptionsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_format** | **str** | The format to return visualization data in. Valid values: &#x60;json&#x60;. | [optional] 
**include_data** | **bool** | If &#x60;true&#x60;, returns additional data relevant to the question, including &#x60;dataJson&#x60; (visualization data) and &#x60;context&#x60; (filters applied to the visualization). Default is &#x60;false&#x60;. | [optional] 
**include_reworded_question** | **bool** | If &#x60;true&#x60;, returns Vee&#39;s plain language interpretation of the original question. For example, if you asked \&quot;what is the headcount by gender in each org?\&quot;, Vee might reword the question as \&quot;What is the gender breakdown of our workforce by organization this month?\&quot;. Default is &#x60;false&#x60;. | [optional] 
**include_visual** | **bool** | If &#x60;true&#x60;, returns a base64 string-encoded PNG of a rendered visualization with Vee&#39;s answer. Default is &#x60;false&#x60;. | [optional] 
**visual_options** | [**VeeVisualOptionsDTO**](VeeVisualOptionsDTO.md) | Specify how to render the visualization. | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_options_dto import VeeOptionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeOptionsDTO from a JSON string
vee_options_dto_instance = VeeOptionsDTO.from_json(json)
# print the JSON string representation of the object
print(VeeOptionsDTO.to_json())

# convert the object into a dict
vee_options_dto_dict = vee_options_dto_instance.to_dict()
# create an instance of VeeOptionsDTO from a dict
vee_options_dto_from_dict = VeeOptionsDTO.from_dict(vee_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


