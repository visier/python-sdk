# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_in.models
from visier_api_data_in.models.data_in_receiving_job_and_status_response import DataInReceivingJobAndStatusResponse

class TestDataInReceivingJobAndStatusResponse(unittest.TestCase):
    """DataInReceivingJobAndStatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataInReceivingJobAndStatusResponse:
        """Test DataInReceivingJobAndStatusResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataInReceivingJobAndStatusResponse(
                limit = 56,
                parent_job_id = '',
                parent_tenant_code = '',
                receiving_jobs = [
                    visier_api_data_in.models.data_in/receiving_job.data_in.ReceivingJob(
                        receiving_job_id = '', 
                        status = '', 
                        tenant_code = '', )
                    ],
                start = 56
            )
        else:
            return DataInReceivingJobAndStatusResponse(
        )

    def testDataInReceivingJobAndStatusResponse(self):
        """Test DataInReceivingJobAndStatusResponse"""
        def validate_instance(instance):
            DataInReceivingJobAndStatusResponse.model_validate(inst_req_only)
            instance_deserialized = DataInReceivingJobAndStatusResponse.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
