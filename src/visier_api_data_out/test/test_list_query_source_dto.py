# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1482
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_out.models.list_query_source_dto import ListQuerySourceDTO

class TestListQuerySourceDTO(unittest.TestCase):
    """ListQuerySourceDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListQuerySourceDTO:
        """Test ListQuerySourceDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListQuerySourceDTO`
        """
        model = ListQuerySourceDTO()
        if include_optional:
            return ListQuerySourceDTO(
                analytic_object = '',
                formula = '',
                metric = ''
            )
        else:
            return ListQuerySourceDTO(
        )
        """

    def testListQuerySourceDTO(self):
        """Test ListQuerySourceDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
