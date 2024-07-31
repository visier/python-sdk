# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.aggregation_type_parameter_value_dto import AggregationTypeParameterValueDTO

class TestAggregationTypeParameterValueDTO(unittest.TestCase):
    """AggregationTypeParameterValueDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AggregationTypeParameterValueDTO:
        """Test AggregationTypeParameterValueDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AggregationTypeParameterValueDTO`
        """
        model = AggregationTypeParameterValueDTO()
        if include_optional:
            return AggregationTypeParameterValueDTO(
                aggregation_option_id = '',
                parameter_id = ''
            )
        else:
            return AggregationTypeParameterValueDTO(
        )
        """

    def testAggregationTypeParameterValueDTO(self):
        """Test AggregationTypeParameterValueDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
