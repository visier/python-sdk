# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1508
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_in.models
from visier_api_data_in.models.push_data_complete_response import PushDataCompleteResponse

class TestPushDataCompleteResponse(unittest.TestCase):
    """PushDataCompleteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PushDataCompleteResponse:
        """Test PushDataCompleteResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return PushDataCompleteResponse(
                data_receiving_job_id = '',
                data_transfer_result_details = [
                    visier_api_data_in.models.data_transfer_result_detail.DataTransferResultDetail(
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
            return PushDataCompleteResponse(
        )

    def testPushDataCompleteResponse(self):
        """Test PushDataCompleteResponse"""
        def validate_instance(instance):
            PushDataCompleteResponse.model_validate(inst_req_only)
            instance_deserialized = PushDataCompleteResponse.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
