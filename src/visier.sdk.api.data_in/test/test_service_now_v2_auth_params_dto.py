# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1443
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.service_now_v2_auth_params_dto import ServiceNowV2AuthParamsDTO

class TestServiceNowV2AuthParamsDTO(unittest.TestCase):
    """ServiceNowV2AuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceNowV2AuthParamsDTO:
        """Test ServiceNowV2AuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceNowV2AuthParamsDTO`
        """
        model = ServiceNowV2AuthParamsDTO()
        if include_optional:
            return ServiceNowV2AuthParamsDTO(
                alternate_domain = '',
                auth_code = '',
                client_id = '',
                client_secret = '',
                host_domain_name = ''
            )
        else:
            return ServiceNowV2AuthParamsDTO(
        )
        """

    def testServiceNowV2AuthParamsDTO(self):
        """Test ServiceNowV2AuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
