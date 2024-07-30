# UsersToUserGroupsRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_project_for_tenants_list** | [**TargetProjectForTenantsListDTO**](TargetProjectForTenantsListDTO.md) | Administrating tenants can specify the tenants and projects in which to assign users to user groups or remove users from user groups. Specify one &#x60;projectId&#x60; per &#x60;tenantCode&#x60;.  If omitted, the request is immediately published to production or applied to the ProjectID in the request header, if available, for the administrating tenant or TargetTenantID, if available. | [optional] 
**user_groups** | [**List[UsersToUserGroupRequestDTO]**](UsersToUserGroupRequestDTO.md) | A list of objects representing the user groups and users to assign or remove. | [optional] 

## Example

```python
from visier.sdk.api.administration.models.users_to_user_groups_request_dto import UsersToUserGroupsRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UsersToUserGroupsRequestDTO from a JSON string
users_to_user_groups_request_dto_instance = UsersToUserGroupsRequestDTO.from_json(json)
# print the JSON string representation of the object
print(UsersToUserGroupsRequestDTO.to_json())

# convert the object into a dict
users_to_user_groups_request_dto_dict = users_to_user_groups_request_dto_instance.to_dict()
# create an instance of UsersToUserGroupsRequestDTO from a dict
users_to_user_groups_request_dto_from_dict = UsersToUserGroupsRequestDTO.from_dict(users_to_user_groups_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


