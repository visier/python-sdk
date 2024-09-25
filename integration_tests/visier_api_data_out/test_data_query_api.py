# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1474
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501
import unittest

from integration_tests.utils import create_api, get_query_content
from visier_api_data_out import DataQueryApi, ListQueryExecutionDTO, AggregationQueryExecutionDTO, \
    SnapshotQueryExecutionDTO


class TestDataQueryApi(unittest.TestCase):
    """DataQueryApi unit test stubs"""

    def setUp(self) -> None:
        self.api = create_api(DataQueryApi)

    def tearDown(self) -> None:
        pass

    def test_aggregate(self) -> None:
        """Test case for aggregate

        Query aggregate data
        """

        query_content = get_query_content('aggregate.json')
        aggregate_query_dto = AggregationQueryExecutionDTO.from_json(query_content)
        cell_set_dto = self.api.aggregate(aggregate_query_dto)

        self.assertIsNotNone(cell_set_dto)
        self.assertGreater(len(cell_set_dto.axes), 0)
        self.assertGreater(len(cell_set_dto.cells), 0)

    def test_list(self) -> None:
        """Test case for list

        Query a list of details
        """

        query_content = get_query_content('list.json')
        list_query_dto = ListQueryExecutionDTO.from_json(query_content)
        list_response_dto = self.api.list(list_query_dto)

        self.assertIsNotNone(list_response_dto)
        self.assertEqual(len(list_response_dto.rows), list_query_dto.options.limit)

    def test_query_snapshot(self) -> None:
        """Test case for query_snapshot

        Query a series of detailed snapshots
        """

        query_content = get_query_content('snapshot.json')
        snapshot_query_dto = SnapshotQueryExecutionDTO.from_json(query_content)
        response_dto = self.api.query_snapshot(snapshot_query_dto)

        self.assertIsNotNone(response_dto)
        self.assertEqual(len(response_dto.rows), snapshot_query_dto.options.limit)


if __name__ == '__main__':
    unittest.main()
