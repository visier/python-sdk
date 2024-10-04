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

from visier_api_data_out.api.data_query_api import DataQueryApi


class TestDataQueryApi(unittest.TestCase):
    """DataQueryApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataQueryApi()

    def tearDown(self) -> None:
        pass

    def test_aggregate(self) -> None:
        """Test case for aggregate

        Query aggregate data
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        Query a list of details
        """
        pass

    def test_query_snapshot(self) -> None:
        """Test case for query_snapshot

        Query a series of detailed snapshots
        """
        pass

    def test_sql_like(self) -> None:
        """Test case for sql_like

        Query aggregate or list data using SQL-like syntax
        """
        pass


if __name__ == '__main__':
    unittest.main()
