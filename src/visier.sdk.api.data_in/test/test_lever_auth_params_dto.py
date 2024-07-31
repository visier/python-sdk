# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.lever_auth_params_dto import LeverAuthParamsDTO

class TestLeverAuthParamsDTO(unittest.TestCase):
    """LeverAuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeverAuthParamsDTO:
        """Test LeverAuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LeverAuthParamsDTO`
        """
        model = LeverAuthParamsDTO()
        if include_optional:
            return LeverAuthParamsDTO(
                api_key = ''
            )
        else:
            return LeverAuthParamsDTO(
        )
        """

    def testLeverAuthParamsDTO(self):
        """Test LeverAuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
