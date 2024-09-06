# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_out.models.snapshot_query_execution_options_dto import SnapshotQueryExecutionOptionsDTO

class TestSnapshotQueryExecutionOptionsDTO(unittest.TestCase):
    """SnapshotQueryExecutionOptionsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnapshotQueryExecutionOptionsDTO:
        """Test SnapshotQueryExecutionOptionsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SnapshotQueryExecutionOptionsDTO`
        """
        model = SnapshotQueryExecutionOptionsDTO()
        if include_optional:
            return SnapshotQueryExecutionOptionsDTO(
                calendar_type = 'TENANT_CALENDAR',
                currency_conversion_code = '',
                currency_conversion_date = '',
                date_time_display_mode = 'EPOCH',
                limit = 56,
                multiple_tables = True,
                omit_header = True,
                page = 56,
                query_mode = 'DEFAULT'
            )
        else:
            return SnapshotQueryExecutionOptionsDTO(
        )
        """

    def testSnapshotQueryExecutionOptionsDTO(self):
        """Test SnapshotQueryExecutionOptionsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
