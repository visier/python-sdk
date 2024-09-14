# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1482
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.willow_auth_params_dto import WillowAuthParamsDTO

class TestWillowAuthParamsDTO(unittest.TestCase):
    """WillowAuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WillowAuthParamsDTO:
        """Test WillowAuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WillowAuthParamsDTO`
        """
        model = WillowAuthParamsDTO()
        if include_optional:
            return WillowAuthParamsDTO(
                api_token = '',
                host_name = ''
            )
        else:
            return WillowAuthParamsDTO(
        )
        """

    def testWillowAuthParamsDTO(self):
        """Test WillowAuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
