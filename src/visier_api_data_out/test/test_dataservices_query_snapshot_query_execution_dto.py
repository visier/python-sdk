# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1828
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.dataservices_query_snapshot_query_execution_dto import DataservicesQuerySnapshotQueryExecutionDTO

class TestDataservicesQuerySnapshotQueryExecutionDTO(unittest.TestCase):
    """DataservicesQuerySnapshotQueryExecutionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesQuerySnapshotQueryExecutionDTO:
        """Test DataservicesQuerySnapshotQueryExecutionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesQuerySnapshotQueryExecutionDTO(
                columns = [
                    visier_api_data_out.models.dataservices/query/property_column_dto.dataservices.query.PropertyColumnDTO(
                        column_definition = None, 
                        column_name = '', )
                    ],
                filters = [
                    visier_api_data_out.models.dataservices/query/query_filter_dto.dataservices.query.QueryFilterDTO(
                        cohort = None, 
                        formula = '', 
                        member_set = None, 
                        selection_concept = None, )
                    ],
                options = visier_api_data_out.models.dataservices/query/snapshot_query_execution_options_dto.dataservices.query.SnapshotQueryExecutionOptionsDTO(
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
                    visier_api_data_out.models.dataservices/query/query_parameter_value_dto.dataservices.query.QueryParameterValueDTO(
                        aggregation_type_value = None, 
                        member_value = None, 
                        numeric_value = None, 
                        plan_value = None, )
                    ],
                sort_options = [
                    visier_api_data_out.models.dataservices/query/sort_option_dto.dataservices.query.SortOptionDTO(
                        column_index = 56, 
                        sort_direction = 'SORT_ASCENDING', )
                    ],
                source = visier_api_data_out.models.dataservices/query/list_query_source_dto.dataservices.query.ListQuerySourceDTO(
                    analytic_object = '', 
                    formula = '', 
                    metric = '', 
                    text_concept = '', ),
                time_intervals = visier_api_data_out.models.dataservices/query/query_time_intervals_dto.dataservices.query.QueryTimeIntervalsDTO(
                    direction = 'BACKWARD', 
                    dynamic_date_from = 'SOURCE', 
                    from_date_time = '', 
                    from_instant = '', 
                    interval_count = 56, 
                    interval_period_count = 56, 
                    interval_period_type = 'MONTH', 
                    shift = None, 
                    trailing_period_count = 56, 
                    trailing_period_type = 'MONTH', )
            )
        else:
            return DataservicesQuerySnapshotQueryExecutionDTO(
        )

    def testDataservicesQuerySnapshotQueryExecutionDTO(self):
        """Test DataservicesQuerySnapshotQueryExecutionDTO"""
        def validate_instance(instance):
            DataservicesQuerySnapshotQueryExecutionDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesQuerySnapshotQueryExecutionDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
