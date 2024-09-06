# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.selection_concepts_dto import SelectionConceptsDTO

class TestSelectionConceptsDTO(unittest.TestCase):
    """SelectionConceptsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SelectionConceptsDTO:
        """Test SelectionConceptsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SelectionConceptsDTO`
        """
        model = SelectionConceptsDTO()
        if include_optional:
            return SelectionConceptsDTO(
                selection_concepts = [
                    visier_api_analytic_model.models.selection_concept_dto.SelectionConceptDTO(
                        description = '', 
                        display_name = '', 
                        id = '', 
                        tags = [
                            visier_api_analytic_model.models.tag_map_element_dto.TagMapElementDTO(
                                display_name = '', 
                                id = '', )
                            ], 
                        visible_in_app = True, )
                    ]
            )
        else:
            return SelectionConceptsDTO(
        )
        """

    def testSelectionConceptsDTO(self):
        """Test SelectionConceptsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()