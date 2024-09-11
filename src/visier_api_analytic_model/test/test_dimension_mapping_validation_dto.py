# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.99201.1475
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.dimension_mapping_validation_dto import DimensionMappingValidationDTO

class TestDimensionMappingValidationDTO(unittest.TestCase):
    """DimensionMappingValidationDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DimensionMappingValidationDTO:
        """Test DimensionMappingValidationDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DimensionMappingValidationDTO`
        """
        model = DimensionMappingValidationDTO()
        if include_optional:
            return DimensionMappingValidationDTO(
                dimension_id = '',
                dimension_map_id = '',
                failures = [
                    ''
                    ],
                unmapped_members = [
                    visier_api_analytic_model.models.dimension_member_reference_dto.DimensionMemberReferenceDTO(
                        path = [
                            ''
                            ], )
                    ]
            )
        else:
            return DimensionMappingValidationDTO(
        )
        """

    def testDimensionMappingValidationDTO(self):
        """Test DimensionMappingValidationDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
