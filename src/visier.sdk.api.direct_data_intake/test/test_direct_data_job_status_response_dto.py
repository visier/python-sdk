# coding: utf-8

"""
    Visier Public Direct Data Intake APIs

    Visier APIs for uploading already transformed data files directly to target objects in Visier.

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.direct_data_intake.models.direct_data_job_status_response_dto import DirectDataJobStatusResponseDTO

class TestDirectDataJobStatusResponseDTO(unittest.TestCase):
    """DirectDataJobStatusResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DirectDataJobStatusResponseDTO:
        """Test DirectDataJobStatusResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DirectDataJobStatusResponseDTO`
        """
        model = DirectDataJobStatusResponseDTO()
        if include_optional:
            return DirectDataJobStatusResponseDTO(
                job_id = '',
                message = '',
                status = '',
                tenant_code = '',
                transaction_id = ''
            )
        else:
            return DirectDataJobStatusResponseDTO(
        )
        """

    def testDirectDataJobStatusResponseDTO(self):
        """Test DirectDataJobStatusResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
