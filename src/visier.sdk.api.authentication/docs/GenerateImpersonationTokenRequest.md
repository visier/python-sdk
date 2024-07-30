# GenerateImpersonationTokenRequest

The details of the user to impersonate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_username** | **str** | The username of the user to impersonate. | [optional] 

## Example

```python
from visier.sdk.api.authentication.models.generate_impersonation_token_request import GenerateImpersonationTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateImpersonationTokenRequest from a JSON string
generate_impersonation_token_request_instance = GenerateImpersonationTokenRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateImpersonationTokenRequest.to_json())

# convert the object into a dict
generate_impersonation_token_request_dict = generate_impersonation_token_request_instance.to_dict()
# create an instance of GenerateImpersonationTokenRequest from a dict
generate_impersonation_token_request_from_dict = GenerateImpersonationTokenRequest.from_dict(generate_impersonation_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


