# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1547
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.selection_concept_configuration_map_dto import SelectionConceptConfigurationMapDTO

class TestSelectionConceptConfigurationMapDTO(unittest.TestCase):
    """SelectionConceptConfigurationMapDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SelectionConceptConfigurationMapDTO:
        """Test SelectionConceptConfigurationMapDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return SelectionConceptConfigurationMapDTO(
                analytic_object_filters_to_map = [
                    visier_api_analytic_model.models.analytic_object_filter_dto.AnalyticObjectFilterDTO(
                        analytic_object_uuid = '', 
                        dimensions = [
                            visier_api_analytic_model.models.dimension_filter_dto.DimensionFilterDTO(
                                dimension_id = '', 
                                dimension_members = [
                                    visier_api_analytic_model.models.dimension_member_dto.DimensionMemberDTO(
                                        dimension_member = [
                                            ''
                                            ], )
                                    ], 
                                symbol_name = '', )
                            ], 
                        symbol_name = '', )
                    ]
            )
        else:
            return SelectionConceptConfigurationMapDTO(
        )

    def testSelectionConceptConfigurationMapDTO(self):
        """Test SelectionConceptConfigurationMapDTO"""
        def validate_instance(instance):
            SelectionConceptConfigurationMapDTO.model_validate(inst_req_only)
            instance_deserialized = SelectionConceptConfigurationMapDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
