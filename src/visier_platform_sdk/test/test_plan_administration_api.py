# coding: utf-8

"""
    API Reference

    Detailed API reference documentation for Visier APIs. Includes all endpoints, headers, path parameters, query parameters, request body schema, response schema, JSON request samples, and JSON response samples.

    The version of the OpenAPI document: 22222222.99201.2050
    Contact: alpine@visier.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_platform_sdk.api.plan_administration_api import PlanAdministrationApi


class TestPlanAdministrationApi(unittest.TestCase):
    """PlanAdministrationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlanAdministrationApi()

    def tearDown(self) -> None:
        pass

    def test_patch_plan(self) -> None:
        """Test case for patch_plan

        Partially update a subplan
        """
        pass

    def test_patch_plans(self) -> None:
        """Test case for patch_plans

        Partially update subplans
        """
        pass


if __name__ == '__main__':
    unittest.main()
