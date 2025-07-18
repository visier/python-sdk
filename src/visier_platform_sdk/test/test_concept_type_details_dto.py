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
from visier_platform_sdk.models.concept_type_details_dto import ConceptTypeDetailsDTO

class TestConceptTypeDetailsDTO(unittest.TestCase):
    """ConceptTypeDetailsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConceptTypeDetailsDTO:
        """Test ConceptTypeDetailsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ConceptTypeDetailsDTO(
                process = visier_platform_sdk.models.process_concept_definition_dto.ProcessConceptDefinitionDTO(
                    analytic_object_name = '', 
                    status_dimension_object_name = '', 
                    participation_concept_uuid = '', 
                    on_hold_concept_uuid = '', 
                    stage_list = None, 
                    outcome_list = None, 
                    metric_list = None, 
                    property_list = None, 
                    tag_list = None, 
                    visible_in_analytics = True, 
                    include_with_vee = True, ),
                member_selection = visier_platform_sdk.models.member_selection_concept_dto.MemberSelectionConceptDTO(
                    analytic_object_filter_list = None, 
                    tag_list = None, 
                    visible_in_analytics = True, 
                    include_with_vee = True, ),
                calculated_selection = visier_platform_sdk.models.calculated_selection_concept_dto.CalculatedSelectionConceptDTO(
                    formula = '', 
                    analytic_object_names = None, 
                    tag_list = None, 
                    visible_in_analytics = True, 
                    include_with_vee = True, )
            )
        else:
            return ConceptTypeDetailsDTO(
        )

    def testConceptTypeDetailsDTO(self):
        """Test ConceptTypeDetailsDTO"""
        def validate_instance(instance):
            ConceptTypeDetailsDTO.model_validate(inst_req_only)
            instance_deserialized = ConceptTypeDetailsDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
