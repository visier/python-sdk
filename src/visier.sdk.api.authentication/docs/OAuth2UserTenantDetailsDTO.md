# OAuth2UserTenantDetailsDTO

The details of all accessible analytic tenants

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[OAuth2UserTenantDetailDTO]**](OAuth2UserTenantDetailDTO.md) | The details of all accessible analytic tenants. | [optional] 

## Example

```python
from visier.sdk.api.authentication.models.o_auth2_user_tenant_details_dto import OAuth2UserTenantDetailsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2UserTenantDetailsDTO from a JSON string
o_auth2_user_tenant_details_dto_instance = OAuth2UserTenantDetailsDTO.from_json(json)
# print the JSON string representation of the object
print(OAuth2UserTenantDetailsDTO.to_json())

# convert the object into a dict
o_auth2_user_tenant_details_dto_dict = o_auth2_user_tenant_details_dto_instance.to_dict()
# create an instance of OAuth2UserTenantDetailsDTO from a dict
o_auth2_user_tenant_details_dto_from_dict = OAuth2UserTenantDetailsDTO.from_dict(o_auth2_user_tenant_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


