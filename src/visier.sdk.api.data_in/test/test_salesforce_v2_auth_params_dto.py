# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.salesforce_v2_auth_params_dto import SalesforceV2AuthParamsDTO

class TestSalesforceV2AuthParamsDTO(unittest.TestCase):
    """SalesforceV2AuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SalesforceV2AuthParamsDTO:
        """Test SalesforceV2AuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SalesforceV2AuthParamsDTO`
        """
        model = SalesforceV2AuthParamsDTO()
        if include_optional:
            return SalesforceV2AuthParamsDTO(
                auth_code = '',
                client_id = '',
                client_secret = '',
                login_host = ''
            )
        else:
            return SalesforceV2AuthParamsDTO(
        )
        """

    def testSalesforceV2AuthParamsDTO(self):
        """Test SalesforceV2AuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
