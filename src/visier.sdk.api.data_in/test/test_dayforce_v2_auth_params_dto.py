# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.dayforce_v2_auth_params_dto import DayforceV2AuthParamsDTO

class TestDayforceV2AuthParamsDTO(unittest.TestCase):
    """DayforceV2AuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DayforceV2AuthParamsDTO:
        """Test DayforceV2AuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DayforceV2AuthParamsDTO`
        """
        model = DayforceV2AuthParamsDTO()
        if include_optional:
            return DayforceV2AuthParamsDTO(
                company_id = '',
                host_domain_name = '',
                password = '',
                token_host = '',
                username = ''
            )
        else:
            return DayforceV2AuthParamsDTO(
        )
        """

    def testDayforceV2AuthParamsDTO(self):
        """Test DayforceV2AuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
