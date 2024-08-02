# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1429
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.analytic_model.models.plan_parameter_definition_dto import PlanParameterDefinitionDTO

class TestPlanParameterDefinitionDTO(unittest.TestCase):
    """PlanParameterDefinitionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanParameterDefinitionDTO:
        """Test PlanParameterDefinitionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlanParameterDefinitionDTO`
        """
        model = PlanParameterDefinitionDTO()
        if include_optional:
            return PlanParameterDefinitionDTO(
                description = '',
                display_name = '',
                id = '',
                model_name = ''
            )
        else:
            return PlanParameterDefinitionDTO(
        )
        """

    def testPlanParameterDefinitionDTO(self):
        """Test PlanParameterDefinitionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
