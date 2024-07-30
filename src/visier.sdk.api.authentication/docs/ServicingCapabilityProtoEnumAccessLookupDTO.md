# ServicingCapabilityProtoEnumAccessLookupDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability_groups** | [**List[CapabilityGroupDTO]**](CapabilityGroupDTO.md) |  | [optional] 

## Example

```python
from visier.sdk.api.authentication.models.servicing_capability_proto_enum_access_lookup_dto import ServicingCapabilityProtoEnumAccessLookupDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ServicingCapabilityProtoEnumAccessLookupDTO from a JSON string
servicing_capability_proto_enum_access_lookup_dto_instance = ServicingCapabilityProtoEnumAccessLookupDTO.from_json(json)
# print the JSON string representation of the object
print(ServicingCapabilityProtoEnumAccessLookupDTO.to_json())

# convert the object into a dict
servicing_capability_proto_enum_access_lookup_dto_dict = servicing_capability_proto_enum_access_lookup_dto_instance.to_dict()
# create an instance of ServicingCapabilityProtoEnumAccessLookupDTO from a dict
servicing_capability_proto_enum_access_lookup_dto_from_dict = ServicingCapabilityProtoEnumAccessLookupDTO.from_dict(servicing_capability_proto_enum_access_lookup_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


