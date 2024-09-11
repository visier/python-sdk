# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.99201.1474
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_out.models.list_response import ListResponse

class TestListResponse(unittest.TestCase):
    """ListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListResponse:
        """Test ListResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListResponse`
        """
        model = ListResponse()
        if include_optional:
            return ListResponse(
                header = { },
                rows = [
                    { }
                    ]
            )
        else:
            return ListResponse(
        )
        """

    def testListResponse(self):
        """Test ListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
