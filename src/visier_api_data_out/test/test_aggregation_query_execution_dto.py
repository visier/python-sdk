# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1481
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_out.models.aggregation_query_execution_dto import AggregationQueryExecutionDTO

class TestAggregationQueryExecutionDTO(unittest.TestCase):
    """AggregationQueryExecutionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AggregationQueryExecutionDTO:
        """Test AggregationQueryExecutionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AggregationQueryExecutionDTO`
        """
        model = AggregationQueryExecutionDTO()
        if include_optional:
            return AggregationQueryExecutionDTO(
                options = visier_api_data_out.models.query_execution_options_dto.QueryExecutionOptionsDTO(
                    axis_visibility = 'SIMPLE', 
                    calendar_type = 'TENANT_CALENDAR', 
                    cell_distribution_options = visier_api_data_out.models.cell_distribution_options_dto.CellDistributionOptionsDTO(
                        bin_count = 56, ), 
                    currency_conversion_code = '', 
                    currency_conversion_date = '', 
                    currency_conversion_mode = 'TENANT_CURRENCY_CONVERSION', 
                    enable_descending_space = True, 
                    enable_sparse_results = True, 
                    internal = visier_api_data_out.models.internal_query_execution_options_dto.InternalQueryExecutionOptionsDTO(
                        align_time_axis_to_period_end = True, 
                        sparse_handling_mode = 'ALLOW', ), 
                    lineage_depth = 56, 
                    member_display_mode = 'DEFAULT', 
                    null_visibility = 'SHOW', 
                    zero_visibility = 'SHOW', ),
                query = visier_api_data_out.models.aggregation_query_dto.AggregationQueryDTO(
                    axes = [
                        visier_api_data_out.models.query_axis_dto.QueryAxisDTO(
                            dimension_data_member_selection = null, 
                            dimension_leaf_member_selection = null, 
                            dimension_level_selection = null, 
                            dimension_level_with_uncategorized_value_selection = null, 
                            dimension_member_selection = null, 
                            formula = '', 
                            member_map_selection = null, 
                            numeric_ranges = null, 
                            selection_concept = null, 
                            table_axis_options = null, )
                        ], 
                    filters = [
                        visier_api_data_out.models.query_filter_dto.QueryFilterDTO(
                            cohort = null, 
                            formula = '', 
                            member_set = null, 
                            selection_concept = null, )
                        ], 
                    parameter_values = [
                        visier_api_data_out.models.query_parameter_value_dto.QueryParameterValueDTO(
                            aggregation_type_value = null, 
                            member_value = null, 
                            numeric_value = null, 
                            plan_value = null, )
                        ], 
                    source = null, 
                    time_intervals = null, )
            )
        else:
            return AggregationQueryExecutionDTO(
        )
        """

    def testAggregationQueryExecutionDTO(self):
        """Test AggregationQueryExecutionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
