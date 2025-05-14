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
from visier_api_analytic_model.models.planning_plan_with_schema_dto import PlanningPlanWithSchemaDTO

class TestPlanningPlanWithSchemaDTO(unittest.TestCase):
    """PlanningPlanWithSchemaDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanningPlanWithSchemaDTO:
        """Test PlanningPlanWithSchemaDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return PlanningPlanWithSchemaDTO(
                plan = visier_api_analytic_model.models.planning/plan_info_dto.planning.PlanInfoDTO(
                    uuid = '', 
                    display_name = '', 
                    model_id = '', 
                    scenarios = [
                        visier_api_analytic_model.models.planning/scenario_info_dto.planning.ScenarioInfoDTO(
                            uuid = '', 
                            display_name = '', 
                            versioned_scenario_id = '', )
                        ], 
                    parent_plan_uuid = '', 
                    currency_code = '', ),
                var_schema = visier_api_analytic_model.models.planning/plan_schema_dto.planning.PlanSchemaDTO(
                    plan_items = [
                        visier_api_analytic_model.models.planning/plan_item_dto.planning.PlanItemDTO(
                            id = '', 
                            display_name = '', 
                            data_type = 'unknown', )
                        ], 
                    time_periods = [
                        visier_api_analytic_model.models.planning/plan_time_period_dto.planning.PlanTimePeriodDTO(
                            date = '', 
                            display_name = '', )
                        ], 
                    plan_segment_levels = [
                        visier_api_analytic_model.models.planning/plan_segment_level_dto.planning.PlanSegmentLevelDTO(
                            id = '', 
                            display_name = '', 
                            order = 56, 
                            segment_id = '', 
                            segment_display_name = '', )
                        ], 
                    plan_segment_level_members = [
                        visier_api_analytic_model.models.planning/plan_segment_level_member_list_dto.planning.PlanSegmentLevelMemberListDTO(
                            segment_level_id = '', 
                            members = [
                                visier_api_analytic_model.models.planning/plan_segment_level_member_dto.planning.PlanSegmentLevelMemberDTO(
                                    id = '', 
                                    display_name = '', 
                                    is_custom = True, 
                                    parent_id = '', )
                                ], 
                            segment_id = '', )
                        ], ),
                errors = [
                    visier_api_analytic_model.models.planning/plan_data_load_error_dto.planning.PlanDataLoadErrorDTO(
                        row = 56, 
                        rci = '', 
                        error_message = '', )
                    ]
            )
        else:
            return PlanningPlanWithSchemaDTO(
        )

    def testPlanningPlanWithSchemaDTO(self):
        """Test PlanningPlanWithSchemaDTO"""
        def validate_instance(instance):
            PlanningPlanWithSchemaDTO.model_validate(inst_req_only)
            instance_deserialized = PlanningPlanWithSchemaDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
