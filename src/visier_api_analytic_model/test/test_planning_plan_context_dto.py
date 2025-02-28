# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1760
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.planning_plan_context_dto import PlanningPlanContextDTO

class TestPlanningPlanContextDTO(unittest.TestCase):
    """PlanningPlanContextDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanningPlanContextDTO:
        """Test PlanningPlanContextDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return PlanningPlanContextDTO(
                concept_filter_context = visier_api_analytic_model.models.planning_concept_filter_context_dto.PlanningConceptFilterContextDTO(
                    name = '', ),
                hierarchy_filter_context = visier_api_analytic_model.models.planning_hierarchy_filter_context_dto.PlanningHierarchyFilterContextDTO(
                    excluded_members = [
                        ''
                        ], 
                    hierarchy_name = '', 
                    included_members = [
                        ''
                        ], )
            )
        else:
            return PlanningPlanContextDTO(
        )

    def testPlanningPlanContextDTO(self):
        """Test PlanningPlanContextDTO"""
        def validate_instance(instance):
            PlanningPlanContextDTO.model_validate(inst_req_only)
            instance_deserialized = PlanningPlanContextDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
