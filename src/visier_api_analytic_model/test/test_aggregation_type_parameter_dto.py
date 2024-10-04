# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1508
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.aggregation_type_parameter_dto import AggregationTypeParameterDTO

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

        if include_optional:
            return AggregationTypeParameterDTO(
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
                    ]
            )
        else:
            return AggregationTypeParameterDTO(
        )

    def testAggregationTypeParameterDTO(self):
        """Test AggregationTypeParameterDTO"""
        def validate_instance(instance):
            AggregationTypeParameterDTO.model_validate(inst_req_only)
            instance_deserialized = AggregationTypeParameterDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
