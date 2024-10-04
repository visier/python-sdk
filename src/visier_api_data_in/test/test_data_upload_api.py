# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1508
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_data_in.api.data_upload_api import DataUploadApi


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
