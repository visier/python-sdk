# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.simple_document_header_search_response_dto import SimpleDocumentHeaderSearchResponseDTO

class TestSimpleDocumentHeaderSearchResponseDTO(unittest.TestCase):
    """SimpleDocumentHeaderSearchResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimpleDocumentHeaderSearchResponseDTO:
        """Test SimpleDocumentHeaderSearchResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimpleDocumentHeaderSearchResponseDTO`
        """
        model = SimpleDocumentHeaderSearchResponseDTO()
        if include_optional:
            return SimpleDocumentHeaderSearchResponseDTO(
                document_headers = [
                    visier.sdk.api.data_out.models.simple_document_header_search_result_dto.SimpleDocumentHeaderSearchResultDTO(
                        description = '', 
                        display_name = '', 
                        relevance = 1.337, 
                        view_link = null, )
                    ]
            )
        else:
            return SimpleDocumentHeaderSearchResponseDTO(
        )
        """

    def testSimpleDocumentHeaderSearchResponseDTO(self):
        """Test SimpleDocumentHeaderSearchResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
