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
from visier_platform_sdk.models.process_concept_stage_dto import ProcessConceptStageDTO

class TestProcessConceptStageDTO(unittest.TestCase):
    """ProcessConceptStageDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProcessConceptStageDTO:
        """Test ProcessConceptStageDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ProcessConceptStageDTO(
                uuid = '',
                object_name = '',
                basic_information = visier_platform_sdk.models.basic_information_dto.BasicInformationDTO(
                    display_name = '', 
                    short_display_name = '', 
                    description = '', 
                    explanation = '', 
                    designer_notes = '', 
                    synonym_list = None, ),
                mapped_member_list = visier_platform_sdk.models.process_concept_member_list_dto.ProcessConceptMemberListDTO(
                    members = [
                        visier_platform_sdk.models.process_concept_member_dto.ProcessConceptMemberDTO(
                            display_name = '', 
                            name_path = [
                                ''
                                ], )
                        ], )
            )
        else:
            return ProcessConceptStageDTO(
        )

    def testProcessConceptStageDTO(self):
        """Test ProcessConceptStageDTO"""
        def validate_instance(instance):
            ProcessConceptStageDTO.model_validate(inst_req_only)
            instance_deserialized = ProcessConceptStageDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
