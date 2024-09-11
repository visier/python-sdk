# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.99201.1476
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.property_dto import PropertyDTO

class TestPropertyDTO(unittest.TestCase):
    """PropertyDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PropertyDTO:
        """Test PropertyDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PropertyDTO`
        """
        model = PropertyDTO()
        if include_optional:
            return PropertyDTO(
                data_type = '',
                description = '',
                display_name = '',
                id = '',
                parameters = [
                    visier_api_analytic_model.models.parameter_definition_dto.ParameterDefinitionDTO(
                        aggregation_type_parameter = null, 
                        member_parameter = null, 
                        numeric_parameter = null, 
                        plan_parameter = null, )
                    ],
                primitive_data_type = '',
                tags = [
                    visier_api_analytic_model.models.tag_map_element_dto.TagMapElementDTO(
                        display_name = '', 
                        id = '', )
                    ]
            )
        else:
            return PropertyDTO(
        )
        """

    def testPropertyDTO(self):
        """Test PropertyDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
