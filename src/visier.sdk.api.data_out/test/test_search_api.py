# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.api.search_api import SearchApi


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
