# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1474
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.extraction_job_and_status_response import ExtractionJobAndStatusResponse

class TestExtractionJobAndStatusResponse(unittest.TestCase):
    """ExtractionJobAndStatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExtractionJobAndStatusResponse:
        """Test ExtractionJobAndStatusResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtractionJobAndStatusResponse`
        """
        model = ExtractionJobAndStatusResponse()
        if include_optional:
            return ExtractionJobAndStatusResponse(
                extraction_jobs = [
                    visier_api_data_in.models.extraction_job.ExtractionJob(
                        current_stage = '', 
                        extraction_job_id = '', 
                        status = '', 
                        tenant_code = '', )
                    ],
                limit = 56,
                parent_job_id = '',
                parent_tenant_code = '',
                start = 56
            )
        else:
            return ExtractionJobAndStatusResponse(
        )
        """

    def testExtractionJobAndStatusResponse(self):
        """Test ExtractionJobAndStatusResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
