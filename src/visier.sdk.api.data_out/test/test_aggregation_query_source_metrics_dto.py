# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.aggregation_query_source_metrics_dto import AggregationQuerySourceMetricsDTO

class TestAggregationQuerySourceMetricsDTO(unittest.TestCase):
    """AggregationQuerySourceMetricsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AggregationQuerySourceMetricsDTO:
        """Test AggregationQuerySourceMetricsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AggregationQuerySourceMetricsDTO`
        """
        model = AggregationQuerySourceMetricsDTO()
        if include_optional:
            return AggregationQuerySourceMetricsDTO(
                columns = [
                    visier.sdk.api.data_out.models.aggregation_query_source_metric_dto.AggregationQuerySourceMetricDTO(
                        column_name = '', 
                        formula = '', 
                        id = '', 
                        qualifying_path = '', )
                    ]
            )
        else:
            return AggregationQuerySourceMetricsDTO(
        )
        """

    def testAggregationQuerySourceMetricsDTO(self):
        """Test AggregationQuerySourceMetricsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
