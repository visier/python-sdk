# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.api.data_upload_api import DataUploadApi


class TestDataUploadApi(unittest.TestCase):
    """DataUploadApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataUploadApi()

    def tearDown(self) -> None:
        pass

    def test_v1_data_upload_files_filename_put(self) -> None:
        """Test case for v1_data_upload_files_filename_put

        Upload a data file to Visier
        """
        pass


if __name__ == '__main__':
    unittest.main()
