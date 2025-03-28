# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1813
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.analysis_common_vee_response_dto import AnalysisCommonVeeResponseDTO

class TestAnalysisCommonVeeResponseDTO(unittest.TestCase):
    """AnalysisCommonVeeResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnalysisCommonVeeResponseDTO:
        """Test AnalysisCommonVeeResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return AnalysisCommonVeeResponseDTO(
                chart_url = '',
                conversation_state = visier_api_data_out.models.analysis/common/vee_conversation_state_dto.analysis.common.VeeConversationStateDTO(
                    question_state = [
                        ''
                        ], ),
                corrections = [
                    visier_api_data_out.models.analysis/common/vee_corrections_dto.analysis.common.VeeCorrectionsDTO(
                        clarifications = [
                            visier_api_data_out.models.analysis/common/vee_clarification_dto.analysis.common.VeeClarificationDTO(
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
                data = visier_api_data_out.models.analysis/common/vee_data_dto.analysis.common.VeeDataDTO(
                    context = '', 
                    data_json = '', ),
                narrative = '',
                reworded_question = '',
                var_schema = visier_api_data_out.models.analysis/common/vee_response_schema_dto.analysis.common.VeeResponseSchemaDTO(
                    concepts = [
                        visier_api_data_out.models.analysis/common/vee_response_schema_reference_dto.analysis.common.VeeResponseSchemaReferenceDTO(
                            name = '', 
                            paths = [
                                ''
                                ], )
                        ], 
                    dimensions = [
                        visier_api_data_out.models.analysis/common/vee_response_schema_reference_dto.analysis.common.VeeResponseSchemaReferenceDTO(
                            name = '', )
                        ], 
                    metrics = [
                        ''
                        ], ),
                status_code = visier_api_data_out.models.analysis/common/vee_status_code_dto.analysis.common.VeeStatusCodeDTO(
                    status_code = 'UNDEFINED', 
                    status_msg = '', ),
                visual = visier_api_data_out.models.analysis/common/vee_visual_dto.analysis.common.VeeVisualDTO(
                    context = '', 
                    image = '', 
                    title = '', )
            )
        else:
            return AnalysisCommonVeeResponseDTO(
        )

    def testAnalysisCommonVeeResponseDTO(self):
        """Test AnalysisCommonVeeResponseDTO"""
        def validate_instance(instance):
            AnalysisCommonVeeResponseDTO.model_validate(inst_req_only)
            instance_deserialized = AnalysisCommonVeeResponseDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
