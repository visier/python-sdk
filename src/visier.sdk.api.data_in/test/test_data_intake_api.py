# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.api.data_intake_api import DataIntakeApi


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
