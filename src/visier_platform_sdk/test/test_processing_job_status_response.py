# coding: utf-8

"""
    API Reference

    Detailed API reference documentation for Visier APIs. Includes all endpoints, headers, path parameters, query parameters, request body schema, response schema, JSON request samples, and JSON response samples.

    The version of the OpenAPI document: 22222222.99201.2050
    Contact: alpine@visier.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import visier_platform_sdk.models
from visier_platform_sdk.models.processing_job_status_response import ProcessingJobStatusResponse

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
                parent_job_id = '',
                parent_tenant_code = '',
                limit = 56,
                start = 56,
                processing_jobs = [
                    visier_platform_sdk.models.processing_job.ProcessingJob(
                        job_id = '', 
                        tenant_code = '', 
                        data_version = '', 
                        status = '', 
                        message = '', )
                    ]
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
