# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1429
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.receiving_job_status_response import ReceivingJobStatusResponse

class TestReceivingJobStatusResponse(unittest.TestCase):
    """ReceivingJobStatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReceivingJobStatusResponse:
        """Test ReceivingJobStatusResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReceivingJobStatusResponse`
        """
        model = ReceivingJobStatusResponse()
        if include_optional:
            return ReceivingJobStatusResponse(
                job_id = '',
                parent_job_id = '',
                parent_tenant_code = '',
                receiving_jobs = [
                    visier.sdk.api.data_in.models.receiving_job.ReceivingJob(
                        receiving_job_id = '', 
                        status = '', 
                        tenant_code = '', )
                    ],
                status = ''
            )
        else:
            return ReceivingJobStatusResponse(
        )
        """

    def testReceivingJobStatusResponse(self):
        """Test ReceivingJobStatusResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
