# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.push_data_response import PushDataResponse

class TestPushDataResponse(unittest.TestCase):
    """PushDataResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PushDataResponse:
        """Test PushDataResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PushDataResponse`
        """
        model = PushDataResponse()
        if include_optional:
            return PushDataResponse(
                transfer_session_id = '',
                sequence = 56,
                status = '',
                message = '',
                tenants = [
                    visier.sdk.api.data_in.models.tenant.Tenant(
                        tenant_code = '', 
                        status = '', 
                        sources = [
                            visier.sdk.api.data_in.models.source.Source(
                                source_id = '', 
                                source_name = '', 
                                data_size = '', 
                                rows = '', 
                                status = '', 
                                message = '', )
                            ], )
                    ]
            )
        else:
            return PushDataResponse(
        )
        """

    def testPushDataResponse(self):
        """Test PushDataResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
