# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.analytic_model.models.aggregation_type_parameter_dto import AggregationTypeParameterDTO

class TestAggregationTypeParameterDTO(unittest.TestCase):
    """AggregationTypeParameterDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AggregationTypeParameterDTO:
        """Test AggregationTypeParameterDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AggregationTypeParameterDTO`
        """
        model = AggregationTypeParameterDTO()
        if include_optional:
            return AggregationTypeParameterDTO(
                id = '',
                display_name = '',
                description = '',
                parameter_options = [
                    visier.sdk.api.analytic_model.models.aggregation_type_option_dto.AggregationTypeOptionDTO(
                        id = '', 
                        display_name = '', 
                        property_name = '', 
                        aggregation_function = '', 
                        is_default = True, )
                    ]
            )
        else:
            return AggregationTypeParameterDTO(
        )
        """

    def testAggregationTypeParameterDTO(self):
        """Test AggregationTypeParameterDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
