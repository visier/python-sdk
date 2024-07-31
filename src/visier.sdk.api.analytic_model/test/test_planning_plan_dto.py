# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.analytic_model.models.planning_plan_dto import PlanningPlanDTO

class TestPlanningPlanDTO(unittest.TestCase):
    """PlanningPlanDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanningPlanDTO:
        """Test PlanningPlanDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlanningPlanDTO`
        """
        model = PlanningPlanDTO()
        if include_optional:
            return PlanningPlanDTO(
                default_contexts = [
                    visier.sdk.api.analytic_model.models.planning_plan_context_dto.PlanningPlanContextDTO(
                        concept_filter_context = null, 
                        hierarchy_filter_context = null, )
                    ],
                id = '',
                name = '',
                plan_dimension_ids = [
                    ''
                    ],
                scenarios = [
                    visier.sdk.api.analytic_model.models.scenario_or_snapshot_dto.ScenarioOrSnapshotDTO(
                        display_name = '', 
                        id = '', )
                    ],
                snapshots = [
                    visier.sdk.api.analytic_model.models.scenario_or_snapshot_dto.ScenarioOrSnapshotDTO(
                        display_name = '', 
                        id = '', )
                    ],
                subject_id = ''
            )
        else:
            return PlanningPlanDTO(
        )
        """

    def testPlanningPlanDTO(self):
        """Test PlanningPlanDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
