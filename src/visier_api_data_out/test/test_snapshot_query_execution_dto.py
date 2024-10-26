# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1547
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.snapshot_query_execution_dto import SnapshotQueryExecutionDTO

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

        if include_optional:
            return SnapshotQueryExecutionDTO(
                columns = [
                    visier_api_data_out.models.property_column_dto.PropertyColumnDTO(
                        column_definition = None, 
                        column_name = '', )
                    ],
                filters = [
                    visier_api_data_out.models.query_filter_dto.QueryFilterDTO(
                        cohort = None, 
                        formula = '', 
                        member_set = None, 
                        selection_concept = None, )
                    ],
                options = visier_api_data_out.models.snapshot_query_execution_options_dto.SnapshotQueryExecutionOptionsDTO(
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
                    visier_api_data_out.models.query_parameter_value_dto.QueryParameterValueDTO(
                        aggregation_type_value = None, 
                        member_value = None, 
                        numeric_value = None, 
                        plan_value = None, )
                    ],
                sort_options = [
                    visier_api_data_out.models.sort_option_dto.SortOptionDTO(
                        column_index = 56, 
                        sort_direction = 'SORT_ASCENDING', )
                    ],
                source = visier_api_data_out.models.list_query_source_dto.ListQuerySourceDTO(
                    analytic_object = '', 
                    formula = '', 
                    metric = '', ),
                time_intervals = visier_api_data_out.models.query_time_intervals_dto.QueryTimeIntervalsDTO(
                    direction = 'BACKWARD', 
                    dynamic_date_from = '', 
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
            return SnapshotQueryExecutionDTO(
        )

    def testSnapshotQueryExecutionDTO(self):
        """Test SnapshotQueryExecutionDTO"""
        def validate_instance(instance):
            SnapshotQueryExecutionDTO.model_validate(inst_req_only)
            instance_deserialized = SnapshotQueryExecutionDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
