# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.99201.1475
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.job_cancellation_result_dto import JobCancellationResultDTO

class TestJobCancellationResultDTO(unittest.TestCase):
    """JobCancellationResultDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobCancellationResultDTO:
        """Test JobCancellationResultDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobCancellationResultDTO`
        """
        model = JobCancellationResultDTO()
        if include_optional:
            return JobCancellationResultDTO(
                cancel_status = 'CANCEL_FAILED',
                job_id = '',
                job_status = '',
                job_type = '',
                message = '',
                parent_job_id = '',
                tenant_code = ''
            )
        else:
            return JobCancellationResultDTO(
        )
        """

    def testJobCancellationResultDTO(self):
        """Test JobCancellationResultDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
