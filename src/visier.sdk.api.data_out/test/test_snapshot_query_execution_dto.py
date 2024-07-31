# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.snapshot_query_execution_dto import SnapshotQueryExecutionDTO

class TestSnapshotQueryExecutionDTO(unittest.TestCase):
    """SnapshotQueryExecutionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnapshotQueryExecutionDTO:
        """Test SnapshotQueryExecutionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SnapshotQueryExecutionDTO`
        """
        model = SnapshotQueryExecutionDTO()
        if include_optional:
            return SnapshotQueryExecutionDTO(
                columns = [
                    visier.sdk.api.data_out.models.property_column_dto.PropertyColumnDTO(
                        column_definition = null, 
                        column_name = '', )
                    ],
                filters = [
                    visier.sdk.api.data_out.models.query_filter_dto.QueryFilterDTO(
                        cohort = null, 
                        formula = '', 
                        member_set = null, 
                        selection_concept = null, )
                    ],
                options = visier.sdk.api.data_out.models.snapshot_query_execution_options_dto.SnapshotQueryExecutionOptionsDTO(
                    calendar_type = 'TENANT_CALENDAR', 
                    currency_conversion_code = '', 
                    currency_conversion_date = '', 
                    date_time_display_mode = 'EPOCH', 
                    limit = 56, 
                    multiple_tables = True, 
                    omit_header = True, 
                    page = 56, 
                    query_mode = 'DEFAULT', ),
                parameter_values = [
                    visier.sdk.api.data_out.models.query_parameter_value_dto.QueryParameterValueDTO(
                        aggregation_type_value = null, 
                        member_value = null, 
                        numeric_value = null, 
                        plan_value = null, )
                    ],
                sort_options = [
                    visier.sdk.api.data_out.models.sort_option_dto.SortOptionDTO(
                        column_index = 56, 
                        sort_direction = 'SORT_ASCENDING', )
                    ],
                source = visier.sdk.api.data_out.models.list_query_source_dto.ListQuerySourceDTO(
                    analytic_object = '', 
                    formula = '', 
                    metric = '', ),
                time_intervals = visier.sdk.api.data_out.models.query_time_intervals_dto.QueryTimeIntervalsDTO(
                    direction = 'BACKWARD', 
                    dynamic_date_from = '', 
                    from_date_time = '', 
                    from_instant = '', 
                    interval_count = 56, 
                    interval_period_count = 56, 
                    interval_period_type = 'MONTH', 
                    shift = null, 
                    trailing_period_count = 56, 
                    trailing_period_type = 'MONTH', )
            )
        else:
            return SnapshotQueryExecutionDTO(
        )
        """

    def testSnapshotQueryExecutionDTO(self):
        """Test SnapshotQueryExecutionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
