# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1598
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_data_in.api.planning_data_load_api import PlanningDataLoadApi


class TestPlanningDataLoadApi(unittest.TestCase):
    """PlanningDataLoadApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlanningDataLoadApi()

    def tearDown(self) -> None:
        pass

    def test_plan_data_load_plan_data_upload(self) -> None:
        """Test case for plan_data_load_plan_data_upload

        Upload plan data
        """
        pass

    def test_plan_data_load_plan_row_data_load(self) -> None:
        """Test case for plan_data_load_plan_row_data_load

        Add or remove plan rows
        """
        pass


if __name__ == '__main__':
    unittest.main()
