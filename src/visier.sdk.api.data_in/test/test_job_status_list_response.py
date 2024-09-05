# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.job_status_list_response import JobStatusListResponse

class TestJobStatusListResponse(unittest.TestCase):
    """JobStatusListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobStatusListResponse:
        """Test JobStatusListResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobStatusListResponse`
        """
        model = JobStatusListResponse()
        if include_optional:
            return JobStatusListResponse(
                query_start_time = '',
                query_end_time = '',
                job_status = [
                    visier.sdk.api.data_in.models.job_status_with_start_time.JobStatusWithStartTime(
                        job_id = '', 
                        tenant = '', 
                        status = '', 
                        job_type = '', 
                        start_time = '', )
                    ]
            )
        else:
            return JobStatusListResponse(
        )
        """

    def testJobStatusListResponse(self):
        """Test JobStatusListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
