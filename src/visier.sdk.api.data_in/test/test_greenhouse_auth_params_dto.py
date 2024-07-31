# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.greenhouse_auth_params_dto import GreenhouseAuthParamsDTO

class TestGreenhouseAuthParamsDTO(unittest.TestCase):
    """GreenhouseAuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GreenhouseAuthParamsDTO:
        """Test GreenhouseAuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GreenhouseAuthParamsDTO`
        """
        model = GreenhouseAuthParamsDTO()
        if include_optional:
            return GreenhouseAuthParamsDTO(
                api_key = ''
            )
        else:
            return GreenhouseAuthParamsDTO(
        )
        """

    def testGreenhouseAuthParamsDTO(self):
        """Test GreenhouseAuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
