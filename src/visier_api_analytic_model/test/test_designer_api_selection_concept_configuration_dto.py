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
from visier_api_analytic_model.models.designer_api_selection_concept_configuration_dto import DesignerApiSelectionConceptConfigurationDTO

class TestDesignerApiSelectionConceptConfigurationDTO(unittest.TestCase):
    """DesignerApiSelectionConceptConfigurationDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DesignerApiSelectionConceptConfigurationDTO:
        """Test DesignerApiSelectionConceptConfigurationDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DesignerApiSelectionConceptConfigurationDTO(
                analytic_object_filters = [
                    visier_api_analytic_model.models.designer/api/analytic_object_filter_dto.designer.api.AnalyticObjectFilterDTO(
                        analytic_object_uuid = '', 
                        symbol_name = '', 
                        dimensions = [
                            visier_api_analytic_model.models.designer/api/dimension_filter_dto.designer.api.DimensionFilterDTO(
                                dimension_id = '', 
                                symbol_name = '', 
                                dimension_members = [
                                    visier_api_analytic_model.models.designer/api/dimension_member_dto.designer.api.DimensionMemberDTO(
                                        dimension_member = [
                                            ''
                                            ], )
                                    ], )
                            ], )
                    ]
            )
        else:
            return DesignerApiSelectionConceptConfigurationDTO(
        )

    def testDesignerApiSelectionConceptConfigurationDTO(self):
        """Test DesignerApiSelectionConceptConfigurationDTO"""
        def validate_instance(instance):
            DesignerApiSelectionConceptConfigurationDTO.model_validate(inst_req_only)
            instance_deserialized = DesignerApiSelectionConceptConfigurationDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
