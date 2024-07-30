# OAuth2UserSubnetInfoDTO

Subnet access details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | The type of subnet access granted to the user. Possible values are:  * &#x60;Unknown&#x60;: Could not determine subnet access details.  * &#x60;All&#39;: No subnet restrictions.  * &#x60;Restricted&#x60;: Access is only granted to requests originating from the specified &#x60;subnets&#x60;.  * &#x60;None&#x60;: Access is denied. Only applicable to the Data Export API. | [optional] 
**subnets** | **List[str]** | The list of trusted IP addresses from which access is granted if accessType is &#x60;Restricted&#x60;. Must be in Classless Inter-Domain Routing (CIDR) format: &#x60;xxx.xxx.xxx.xxx/xx&#x60;. | [optional] 

## Example

```python
from visier.sdk.api.authentication.models.o_auth2_user_subnet_info_dto import OAuth2UserSubnetInfoDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2UserSubnetInfoDTO from a JSON string
o_auth2_user_subnet_info_dto_instance = OAuth2UserSubnetInfoDTO.from_json(json)
# print the JSON string representation of the object
print(OAuth2UserSubnetInfoDTO.to_json())

# convert the object into a dict
o_auth2_user_subnet_info_dto_dict = o_auth2_user_subnet_info_dto_instance.to_dict()
# create an instance of OAuth2UserSubnetInfoDTO from a dict
o_auth2_user_subnet_info_dto_from_dict = OAuth2UserSubnetInfoDTO.from_dict(o_auth2_user_subnet_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


