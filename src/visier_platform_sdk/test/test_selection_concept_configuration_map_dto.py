# coding: utf-8

"""
    API Reference

    Detailed API reference documentation for Visier APIs. Includes all endpoints, headers, path parameters, query parameters, request body schema, response schema, JSON request samples, and JSON response samples.

    The version of the OpenAPI document: 22222222.99201.2050
    Contact: alpine@visier.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import visier_platform_sdk.models
from visier_platform_sdk.models.selection_concept_configuration_map_dto import SelectionConceptConfigurationMapDTO

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
                    visier_platform_sdk.models.analytic_object_filter_dto.AnalyticObjectFilterDTO(
                        analytic_object_name = '', 
                        filters = [
                            visier_platform_sdk.models.dimension_filter_dto.DimensionFilterDTO(
                                dimension_name = '', 
                                qualifying_path = [
                                    ''
                                    ], 
                                member_selections = [
                                    visier_platform_sdk.models.member_selection_dto.MemberSelectionDTO(
                                        name_path = [
                                            ''
                                            ], 
                                        is_excluded = True, )
                                    ], )
                            ], )
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
