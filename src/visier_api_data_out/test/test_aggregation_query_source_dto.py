# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1739
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.aggregation_query_source_dto import AggregationQuerySourceDTO

class TestAggregationQuerySourceDTO(unittest.TestCase):
    """AggregationQuerySourceDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AggregationQuerySourceDTO:
        """Test AggregationQuerySourceDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return AggregationQuerySourceDTO(
                formula = '',
                metric = '',
                metrics = visier_api_data_out.models.aggregation_query_source_metrics_dto.AggregationQuerySourceMetricsDTO(
                    columns = [
                        visier_api_data_out.models.aggregation_query_source_metric_dto.AggregationQuerySourceMetricDTO(
                            column_name = '', 
                            formula = '', 
                            id = '', 
                            qualifying_path = '', )
                        ], )
            )
        else:
            return AggregationQuerySourceDTO(
        )

    def testAggregationQuerySourceDTO(self):
        """Test AggregationQuerySourceDTO"""
        def validate_instance(instance):
            AggregationQuerySourceDTO.model_validate(inst_req_only)
            instance_deserialized = AggregationQuerySourceDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
