# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1474
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.dimension_dto import DimensionDTO

class TestDimensionDTO(unittest.TestCase):
    """DimensionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DimensionDTO:
        """Test DimensionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DimensionDTO`
        """
        model = DimensionDTO()
        if include_optional:
            return DimensionDTO(
                description = '',
                display_name = '',
                id = '',
                levels = [
                    visier_api_analytic_model.models.level_dto.LevelDTO(
                        depth = 56, 
                        display_name = '', 
                        id = '', )
                    ],
                member_count = 56,
                tags = [
                    visier_api_analytic_model.models.tag_map_element_dto.TagMapElementDTO(
                        display_name = '', 
                        id = '', )
                    ],
                unknown_member = [
                    ''
                    ],
                visible_in_app = True
            )
        else:
            return DimensionDTO(
        )
        """

    def testDimensionDTO(self):
        """Test DimensionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
