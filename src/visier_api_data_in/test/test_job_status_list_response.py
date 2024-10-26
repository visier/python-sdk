# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1547
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_in.models
from visier_api_data_in.models.job_status_list_response import JobStatusListResponse

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

        if include_optional:
            return JobStatusListResponse(
                job_status = [
                    visier_api_data_in.models.job_status_with_start_time.JobStatusWithStartTime(
                        job_id = '', 
                        job_type = '', 
                        start_time = '', 
                        status = '', 
                        tenant = '', )
                    ],
                query_end_time = '',
                query_start_time = ''
            )
        else:
            return JobStatusListResponse(
        )

    def testJobStatusListResponse(self):
        """Test JobStatusListResponse"""
        def validate_instance(instance):
            JobStatusListResponse.model_validate(inst_req_only)
            instance_deserialized = JobStatusListResponse.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
