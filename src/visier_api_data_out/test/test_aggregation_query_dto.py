# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1482
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_out.models.aggregation_query_dto import AggregationQueryDTO

class TestAggregationQueryDTO(unittest.TestCase):
    """AggregationQueryDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AggregationQueryDTO:
        """Test AggregationQueryDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AggregationQueryDTO`
        """
        model = AggregationQueryDTO()
        if include_optional:
            return AggregationQueryDTO(
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
                source = visier_api_data_out.models.aggregation_query_source_dto.AggregationQuerySourceDTO(
                    formula = '', 
                    metric = '', 
                    metrics = null, ),
                time_intervals = visier_api_data_out.models.query_time_intervals_dto.QueryTimeIntervalsDTO(
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
            return AggregationQueryDTO(
        )
        """

    def testAggregationQueryDTO(self):
        """Test AggregationQueryDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
