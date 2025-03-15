# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.dataservices_query_transfers_aggregation_query_dto import DataservicesQueryTransfersAggregationQueryDTO

class TestDataservicesQueryTransfersAggregationQueryDTO(unittest.TestCase):
    """DataservicesQueryTransfersAggregationQueryDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesQueryTransfersAggregationQueryDTO:
        """Test DataservicesQueryTransfersAggregationQueryDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesQueryTransfersAggregationQueryDTO(
                axes = [
                    visier_api_data_out.models.dataservices/query/transfers/query_axis_dto.dataservices.query.transfers.QueryAxisDTO(
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
                    visier_api_data_out.models.dataservices/query/transfers/query_filter_dto.dataservices.query.transfers.QueryFilterDTO(
                        cohort = None, 
                        formula = '', 
                        member_set = None, 
                        selection_concept = None, )
                    ],
                parameter_values = [
                    visier_api_data_out.models.dataservices/query/transfers/query_parameter_value_dto.dataservices.query.transfers.QueryParameterValueDTO(
                        aggregation_type_value = None, 
                        member_value = None, 
                        numeric_value = None, 
                        plan_value = None, )
                    ],
                source = visier_api_data_out.models.dataservices/query/transfers/aggregation_query_source_dto.dataservices.query.transfers.AggregationQuerySourceDTO(
                    formula = '', 
                    metric = '', 
                    metrics = None, ),
                time_intervals = visier_api_data_out.models.dataservices/query/transfers/query_time_intervals_dto.dataservices.query.transfers.QueryTimeIntervalsDTO(
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
            return DataservicesQueryTransfersAggregationQueryDTO(
        )

    def testDataservicesQueryTransfersAggregationQueryDTO(self):
        """Test DataservicesQueryTransfersAggregationQueryDTO"""
        def validate_instance(instance):
            DataservicesQueryTransfersAggregationQueryDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesQueryTransfersAggregationQueryDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
