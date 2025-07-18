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
from visier_platform_sdk.models.vee_response_dto import VeeResponseDTO

class TestVeeResponseDTO(unittest.TestCase):
    """VeeResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VeeResponseDTO:
        """Test VeeResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return VeeResponseDTO(
                conversation_state = visier_platform_sdk.models.vee_conversation_state_dto.VeeConversationStateDTO(
                    question_state = [
                        ''
                        ], ),
                status_code = visier_platform_sdk.models.vee_status_code_dto.VeeStatusCodeDTO(
                    status_code = 'UNDEFINED', 
                    status_msg = '', ),
                narrative = '',
                chart_url = '',
                var_schema = visier_platform_sdk.models.vee_response_schema_dto.VeeResponseSchemaDTO(
                    metrics = [
                        ''
                        ], 
                    dimensions = [
                        visier_platform_sdk.models.vee_response_schema_reference_dto.VeeResponseSchemaReferenceDTO(
                            name = '', 
                            paths = [
                                ''
                                ], )
                        ], 
                    concepts = [
                        visier_platform_sdk.models.vee_response_schema_reference_dto.VeeResponseSchemaReferenceDTO(
                            name = '', )
                        ], ),
                corrections = [
                    visier_platform_sdk.models.vee_corrections_dto.VeeCorrectionsDTO(
                        warning = [
                            'VEE_NO_WARNING'
                            ], 
                        clarifications = [
                            visier_platform_sdk.models.vee_clarification_dto.VeeClarificationDTO(
                                message = '', 
                                questions = [
                                    ''
                                    ], 
                                metrics = [
                                    ''
                                    ], 
                                dimensions = [
                                    ''
                                    ], 
                                filters = [
                                    ''
                                    ], 
                                attributes = [
                                    ''
                                    ], )
                            ], )
                    ],
                data = visier_platform_sdk.models.vee_data_dto.VeeDataDTO(
                    data_json = '', 
                    context = '', ),
                visual = visier_platform_sdk.models.vee_visual_dto.VeeVisualDTO(
                    image = '', 
                    title = '', 
                    context = '', ),
                reworded_question = ''
            )
        else:
            return VeeResponseDTO(
        )

    def testVeeResponseDTO(self):
        """Test VeeResponseDTO"""
        def validate_instance(instance):
            VeeResponseDTO.model_validate(inst_req_only)
            instance_deserialized = VeeResponseDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
