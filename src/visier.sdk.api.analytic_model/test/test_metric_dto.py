# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.analytic_model.models.metric_dto import MetricDTO

class TestMetricDTO(unittest.TestCase):
    """MetricDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetricDTO:
        """Test MetricDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetricDTO`
        """
        model = MetricDTO()
        if include_optional:
            return MetricDTO(
                analytic_object_id = '',
                category = 'REGULAR',
                data_end_date = '',
                data_start_date = '',
                description = '',
                display_name = '',
                id = '',
                parameters = [
                    visier.sdk.api.analytic_model.models.parameter_definition_dto.ParameterDefinitionDTO(
                        aggregation_type_parameter = null, 
                        member_parameter = null, 
                        numeric_parameter = null, 
                        plan_parameter = null, )
                    ],
                visible_in_app = True
            )
        else:
            return MetricDTO(
        )
        """

    def testMetricDTO(self):
        """Test MetricDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
