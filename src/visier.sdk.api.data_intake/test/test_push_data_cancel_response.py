# coding: utf-8

"""
    Visier Data Intake APIs

    Visier APIs for sending raw or untransformed source data to Visier

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_intake.models.push_data_cancel_response import PushDataCancelResponse

class TestPushDataCancelResponse(unittest.TestCase):
    """PushDataCancelResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PushDataCancelResponse:
        """Test PushDataCancelResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PushDataCancelResponse`
        """
        model = PushDataCancelResponse()
        if include_optional:
            return PushDataCancelResponse(
                data_transfer_result_details = [
                    visier.sdk.api.data_intake.models.data_transfer_result_detail.DataTransferResultDetail(
                        data_size = '', 
                        rows = '', 
                        source_names = [
                            ''
                            ], 
                        tenant_code = '', )
                    ],
                message = '',
                status = '',
                transfer_session_id = ''
            )
        else:
            return PushDataCancelResponse(
        )
        """

    def testPushDataCancelResponse(self):
        """Test PushDataCancelResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
