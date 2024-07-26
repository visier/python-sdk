# coding: utf-8

"""
    Visier Document Search API

    Visier API for searching for Visier documents

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.document_search.models.simple_document_header_search_result_dto import SimpleDocumentHeaderSearchResultDTO

class TestSimpleDocumentHeaderSearchResultDTO(unittest.TestCase):
    """SimpleDocumentHeaderSearchResultDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimpleDocumentHeaderSearchResultDTO:
        """Test SimpleDocumentHeaderSearchResultDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimpleDocumentHeaderSearchResultDTO`
        """
        model = SimpleDocumentHeaderSearchResultDTO()
        if include_optional:
            return SimpleDocumentHeaderSearchResultDTO(
                description = '',
                display_name = '',
                relevance = 1.337,
                view_link = visier.sdk.api.document_search.models.document_search_link_dto.DocumentSearchLinkDTO(
                    href = '', 
                    verb = '', )
            )
        else:
            return SimpleDocumentHeaderSearchResultDTO(
        )
        """

    def testSimpleDocumentHeaderSearchResultDTO(self):
        """Test SimpleDocumentHeaderSearchResultDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
