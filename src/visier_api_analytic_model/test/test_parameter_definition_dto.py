# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.parameter_definition_dto import ParameterDefinitionDTO

class TestParameterDefinitionDTO(unittest.TestCase):
    """ParameterDefinitionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ParameterDefinitionDTO:
        """Test ParameterDefinitionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParameterDefinitionDTO`
        """
        model = ParameterDefinitionDTO()
        if include_optional:
            return ParameterDefinitionDTO(
                aggregation_type_parameter = visier_api_analytic_model.models.aggregation_type_parameter_dto.AggregationTypeParameterDTO(
                    description = '', 
                    display_name = '', 
                    id = '', 
                    parameter_options = [
                        visier_api_analytic_model.models.aggregation_type_option_dto.AggregationTypeOptionDTO(
                            aggregation_function = '', 
                            display_name = '', 
                            id = '', 
                            is_default = True, 
                            property_name = '', )
                        ], ),
                member_parameter = visier_api_analytic_model.models.member_parameter_definition_dto.MemberParameterDefinitionDTO(
                    default = null, 
                    description = '', 
                    dimension_id = '', 
                    display_name = '', 
                    id = '', 
                    reference_path = [
                        ''
                        ], ),
                numeric_parameter = visier_api_analytic_model.models.numeric_parameter_definition_dto.NumericParameterDefinitionDTO(
                    default = 1.337, 
                    description = '', 
                    display_name = '', 
                    id = '', 
                    lower_bound = 1.337, 
                    upper_bound = 1.337, ),
                plan_parameter = visier_api_analytic_model.models.plan_parameter_definition_dto.PlanParameterDefinitionDTO(
                    description = '', 
                    display_name = '', 
                    id = '', 
                    model_name = '', )
            )
        else:
            return ParameterDefinitionDTO(
        )
        """

    def testParameterDefinitionDTO(self):
        """Test ParameterDefinitionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
