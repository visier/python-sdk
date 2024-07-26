# coding: utf-8

"""
    Visier Data and Job Handling APIs

    Visier APIs for data and job handling

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_handling.models.microsoft365_auth_params_dto import Microsoft365AuthParamsDTO

class TestMicrosoft365AuthParamsDTO(unittest.TestCase):
    """Microsoft365AuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Microsoft365AuthParamsDTO:
        """Test Microsoft365AuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Microsoft365AuthParamsDTO`
        """
        model = Microsoft365AuthParamsDTO()
        if include_optional:
            return Microsoft365AuthParamsDTO(
                client_id = '',
                client_secret = '',
                o_auth_tenant_id = ''
            )
        else:
            return Microsoft365AuthParamsDTO(
        )
        """

    def testMicrosoft365AuthParamsDTO(self):
        """Test Microsoft365AuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
