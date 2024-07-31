# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.analytic_model.models.selection_concept_configuration_map_dto import SelectionConceptConfigurationMapDTO

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
        # uncomment below to create an instance of `SelectionConceptConfigurationMapDTO`
        """
        model = SelectionConceptConfigurationMapDTO()
        if include_optional:
            return SelectionConceptConfigurationMapDTO(
                analytic_object_filters_to_map = [
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
                    ]
            )
        else:
            return SelectionConceptConfigurationMapDTO(
        )
        """

    def testSelectionConceptConfigurationMapDTO(self):
        """Test SelectionConceptConfigurationMapDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
