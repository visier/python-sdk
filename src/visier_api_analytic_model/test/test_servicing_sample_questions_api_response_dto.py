# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1905
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.servicing_sample_questions_api_response_dto import ServicingSampleQuestionsAPIResponseDTO

class TestServicingSampleQuestionsAPIResponseDTO(unittest.TestCase):
    """ServicingSampleQuestionsAPIResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingSampleQuestionsAPIResponseDTO:
        """Test ServicingSampleQuestionsAPIResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingSampleQuestionsAPIResponseDTO(
                questions = [
                    visier_api_analytic_model.models.servicing/sample_question_api_response_dto.servicing.SampleQuestionAPIResponseDTO(
                        question = '', 
                        question_id = '', 
                        visible_in_vee = True, 
                        category_id = '', 
                        user_group_assignment = None, )
                    ]
            )
        else:
            return ServicingSampleQuestionsAPIResponseDTO(
        )

    def testServicingSampleQuestionsAPIResponseDTO(self):
        """Test ServicingSampleQuestionsAPIResponseDTO"""
        def validate_instance(instance):
            ServicingSampleQuestionsAPIResponseDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingSampleQuestionsAPIResponseDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
