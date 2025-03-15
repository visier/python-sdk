# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.analysis_common_transfers_vee_response_dto import AnalysisCommonTransfersVeeResponseDTO

class TestAnalysisCommonTransfersVeeResponseDTO(unittest.TestCase):
    """AnalysisCommonTransfersVeeResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnalysisCommonTransfersVeeResponseDTO:
        """Test AnalysisCommonTransfersVeeResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return AnalysisCommonTransfersVeeResponseDTO(
                chart_url = '',
                conversation_state = visier_api_data_out.models.analysis/common/transfers/vee_conversation_state_dto.analysis.common.transfers.VeeConversationStateDTO(
                    question_state = [
                        ''
                        ], ),
                corrections = [
                    visier_api_data_out.models.analysis/common/transfers/vee_corrections_dto.analysis.common.transfers.VeeCorrectionsDTO(
                        clarifications = [
                            visier_api_data_out.models.analysis/common/transfers/vee_clarification_dto.analysis.common.transfers.VeeClarificationDTO(
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
                data = visier_api_data_out.models.analysis/common/transfers/vee_data_dto.analysis.common.transfers.VeeDataDTO(
                    context = '', 
                    data_json = '', ),
                narrative = '',
                reworded_question = '',
                var_schema = visier_api_data_out.models.analysis/common/transfers/vee_response_schema_dto.analysis.common.transfers.VeeResponseSchemaDTO(
                    concepts = [
                        visier_api_data_out.models.analysis/common/transfers/vee_response_schema_reference_dto.analysis.common.transfers.VeeResponseSchemaReferenceDTO(
                            name = '', 
                            paths = [
                                ''
                                ], )
                        ], 
                    dimensions = [
                        visier_api_data_out.models.analysis/common/transfers/vee_response_schema_reference_dto.analysis.common.transfers.VeeResponseSchemaReferenceDTO(
                            name = '', )
                        ], 
                    metrics = [
                        ''
                        ], ),
                status_code = visier_api_data_out.models.analysis/common/transfers/vee_status_code_dto.analysis.common.transfers.VeeStatusCodeDTO(
                    status_code = 'UNDEFINED', 
                    status_msg = '', ),
                visual = visier_api_data_out.models.analysis/common/transfers/vee_visual_dto.analysis.common.transfers.VeeVisualDTO(
                    context = '', 
                    image = '', 
                    title = '', )
            )
        else:
            return AnalysisCommonTransfersVeeResponseDTO(
        )

    def testAnalysisCommonTransfersVeeResponseDTO(self):
        """Test AnalysisCommonTransfersVeeResponseDTO"""
        def validate_instance(instance):
            AnalysisCommonTransfersVeeResponseDTO.model_validate(inst_req_only)
            instance_deserialized = AnalysisCommonTransfersVeeResponseDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
