# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_data_out.api.data_version_export_api import DataVersionExportApi


class TestDataVersionExportApi(unittest.TestCase):
    """DataVersionExportApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataVersionExportApi()

    def tearDown(self) -> None:
        pass

    def test_call_1_alpha_download_file(self) -> None:
        """Test case for call_1_alpha_download_file

        Download a file from a data version export
        """
        pass

    def test_get_available_data_versions(self) -> None:
        """Test case for get_available_data_versions

        Retrieve a list of all data versions
        """
        pass

    def test_get_available_exports(self) -> None:
        """Test case for get_available_exports

        Retrieve the details of all data version exports
        """
        pass

    def test_get_export(self) -> None:
        """Test case for get_export

        Retrieve the details of a data version export
        """
        pass

    def test_get_export_job_status(self) -> None:
        """Test case for get_export_job_status

        Retrieve a data version export job's status
        """
        pass

    def test_schedule_export_job(self) -> None:
        """Test case for schedule_export_job

        Schedule a data version export job
        """
        pass


if __name__ == '__main__':
    unittest.main()
