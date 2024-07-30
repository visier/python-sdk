# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1418
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.member_parameter_value_dto import MemberParameterValueDTO

class TestMemberParameterValueDTO(unittest.TestCase):
    """MemberParameterValueDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemberParameterValueDTO:
        """Test MemberParameterValueDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemberParameterValueDTO`
        """
        model = MemberParameterValueDTO()
        if include_optional:
            return MemberParameterValueDTO(
                dimension_id = '',
                parameter_id = '',
                reference_path = [
                    ''
                    ],
                values = visier.sdk.api.data_out.models.member_values_dto.MemberValuesDTO(
                    excluded = [
                        visier.sdk.api.data_out.models.dimension_member_reference_dto.DimensionMemberReferenceDTO(
                            path = [
                                ''
                                ], )
                        ], 
                    included = [
                        visier.sdk.api.data_out.models.dimension_member_reference_dto.DimensionMemberReferenceDTO()
                        ], )
            )
        else:
            return MemberParameterValueDTO(
        )
        """

    def testMemberParameterValueDTO(self):
        """Test MemberParameterValueDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
