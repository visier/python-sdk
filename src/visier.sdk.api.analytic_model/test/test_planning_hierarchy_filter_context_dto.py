# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1418
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.analytic_model.models.planning_hierarchy_filter_context_dto import PlanningHierarchyFilterContextDTO

class TestPlanningHierarchyFilterContextDTO(unittest.TestCase):
    """PlanningHierarchyFilterContextDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanningHierarchyFilterContextDTO:
        """Test PlanningHierarchyFilterContextDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlanningHierarchyFilterContextDTO`
        """
        model = PlanningHierarchyFilterContextDTO()
        if include_optional:
            return PlanningHierarchyFilterContextDTO(
                excluded_members = [
                    ''
                    ],
                hierarchy_name = '',
                included_members = [
                    ''
                    ]
            )
        else:
            return PlanningHierarchyFilterContextDTO(
        )
        """

    def testPlanningHierarchyFilterContextDTO(self):
        """Test PlanningHierarchyFilterContextDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
