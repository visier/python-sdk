# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.tenant_data_uploads_list_response_dto import TenantDataUploadsListResponseDTO

class TestTenantDataUploadsListResponseDTO(unittest.TestCase):
    """TenantDataUploadsListResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantDataUploadsListResponseDTO:
        """Test TenantDataUploadsListResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantDataUploadsListResponseDTO`
        """
        model = TenantDataUploadsListResponseDTO()
        if include_optional:
            return TenantDataUploadsListResponseDTO(
                limit = 56,
                start = 56,
                tenants = [
                    visier.sdk.api.data_in.models.tenant_data_uploads_response_dto.TenantDataUploadsResponseDTO(
                        tenant_code = '', 
                        uploads = [
                            visier.sdk.api.data_in.models.tenant_data_upload_status_response_dto.TenantDataUploadStatusResponseDTO(
                                included = True, 
                                upload_time = '', )
                            ], )
                    ]
            )
        else:
            return TenantDataUploadsListResponseDTO(
        )
        """

    def testTenantDataUploadsListResponseDTO(self):
        """Test TenantDataUploadsListResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
