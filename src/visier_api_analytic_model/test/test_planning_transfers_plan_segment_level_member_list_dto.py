# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.planning_transfers_plan_segment_level_member_list_dto import PlanningTransfersPlanSegmentLevelMemberListDTO

class TestPlanningTransfersPlanSegmentLevelMemberListDTO(unittest.TestCase):
    """PlanningTransfersPlanSegmentLevelMemberListDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanningTransfersPlanSegmentLevelMemberListDTO:
        """Test PlanningTransfersPlanSegmentLevelMemberListDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return PlanningTransfersPlanSegmentLevelMemberListDTO(
                members = [
                    visier_api_analytic_model.models.planning/transfers/plan_segment_level_member_dto.planning.transfers.PlanSegmentLevelMemberDTO(
                        display_name = '', 
                        id = '', 
                        is_custom = True, 
                        parent_id = '', )
                    ],
                segment_id = '',
                segment_level_id = ''
            )
        else:
            return PlanningTransfersPlanSegmentLevelMemberListDTO(
        )

    def testPlanningTransfersPlanSegmentLevelMemberListDTO(self):
        """Test PlanningTransfersPlanSegmentLevelMemberListDTO"""
        def validate_instance(instance):
            PlanningTransfersPlanSegmentLevelMemberListDTO.model_validate(inst_req_only)
            instance_deserialized = PlanningTransfersPlanSegmentLevelMemberListDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
