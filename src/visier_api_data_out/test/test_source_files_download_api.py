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

from visier_api_data_out.api.source_files_download_api import SourceFilesDownloadApi


class TestSourceFilesDownloadApi(unittest.TestCase):
    """SourceFilesDownloadApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SourceFilesDownloadApi()

    def tearDown(self) -> None:
        pass

    def test_download_source_files(self) -> None:
        """Test case for download_source_files

        Download source files
        """
        pass


if __name__ == '__main__':
    unittest.main()
