# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1905
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.dataservices_query_aggregation_query_execution_dto import DataservicesQueryAggregationQueryExecutionDTO

class TestDataservicesQueryAggregationQueryExecutionDTO(unittest.TestCase):
    """DataservicesQueryAggregationQueryExecutionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesQueryAggregationQueryExecutionDTO:
        """Test DataservicesQueryAggregationQueryExecutionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesQueryAggregationQueryExecutionDTO(
                query = visier_api_data_out.models.dataservices/query/aggregation_query_dto.dataservices.query.AggregationQueryDTO(
                    source = None, 
                    filters = [
                        visier_api_data_out.models.dataservices/query/query_filter_dto.dataservices.query.QueryFilterDTO(
                            formula = '', 
                            selection_concept = None, 
                            member_set = None, 
                            cohort = None, )
                        ], 
                    axes = [
                        visier_api_data_out.models.dataservices/query/query_axis_dto.dataservices.query.QueryAxisDTO(
                            formula = '', 
                            selection_concept = None, 
                            dimension_member_selection = None, 
                            member_map_selection = None, 
                            numeric_ranges = None, 
                            dimension_level_selection = None, 
                            dimension_leaf_member_selection = None, 
                            dimension_data_member_selection = None, 
                            dimension_level_with_uncategorized_value_selection = None, 
                            table_axis_options = None, )
                        ], 
                    time_intervals = None, 
                    parameter_values = [
                        visier_api_data_out.models.dataservices/query/query_parameter_value_dto.dataservices.query.QueryParameterValueDTO(
                            member_value = None, 
                            numeric_value = None, 
                            plan_value = None, 
                            aggregation_type_value = None, )
                        ], ),
                options = visier_api_data_out.models.dataservices/query/query_execution_options_dto.dataservices.query.QueryExecutionOptionsDTO(
                    calendar_type = 'TENANT_CALENDAR', 
                    currency_conversion_mode = 'TENANT_CURRENCY_CONVERSION', 
                    currency_conversion_date = '', 
                    lineage_depth = 56, 
                    zero_visibility = 'SHOW', 
                    null_visibility = 'SHOW', 
                    cell_distribution_options = visier_api_data_out.models.dataservices/query/cell_distribution_options_dto.dataservices.query.CellDistributionOptionsDTO(
                        bin_count = 56, ), 
                    axis_visibility = 'SIMPLE', 
                    enable_sparse_results = True, 
                    internal = visier_api_data_out.models.dataservices/query/internal_query_execution_options_dto.dataservices.query.InternalQueryExecutionOptionsDTO(
                        sparse_handling_mode = 'ALLOW', 
                        align_time_axis_to_period_end = True, ), 
                    enable_descending_space = True, 
                    currency_conversion_code = '', 
                    member_display_mode = 'DEFAULT', 
                    axes_overall_value_mode = 'NONE', )
            )
        else:
            return DataservicesQueryAggregationQueryExecutionDTO(
        )

    def testDataservicesQueryAggregationQueryExecutionDTO(self):
        """Test DataservicesQueryAggregationQueryExecutionDTO"""
        def validate_instance(instance):
            DataservicesQueryAggregationQueryExecutionDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesQueryAggregationQueryExecutionDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
