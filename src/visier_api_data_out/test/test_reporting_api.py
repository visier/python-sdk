# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1701
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_data_out.api.reporting_api import ReportingApi


class TestReportingApi(unittest.TestCase):
    """ReportingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReportingApi()

    def tearDown(self) -> None:
        pass

    def test_create_report(self) -> None:
        """Test case for create_report

        Create a report
        """
        pass

    def test_delete_report(self) -> None:
        """Test case for delete_report

        Delete a report
        """
        pass

    def test_download_report(self) -> None:
        """Test case for download_report

        Download a report
        """
        pass

    def test_duplicate_report(self) -> None:
        """Test case for duplicate_report

        Duplicate a report
        """
        pass

    def test_get_report(self) -> None:
        """Test case for get_report

        Retrieve a report's details
        """
        pass

    def test_get_reports(self) -> None:
        """Test case for get_reports

        Retrieve a list of reports
        """
        pass


if __name__ == '__main__':
    unittest.main()
