# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.99201.1475
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.numeric_parameter_definition_dto import NumericParameterDefinitionDTO

class TestNumericParameterDefinitionDTO(unittest.TestCase):
    """NumericParameterDefinitionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NumericParameterDefinitionDTO:
        """Test NumericParameterDefinitionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NumericParameterDefinitionDTO`
        """
        model = NumericParameterDefinitionDTO()
        if include_optional:
            return NumericParameterDefinitionDTO(
                default = 1.337,
                description = '',
                display_name = '',
                id = '',
                lower_bound = 1.337,
                upper_bound = 1.337
            )
        else:
            return NumericParameterDefinitionDTO(
        )
        """

    def testNumericParameterDefinitionDTO(self):
        """Test NumericParameterDefinitionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
