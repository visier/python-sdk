# VeeThreadStateDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question_state** | **List[str]** |  | [optional] 

## Example

```python
from visier.sdk.api.data_out.models.vee_thread_state_dto import VeeThreadStateDTO

# TODO update the JSON string below
json = "{}"
# create an instance of VeeThreadStateDTO from a JSON string
vee_thread_state_dto_instance = VeeThreadStateDTO.from_json(json)
# print the JSON string representation of the object
print(VeeThreadStateDTO.to_json())

# convert the object into a dict
vee_thread_state_dto_dict = vee_thread_state_dto_instance.to_dict()
# create an instance of VeeThreadStateDTO from a dict
vee_thread_state_dto_from_dict = VeeThreadStateDTO.from_dict(vee_thread_state_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


