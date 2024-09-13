# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1481
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.aggregation_type_option_dto import AggregationTypeOptionDTO

class TestAggregationTypeOptionDTO(unittest.TestCase):
    """AggregationTypeOptionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AggregationTypeOptionDTO:
        """Test AggregationTypeOptionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AggregationTypeOptionDTO`
        """
        model = AggregationTypeOptionDTO()
        if include_optional:
            return AggregationTypeOptionDTO(
                aggregation_function = '',
                display_name = '',
                id = '',
                is_default = True,
                property_name = ''
            )
        else:
            return AggregationTypeOptionDTO(
        )
        """

    def testAggregationTypeOptionDTO(self):
        """Test AggregationTypeOptionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
