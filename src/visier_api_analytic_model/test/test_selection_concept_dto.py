# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.99201.1474
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.selection_concept_dto import SelectionConceptDTO

class TestSelectionConceptDTO(unittest.TestCase):
    """SelectionConceptDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SelectionConceptDTO:
        """Test SelectionConceptDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SelectionConceptDTO`
        """
        model = SelectionConceptDTO()
        if include_optional:
            return SelectionConceptDTO(
                description = '',
                display_name = '',
                id = '',
                tags = [
                    visier_api_analytic_model.models.tag_map_element_dto.TagMapElementDTO(
                        display_name = '', 
                        id = '', )
                    ],
                visible_in_app = True
            )
        else:
            return SelectionConceptDTO(
        )
        """

    def testSelectionConceptDTO(self):
        """Test SelectionConceptDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
