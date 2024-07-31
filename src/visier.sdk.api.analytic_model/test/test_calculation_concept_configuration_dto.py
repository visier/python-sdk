# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.analytic_model.models.calculation_concept_configuration_dto import CalculationConceptConfigurationDTO

class TestCalculationConceptConfigurationDTO(unittest.TestCase):
    """CalculationConceptConfigurationDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CalculationConceptConfigurationDTO:
        """Test CalculationConceptConfigurationDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CalculationConceptConfigurationDTO`
        """
        model = CalculationConceptConfigurationDTO()
        if include_optional:
            return CalculationConceptConfigurationDTO(
                perspectives = [
                    visier.sdk.api.analytic_model.models.perspective_configuration_dto.PerspectiveConfigurationDTO(
                        perspective_id = '', 
                        perspective_name = '', 
                        perspective_nodes = [
                            visier.sdk.api.analytic_model.models.perspective_node_dto.PerspectiveNodeDTO(
                                analytic_object_filters = [
                                    visier.sdk.api.analytic_model.models.analytic_object_filter_dto.AnalyticObjectFilterDTO(
                                        analytic_object_uuid = '', 
                                        dimensions = [
                                            visier.sdk.api.analytic_model.models.dimension_filter_dto.DimensionFilterDTO(
                                                dimension_id = '', 
                                                dimension_members = [
                                                    visier.sdk.api.analytic_model.models.dimension_member_dto.DimensionMemberDTO(
                                                        dimension_member = [
                                                            ''
                                                            ], )
                                                    ], 
                                                symbol_name = '', )
                                            ], 
                                        symbol_name = '', )
                                    ], 
                                selection_concept_uuid = '', 
                                symbol_name = '', )
                            ], )
                    ]
            )
        else:
            return CalculationConceptConfigurationDTO(
        )
        """

    def testCalculationConceptConfigurationDTO(self):
        """Test CalculationConceptConfigurationDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
