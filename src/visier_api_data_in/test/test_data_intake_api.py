# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1547
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_data_in.api.data_intake_api import DataIntakeApi


class TestDataIntakeApi(unittest.TestCase):
    """DataIntakeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataIntakeApi()

    def tearDown(self) -> None:
        pass

    def test_get_sources(self) -> None:
        """Test case for get_sources

        Retrieve a list of sources
        """
        pass

    def test_push_data(self) -> None:
        """Test case for push_data

        Transfer data to sources via JSON
        """
        pass

    def test_push_data_cancel(self) -> None:
        """Test case for push_data_cancel

        Cancel a transfer session
        """
        pass

    def test_push_data_complete(self) -> None:
        """Test case for push_data_complete

        Complete a transfer session
        """
        pass

    def test_start_transfer(self) -> None:
        """Test case for start_transfer

        Start a transfer session
        """
        pass

    def test_upload_data(self) -> None:
        """Test case for upload_data

        Transfer data to sources via file upload
        """
        pass


if __name__ == '__main__':
    unittest.main()
