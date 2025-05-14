# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1905
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.dataservices_datamodel_dimension_dto import DataservicesDatamodelDimensionDTO

class TestDataservicesDatamodelDimensionDTO(unittest.TestCase):
    """DataservicesDatamodelDimensionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesDatamodelDimensionDTO:
        """Test DataservicesDatamodelDimensionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesDatamodelDimensionDTO(
                id = '',
                display_name = '',
                description = '',
                levels = [
                    visier_api_analytic_model.models.dataservices/datamodel/level_dto.dataservices.datamodel.LevelDTO(
                        id = '', 
                        display_name = '', 
                        depth = 56, )
                    ],
                unknown_member = [
                    ''
                    ],
                member_count = 56,
                visible_in_app = True,
                tags = [
                    visier_api_analytic_model.models.dataservices/datamodel/tag_map_element_dto.dataservices.datamodel.TagMapElementDTO(
                        id = '', 
                        display_name = '', )
                    ],
                explanation = ''
            )
        else:
            return DataservicesDatamodelDimensionDTO(
        )

    def testDataservicesDatamodelDimensionDTO(self):
        """Test DataservicesDatamodelDimensionDTO"""
        def validate_instance(instance):
            DataservicesDatamodelDimensionDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesDatamodelDimensionDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
