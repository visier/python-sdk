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
                            dimension_data_member_selection = None, 
                            dimension_leaf_member_selection = None, 
                            dimension_level_selection = None, 
                            dimension_level_with_uncategorized_value_selection = None, 
                            dimension_member_selection = None, 
                            formula = '', 
                            member_map_selection = None, 
                            numeric_ranges = None, 
                            selection_concept = None, 
                            table_axis_options = None, )
                        ], 
                    filters = [
                        visier_api_data_out.models.query_filter_dto.QueryFilterDTO(
                            cohort = None, 
                            formula = '', 
                            member_set = None, 
                            selection_concept = None, )
                        ], 
                    parameter_values = [
                        visier_api_data_out.models.query_parameter_value_dto.QueryParameterValueDTO(
                            aggregation_type_value = None, 
                            member_value = None, 
                            numeric_value = None, 
                            plan_value = None, )
                        ], 
                    source = None, 
                    time_intervals = None, )
            )
        else:
            return AggregationQueryExecutionDTO(
        )

    def testAggregationQueryExecutionDTO(self):
        """Test AggregationQueryExecutionDTO"""
        def validate_instance(instance):
            AggregationQueryExecutionDTO.model_validate(inst_req_only)
            instance_deserialized = AggregationQueryExecutionDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
