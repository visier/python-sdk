# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.analytic_model.models.member_parameter_definition_dto import MemberParameterDefinitionDTO

class TestMemberParameterDefinitionDTO(unittest.TestCase):
    """MemberParameterDefinitionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemberParameterDefinitionDTO:
        """Test MemberParameterDefinitionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemberParameterDefinitionDTO`
        """
        model = MemberParameterDefinitionDTO()
        if include_optional:
            return MemberParameterDefinitionDTO(
                id = '',
                display_name = '',
                description = '',
                dimension_id = '',
                reference_path = [
                    ''
                    ],
                default = visier.sdk.api.analytic_model.models.member_values_dto.MemberValuesDTO(
                    included = [
                        visier.sdk.api.analytic_model.models.dimension_member_reference_dto.DimensionMemberReferenceDTO(
                            path = [
                                ''
                                ], )
                        ], 
                    excluded = [
                        visier.sdk.api.analytic_model.models.dimension_member_reference_dto.DimensionMemberReferenceDTO()
                        ], )
            )
        else:
            return MemberParameterDefinitionDTO(
        )
        """

    def testMemberParameterDefinitionDTO(self):
        """Test MemberParameterDefinitionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
