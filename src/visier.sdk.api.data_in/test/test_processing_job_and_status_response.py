# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1429
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.processing_job_and_status_response import ProcessingJobAndStatusResponse

class TestProcessingJobAndStatusResponse(unittest.TestCase):
    """ProcessingJobAndStatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProcessingJobAndStatusResponse:
        """Test ProcessingJobAndStatusResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProcessingJobAndStatusResponse`
        """
        model = ProcessingJobAndStatusResponse()
        if include_optional:
            return ProcessingJobAndStatusResponse(
                limit = 56,
                parent_job_id = '',
                parent_tenant_code = '',
                processing_jobs = [
                    visier.sdk.api.data_in.models.processing_job.ProcessingJob(
                        data_version = '', 
                        job_id = '', 
                        message = '', 
                        status = '', 
                        tenant_code = '', )
                    ],
                start = 56
            )
        else:
            return ProcessingJobAndStatusResponse(
        )
        """

    def testProcessingJobAndStatusResponse(self):
        """Test ProcessingJobAndStatusResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
