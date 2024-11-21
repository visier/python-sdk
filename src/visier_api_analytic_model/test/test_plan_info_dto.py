# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1598
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.plan_info_dto import PlanInfoDTO

class TestPlanInfoDTO(unittest.TestCase):
    """PlanInfoDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanInfoDTO:
        """Test PlanInfoDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return PlanInfoDTO(
                currency_code = '',
                display_name = '',
                model_id = '',
                parent_plan_uuid = '',
                scenarios = [
                    visier_api_analytic_model.models.scenario_info_dto.ScenarioInfoDTO(
                        display_name = '', 
                        uuid = '', 
                        versioned_scenario_id = '', )
                    ],
                uuid = ''
            )
        else:
            return PlanInfoDTO(
        )

    def testPlanInfoDTO(self):
        """Test PlanInfoDTO"""
        def validate_instance(instance):
            PlanInfoDTO.model_validate(inst_req_only)
            instance_deserialized = PlanInfoDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
