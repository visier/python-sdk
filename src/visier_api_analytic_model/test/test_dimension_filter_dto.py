# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.99201.1475
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.dimension_filter_dto import DimensionFilterDTO

class TestDimensionFilterDTO(unittest.TestCase):
    """DimensionFilterDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DimensionFilterDTO:
        """Test DimensionFilterDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DimensionFilterDTO`
        """
        model = DimensionFilterDTO()
        if include_optional:
            return DimensionFilterDTO(
                dimension_id = '',
                dimension_members = [
                    visier_api_analytic_model.models.dimension_member_dto.DimensionMemberDTO(
                        dimension_member = [
                            ''
                            ], )
                    ],
                symbol_name = ''
            )
        else:
            return DimensionFilterDTO(
        )
        """

    def testDimensionFilterDTO(self):
        """Test DimensionFilterDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
