# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1905
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.analysis_common_vee_feedback_dto import AnalysisCommonVeeFeedbackDTO

class TestAnalysisCommonVeeFeedbackDTO(unittest.TestCase):
    """AnalysisCommonVeeFeedbackDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnalysisCommonVeeFeedbackDTO:
        """Test AnalysisCommonVeeFeedbackDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return AnalysisCommonVeeFeedbackDTO(
                response = visier_api_data_out.models.analysis/common/vee_response_dto.analysis.common.VeeResponseDTO(
                    conversation_state = None, 
                    status_code = None, 
                    narrative = '', 
                    chart_url = '', 
                    schema = None, 
                    corrections = [
                        visier_api_data_out.models.analysis/common/vee_corrections_dto.analysis.common.VeeCorrectionsDTO(
                            warning = [
                                'VEE_NO_WARNING'
                                ], 
                            clarifications = [
                                visier_api_data_out.models.analysis/common/vee_clarification_dto.analysis.common.VeeClarificationDTO(
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
                    data = None, 
                    visual = None, 
                    reworded_question = '', ),
                is_approved = True,
                description = ''
            )
        else:
            return AnalysisCommonVeeFeedbackDTO(
        )

    def testAnalysisCommonVeeFeedbackDTO(self):
        """Test AnalysisCommonVeeFeedbackDTO"""
        def validate_instance(instance):
            AnalysisCommonVeeFeedbackDTO.model_validate(inst_req_only)
            instance_deserialized = AnalysisCommonVeeFeedbackDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
