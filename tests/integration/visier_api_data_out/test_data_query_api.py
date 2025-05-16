import os
import unittest

from test_utils import create_api
from visier_platform_sdk import DataQueryApi, DataservicesQueryListQueryExecutionDTO, DataservicesQueryAggregationQueryExecutionDTO, \
    DataservicesQuerySnapshotQueryExecutionDTO, DataservicesQuerySqlLikeQueryExecutionDTO, DataservicesQueryCellSetDTO, TableResponseDTO


def get_query_content(file_name):
    file_path = os.path.join('queries', file_name)
    with open(file_path, 'r') as file:
        return file.read()


class TestDataQueryApi(unittest.TestCase):
    """DataQueryApi unit test stubs"""

    def setUp(self) -> None:
        self.api: DataQueryApi = create_api(DataQueryApi)

    def tearDown(self) -> None:
        pass

    def test_aggregate(self) -> None:
        """Test case for aggregate

        Query aggregate data
        """

        query_content = get_query_content('aggregate.json')
        aggregate_query_dto = DataservicesQueryAggregationQueryExecutionDTO.from_json(query_content)
        cell_set_dto = self.api.aggregate(aggregate_query_dto)

        self.assertIsNotNone(cell_set_dto)
        self.assertGreater(len(cell_set_dto.axes), 0)
        self.assertGreater(len(cell_set_dto.cells), 0)

    def test_list(self) -> None:
        """Test case for list

        Query a list of details
        """

        query_content = get_query_content('list.json')
        list_query_dto = DataservicesQueryListQueryExecutionDTO.from_json(query_content)
        list_response_dto = self.api.list(list_query_dto)

        self.assertIsNotNone(list_response_dto)
        self.assertEqual(len(list_response_dto.rows), list_query_dto.options.limit)

    def test_query_snapshot(self) -> None:
        """Test case for query_snapshot

        Query a series of detailed snapshots
        """

        query_content = get_query_content('snapshot.json')
        snapshot_query_dto = DataservicesQuerySnapshotQueryExecutionDTO.from_json(query_content)
        response_dto = self.api.query_snapshot(snapshot_query_dto)

        self.assertIsNotNone(response_dto)
        self.assertEqual(len(response_dto.rows), snapshot_query_dto.options.limit)

    def test_sql_like_cell_set(self) -> None:
        """Test case for sql_like

        Should return CellSetDTO
        """

        sqlike_query_dto = DataservicesQuerySqlLikeQueryExecutionDTO(
            query='SELECT employeeCount() AS "Headcount", Union_Status FROM Employee'
        )
        sqlike_response_dto = self.api.sql_like(sqlike_query_dto)
        self.assertIsNotNone(sqlike_response_dto)
        self.assertIsNotNone(sqlike_response_dto.actual_instance)
        self.assertIsInstance(sqlike_response_dto.actual_instance, DataservicesQueryCellSetDTO)

    def test_sql_like(self) -> None:
        """Test case for sql_like

        Should return TableResponseDTO
        """

        sqlike_query_dto = DataservicesQuerySqlLikeQueryExecutionDTO(
            query="SELECT EmployeeID, First_Name, Last_Name FROM Employee WHERE isFemale=TRUE "
                  "AND Visier_Time BETWEEN date('2021-01-01') AND date('2022-01-01')"
        )
        sqlike_response_dto = self.api.sql_like(sqlike_query_dto)
        self.assertIsNotNone(sqlike_response_dto)
        self.assertIsNotNone(sqlike_response_dto.actual_instance)
        self.assertIsInstance(sqlike_response_dto.actual_instance, TableResponseDTO)


if __name__ == '__main__':
    unittest.main()
