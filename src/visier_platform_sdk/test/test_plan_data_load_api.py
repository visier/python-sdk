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

from visier_platform_sdk.api.plan_data_load_api import PlanDataLoadApi


class TestPlanDataLoadApi(unittest.TestCase):
    """PlanDataLoadApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlanDataLoadApi()

    def tearDown(self) -> None:
        pass

    def test_plan_data_upload(self) -> None:
        """Test case for plan_data_upload

        Upload plan data
        """
        pass

    def test_plan_row_data_load(self) -> None:
        """Test case for plan_row_data_load

        Add or remove plan rows
        """
        pass


if __name__ == '__main__':
    unittest.main()
