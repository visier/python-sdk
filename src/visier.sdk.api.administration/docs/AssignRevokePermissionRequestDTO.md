# AssignRevokePermissionRequestDTO

Set permission detail  permissionId with assign to userIds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_id** | **str** | The unique identifier associated with a permission. | [optional] 
**user_ids** | **List[str]** | A list of strings representing unique user IDs. | [optional] 

## Example

```python
from visier.sdk.api.administration.models.assign_revoke_permission_request_dto import AssignRevokePermissionRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AssignRevokePermissionRequestDTO from a JSON string
assign_revoke_permission_request_dto_instance = AssignRevokePermissionRequestDTO.from_json(json)
# print the JSON string representation of the object
print(AssignRevokePermissionRequestDTO.to_json())

# convert the object into a dict
assign_revoke_permission_request_dto_dict = assign_revoke_permission_request_dto_instance.to_dict()
# create an instance of AssignRevokePermissionRequestDTO from a dict
assign_revoke_permission_request_dto_from_dict = AssignRevokePermissionRequestDTO.from_dict(assign_revoke_permission_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


