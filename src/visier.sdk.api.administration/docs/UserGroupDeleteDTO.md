# UserGroupDeleteDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The project ID in which to delete the user group.  If omitted and the &#x60;ProjectID&#x60; request header is not defined, the change is published to production immediately. | [optional] 
**tenant_code** | **str** | The code of the tenant from which to delete the user group.  Omit if deleting user groups in the current tenant. | [optional] 
**user_group_id** | **str** | Unique identifier for the user group. | [optional] 

## Example

```python
from visier.sdk.api.administration.models.user_group_delete_dto import UserGroupDeleteDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupDeleteDTO from a JSON string
user_group_delete_dto_instance = UserGroupDeleteDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupDeleteDTO.to_json())

# convert the object into a dict
user_group_delete_dto_dict = user_group_delete_dto_instance.to_dict()
# create an instance of UserGroupDeleteDTO from a dict
user_group_delete_dto_from_dict = UserGroupDeleteDTO.from_dict(user_group_delete_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


