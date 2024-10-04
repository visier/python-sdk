# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1508
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_data_out.api.search_api import SearchApi


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SearchApi()

    def tearDown(self) -> None:
        pass

    def test_simple_search_document_headers(self) -> None:
        """Test case for simple_search_document_headers

        Perform a simple search for Visier document headers
        """
        pass


if __name__ == '__main__':
    unittest.main()
