# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.tenant_data_uploads_response_dto import TenantDataUploadsResponseDTO

class TestTenantDataUploadsResponseDTO(unittest.TestCase):
    """TenantDataUploadsResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantDataUploadsResponseDTO:
        """Test TenantDataUploadsResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantDataUploadsResponseDTO`
        """
        model = TenantDataUploadsResponseDTO()
        if include_optional:
            return TenantDataUploadsResponseDTO(
                tenant_code = '',
                uploads = [
                    visier.sdk.api.data_in.models.tenant_data_upload_status_response_dto.TenantDataUploadStatusResponseDTO(
                        included = True, 
                        upload_time = '', )
                    ]
            )
        else:
            return TenantDataUploadsResponseDTO(
        )
        """

    def testTenantDataUploadsResponseDTO(self):
        """Test TenantDataUploadsResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
