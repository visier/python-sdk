# coding: utf-8

"""
    Visier Authentication APIs

    Visier APIs for authenticating with Visier. To use Visier's public APIs, you must first authenticate yourself as a Visier user who is allowed to use Visier APIs.

    The version of the OpenAPI document: 22222222.99201.1418
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.authentication.models.servicing_capability_proto_enum_access_lookup_dto import ServicingCapabilityProtoEnumAccessLookupDTO

class TestServicingCapabilityProtoEnumAccessLookupDTO(unittest.TestCase):
    """ServicingCapabilityProtoEnumAccessLookupDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingCapabilityProtoEnumAccessLookupDTO:
        """Test ServicingCapabilityProtoEnumAccessLookupDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServicingCapabilityProtoEnumAccessLookupDTO`
        """
        model = ServicingCapabilityProtoEnumAccessLookupDTO()
        if include_optional:
            return ServicingCapabilityProtoEnumAccessLookupDTO(
                capability_groups = [
                    visier.sdk.api.authentication.models.capability_group_dto.CapabilityGroupDTO(
                        access_level = 'NoAccess', 
                        api_access_level = 'NoAccess', 
                        api_view_level = 'Simple', 
                        group = 'unknown', 
                        view_level = 'Simple', )
                    ]
            )
        else:
            return ServicingCapabilityProtoEnumAccessLookupDTO(
        )
        """

    def testServicingCapabilityProtoEnumAccessLookupDTO(self):
        """Test ServicingCapabilityProtoEnumAccessLookupDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
