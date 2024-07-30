# OAuth2UserTenantDetailDTO

Tenant detail information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The tenant&#39;s display name. | [optional] 
**properties** | [**OAuth2UserTenantPropertiesDTO**](OAuth2UserTenantPropertiesDTO.md) | The tenant&#39;s properties. | [optional] 
**tenant_code** | **str** | The tenant&#39;s unique ID. | [optional] 

## Example

```python
from visier.sdk.api.authentication.models.o_auth2_user_tenant_detail_dto import OAuth2UserTenantDetailDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2UserTenantDetailDTO from a JSON string
o_auth2_user_tenant_detail_dto_instance = OAuth2UserTenantDetailDTO.from_json(json)
# print the JSON string representation of the object
print(OAuth2UserTenantDetailDTO.to_json())

# convert the object into a dict
o_auth2_user_tenant_detail_dto_dict = o_auth2_user_tenant_detail_dto_instance.to_dict()
# create an instance of OAuth2UserTenantDetailDTO from a dict
o_auth2_user_tenant_detail_dto_from_dict = OAuth2UserTenantDetailDTO.from_dict(o_auth2_user_tenant_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


