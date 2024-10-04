# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1508
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.vee_response_dto import VeeResponseDTO

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
                chart_url = '',
                conversation_state = visier_api_data_out.models.vee_conversation_state_dto.VeeConversationStateDTO(
                    question_state = [
                        ''
                        ], ),
                corrections = [
                    visier_api_data_out.models.vee_corrections_dto.VeeCorrectionsDTO(
                        clarifications = [
                            visier_api_data_out.models.vee_clarification_dto.VeeClarificationDTO(
                                attributes = [
                                    ''
                                    ], 
                                dimensions = [
                                    ''
                                    ], 
                                filters = [
                                    ''
                                    ], 
                                message = '', 
                                metrics = [
                                    ''
                                    ], 
                                questions = [
                                    ''
                                    ], )
                            ], 
                        warning = [
                            'VEE_NO_WARNING'
                            ], )
                    ],
                data = visier_api_data_out.models.vee_data_dto.VeeDataDTO(
                    context = '', 
                    data_json = '', ),
                narrative = '',
                reworded_question = '',
                var_schema = visier_api_data_out.models.vee_response_schema_dto.VeeResponseSchemaDTO(
                    concepts = [
                        visier_api_data_out.models.vee_response_schema_reference_dto.VeeResponseSchemaReferenceDTO(
                            name = '', 
                            paths = [
                                ''
                                ], )
                        ], 
                    dimensions = [
                        visier_api_data_out.models.vee_response_schema_reference_dto.VeeResponseSchemaReferenceDTO(
                            name = '', )
                        ], 
                    metrics = [
                        ''
                        ], ),
                status_code = visier_api_data_out.models.vee_status_code_dto.VeeStatusCodeDTO(
                    status_code = 'UNDEFINED', 
                    status_msg = '', ),
                visual = visier_api_data_out.models.vee_visual_dto.VeeVisualDTO(
                    context = '', 
                    image = '', 
                    title = '', )
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
