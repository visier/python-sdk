# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.analytic_model.models.dimensions_dto import DimensionsDTO

class TestDimensionsDTO(unittest.TestCase):
    """DimensionsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DimensionsDTO:
        """Test DimensionsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DimensionsDTO`
        """
        model = DimensionsDTO()
        if include_optional:
            return DimensionsDTO(
                dimensions = [
                    visier.sdk.api.analytic_model.models.dimension_dto.DimensionDTO(
                        description = '', 
                        display_name = '', 
                        id = '', 
                        levels = [
                            visier.sdk.api.analytic_model.models.level_dto.LevelDTO(
                                depth = 56, 
                                display_name = '', 
                                id = '', )
                            ], 
                        member_count = 56, 
                        tags = [
                            visier.sdk.api.analytic_model.models.tag_map_element_dto.TagMapElementDTO(
                                display_name = '', 
                                id = '', )
                            ], 
                        unknown_member = [
                            ''
                            ], 
                        visible_in_app = True, )
                    ]
            )
        else:
            return DimensionsDTO(
        )
        """

    def testDimensionsDTO(self):
        """Test DimensionsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
