# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1772
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
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

    def testNumericParameterDefinitionDTO(self):
        """Test NumericParameterDefinitionDTO"""
        def validate_instance(instance):
            NumericParameterDefinitionDTO.model_validate(inst_req_only)
            instance_deserialized = NumericParameterDefinitionDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
