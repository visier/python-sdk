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
from visier_api_data_out.models.analysis_common_transfers_vee_feedback_dto import AnalysisCommonTransfersVeeFeedbackDTO

class TestAnalysisCommonTransfersVeeFeedbackDTO(unittest.TestCase):
    """AnalysisCommonTransfersVeeFeedbackDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnalysisCommonTransfersVeeFeedbackDTO:
        """Test AnalysisCommonTransfersVeeFeedbackDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return AnalysisCommonTransfersVeeFeedbackDTO(
                description = '',
                is_approved = True,
                response = visier_api_data_out.models.analysis/common/transfers/vee_response_dto.analysis.common.transfers.VeeResponseDTO(
                    chart_url = '', 
                    conversation_state = None, 
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
                    data = None, 
                    narrative = '', 
                    reworded_question = '', 
                    schema = None, 
                    status_code = None, 
                    visual = None, )
            )
        else:
            return AnalysisCommonTransfersVeeFeedbackDTO(
        )

    def testAnalysisCommonTransfersVeeFeedbackDTO(self):
        """Test AnalysisCommonTransfersVeeFeedbackDTO"""
        def validate_instance(instance):
            AnalysisCommonTransfersVeeFeedbackDTO.model_validate(inst_req_only)
            instance_deserialized = AnalysisCommonTransfersVeeFeedbackDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
