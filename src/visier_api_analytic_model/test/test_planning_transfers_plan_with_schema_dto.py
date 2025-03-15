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
from visier_api_analytic_model.models.planning_transfers_plan_with_schema_dto import PlanningTransfersPlanWithSchemaDTO

class TestPlanningTransfersPlanWithSchemaDTO(unittest.TestCase):
    """PlanningTransfersPlanWithSchemaDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanningTransfersPlanWithSchemaDTO:
        """Test PlanningTransfersPlanWithSchemaDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return PlanningTransfersPlanWithSchemaDTO(
                errors = [
                    visier_api_analytic_model.models.planning/transfers/plan_data_load_error_dto.planning.transfers.PlanDataLoadErrorDTO(
                        error_message = '', 
                        rci = '', 
                        row = 56, )
                    ],
                plan = visier_api_analytic_model.models.planning/transfers/plan_info_dto.planning.transfers.PlanInfoDTO(
                    currency_code = '', 
                    display_name = '', 
                    model_id = '', 
                    parent_plan_uuid = '', 
                    scenarios = [
                        visier_api_analytic_model.models.planning/transfers/scenario_info_dto.planning.transfers.ScenarioInfoDTO(
                            display_name = '', 
                            uuid = '', 
                            versioned_scenario_id = '', )
                        ], 
                    uuid = '', ),
                var_schema = visier_api_analytic_model.models.planning/transfers/plan_schema_dto.planning.transfers.PlanSchemaDTO(
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
                        ], )
            )
        else:
            return PlanningTransfersPlanWithSchemaDTO(
        )

    def testPlanningTransfersPlanWithSchemaDTO(self):
        """Test PlanningTransfersPlanWithSchemaDTO"""
        def validate_instance(instance):
            PlanningTransfersPlanWithSchemaDTO.model_validate(inst_req_only)
            instance_deserialized = PlanningTransfersPlanWithSchemaDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
