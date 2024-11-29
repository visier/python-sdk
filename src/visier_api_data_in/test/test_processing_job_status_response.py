# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1614
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_in.models
from visier_api_data_in.models.processing_job_status_response import ProcessingJobStatusResponse

class TestProcessingJobStatusResponse(unittest.TestCase):
    """ProcessingJobStatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProcessingJobStatusResponse:
        """Test ProcessingJobStatusResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ProcessingJobStatusResponse(
                limit = 56,
                parent_job_id = '',
                parent_tenant_code = '',
                processing_jobs = [
                    visier_api_data_in.models.processing_job.ProcessingJob(
                        data_version = '', 
                        job_id = '', 
                        message = '', 
                        status = '', 
                        tenant_code = '', )
                    ],
                start = 56
            )
        else:
            return ProcessingJobStatusResponse(
        )

    def testProcessingJobStatusResponse(self):
        """Test ProcessingJobStatusResponse"""
        def validate_instance(instance):
            ProcessingJobStatusResponse.model_validate(inst_req_only)
            instance_deserialized = ProcessingJobStatusResponse.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
