# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.99201.1476
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.concept_configuration_result_dto import ConceptConfigurationResultDTO

class TestConceptConfigurationResultDTO(unittest.TestCase):
    """ConceptConfigurationResultDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConceptConfigurationResultDTO:
        """Test ConceptConfigurationResultDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConceptConfigurationResultDTO`
        """
        model = ConceptConfigurationResultDTO()
        if include_optional:
            return ConceptConfigurationResultDTO(
                concept_id = '',
                message = '',
                project_id = ''
            )
        else:
            return ConceptConfigurationResultDTO(
        )
        """

    def testConceptConfigurationResultDTO(self):
        """Test ConceptConfigurationResultDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
