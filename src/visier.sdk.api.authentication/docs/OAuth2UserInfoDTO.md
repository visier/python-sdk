# OAuth2UserInfoDTO

Response from OAuth 2 `userinfo` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user&#39;s email address. | [optional] 
**name** | **str** | The user&#39;s Common Name. | [optional] 
**subject** | **str** | The user&#39;s display name. | [optional] 
**visiercapabilities** | [**ServicingCapabilityProtoEnumAccessLookupDTO**](ServicingCapabilityProtoEnumAccessLookupDTO.md) | The user&#39;s profile capabilities. | [optional] 
**visierexport_subnets** | [**OAuth2UserSubnetInfoDTO**](OAuth2UserSubnetInfoDTO.md) | Subnet restrictions controlling the IP addresses from which data and metadata requests can be made. | [optional] 
**visiersubnets** | [**OAuth2UserSubnetInfoDTO**](OAuth2UserSubnetInfoDTO.md) | Subnet restrictions controlling the IP addresses from which users can access the tenant. | [optional] 
**visiertenant_details** | [**OAuth2UserTenantDetailsDTO**](OAuth2UserTenantDetailsDTO.md) | Detailed information about the analytic tenant. Included in the response if &#x60;includeTenantDetail&#x60; is &#x60;true&#x60;. | [optional] 
**visieruser_id** | **str** | The user&#39;s unique ID. | [optional] 

## Example

```python
from visier.sdk.api.authentication.models.o_auth2_user_info_dto import OAuth2UserInfoDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2UserInfoDTO from a JSON string
o_auth2_user_info_dto_instance = OAuth2UserInfoDTO.from_json(json)
# print the JSON string representation of the object
print(OAuth2UserInfoDTO.to_json())

# convert the object into a dict
o_auth2_user_info_dto_dict = o_auth2_user_info_dto_instance.to_dict()
# create an instance of OAuth2UserInfoDTO from a dict
o_auth2_user_info_dto_from_dict = OAuth2UserInfoDTO.from_dict(o_auth2_user_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


