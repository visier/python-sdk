# OAuth2UserTenantPropertiesDTO

Detailed information about the tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vanity_url_name** | **str** | The tenant&#39;s vanity name. | [optional] 

## Example

```python
from visier.sdk.api.authentication.models.o_auth2_user_tenant_properties_dto import OAuth2UserTenantPropertiesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2UserTenantPropertiesDTO from a JSON string
o_auth2_user_tenant_properties_dto_instance = OAuth2UserTenantPropertiesDTO.from_json(json)
# print the JSON string representation of the object
print(OAuth2UserTenantPropertiesDTO.to_json())

# convert the object into a dict
o_auth2_user_tenant_properties_dto_dict = o_auth2_user_tenant_properties_dto_instance.to_dict()
# create an instance of OAuth2UserTenantPropertiesDTO from a dict
o_auth2_user_tenant_properties_dto_from_dict = OAuth2UserTenantPropertiesDTO.from_dict(o_auth2_user_tenant_properties_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


