# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1892
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.servicing_sample_question_api_response_dto import ServicingSampleQuestionAPIResponseDTO

class TestServicingSampleQuestionAPIResponseDTO(unittest.TestCase):
    """ServicingSampleQuestionAPIResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingSampleQuestionAPIResponseDTO:
        """Test ServicingSampleQuestionAPIResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingSampleQuestionAPIResponseDTO(
                question = '',
                question_id = '',
                visible_in_vee = True,
                category_id = '',
                user_group_assignment = visier_api_analytic_model.models.servicing/user_group_assignment_dto.servicing.UserGroupAssignmentDTO(
                    user_group_ids = [
                        ''
                        ], )
            )
        else:
            return ServicingSampleQuestionAPIResponseDTO(
        )

    def testServicingSampleQuestionAPIResponseDTO(self):
        """Test ServicingSampleQuestionAPIResponseDTO"""
        def validate_instance(instance):
            ServicingSampleQuestionAPIResponseDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingSampleQuestionAPIResponseDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
