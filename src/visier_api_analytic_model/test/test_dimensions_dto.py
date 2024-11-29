# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1614
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.dimensions_dto import DimensionsDTO

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

        if include_optional:
            return DimensionsDTO(
                dimensions = [
                    visier_api_analytic_model.models.dimension_dto.DimensionDTO(
                        description = '', 
                        display_name = '', 
                        explanation = '', 
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
                        visible_in_app = True, )
                    ]
            )
        else:
            return DimensionsDTO(
        )

    def testDimensionsDTO(self):
        """Test DimensionsDTO"""
        def validate_instance(instance):
            DimensionsDTO.model_validate(inst_req_only)
            instance_deserialized = DimensionsDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
