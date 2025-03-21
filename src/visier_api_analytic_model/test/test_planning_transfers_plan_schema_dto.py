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
from visier_api_analytic_model.models.planning_transfers_plan_schema_dto import PlanningTransfersPlanSchemaDTO

class TestPlanningTransfersPlanSchemaDTO(unittest.TestCase):
    """PlanningTransfersPlanSchemaDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanningTransfersPlanSchemaDTO:
        """Test PlanningTransfersPlanSchemaDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return PlanningTransfersPlanSchemaDTO(
                plan_items = [
                    visier_api_analytic_model.models.planning/transfers/plan_item_dto.planning.transfers.PlanItemDTO(
                        data_type = 'unknown', 
                        display_name = '', 
                        id = '', )
                    ],
                plan_segment_level_members = [
                    visier_api_analytic_model.models.planning/transfers/plan_segment_level_member_list_dto.planning.transfers.PlanSegmentLevelMemberListDTO(
                        members = [
                            visier_api_analytic_model.models.planning/transfers/plan_segment_level_member_dto.planning.transfers.PlanSegmentLevelMemberDTO(
                                display_name = '', 
                                id = '', 
                                is_custom = True, 
                                parent_id = '', )
                            ], 
                        segment_id = '', 
                        segment_level_id = '', )
                    ],
                plan_segment_levels = [
                    visier_api_analytic_model.models.planning/transfers/plan_segment_level_dto.planning.transfers.PlanSegmentLevelDTO(
                        display_name = '', 
                        id = '', 
                        order = 56, 
                        segment_display_name = '', 
                        segment_id = '', )
                    ],
                time_periods = [
                    visier_api_analytic_model.models.planning/transfers/plan_time_period_dto.planning.transfers.PlanTimePeriodDTO(
                        date = '', 
                        display_name = '', )
                    ]
            )
        else:
            return PlanningTransfersPlanSchemaDTO(
        )

    def testPlanningTransfersPlanSchemaDTO(self):
        """Test PlanningTransfersPlanSchemaDTO"""
        def validate_instance(instance):
            PlanningTransfersPlanSchemaDTO.model_validate(inst_req_only)
            instance_deserialized = PlanningTransfersPlanSchemaDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
