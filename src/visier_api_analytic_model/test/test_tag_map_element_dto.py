# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.99201.1474
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.tag_map_element_dto import TagMapElementDTO

class TestTagMapElementDTO(unittest.TestCase):
    """TagMapElementDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TagMapElementDTO:
        """Test TagMapElementDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TagMapElementDTO`
        """
        model = TagMapElementDTO()
        if include_optional:
            return TagMapElementDTO(
                display_name = '',
                id = ''
            )
        else:
            return TagMapElementDTO(
        )
        """

    def testTagMapElementDTO(self):
        """Test TagMapElementDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
