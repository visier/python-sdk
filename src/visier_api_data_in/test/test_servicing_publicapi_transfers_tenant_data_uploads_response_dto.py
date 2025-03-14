# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1791
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_in.models
from visier_api_data_in.models.servicing_publicapi_transfers_tenant_data_uploads_response_dto import ServicingPublicapiTransfersTenantDataUploadsResponseDTO

class TestServicingPublicapiTransfersTenantDataUploadsResponseDTO(unittest.TestCase):
    """ServicingPublicapiTransfersTenantDataUploadsResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingPublicapiTransfersTenantDataUploadsResponseDTO:
        """Test ServicingPublicapiTransfersTenantDataUploadsResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingPublicapiTransfersTenantDataUploadsResponseDTO(
                tenant_code = '',
                uploads = [
                    visier_api_data_in.models.servicing/publicapi/transfers/tenant_data_upload_status_response_dto.servicing.publicapi.transfers.TenantDataUploadStatusResponseDTO(
                        included = True, 
                        upload_time = '', )
                    ]
            )
        else:
            return ServicingPublicapiTransfersTenantDataUploadsResponseDTO(
        )

    def testServicingPublicapiTransfersTenantDataUploadsResponseDTO(self):
        """Test ServicingPublicapiTransfersTenantDataUploadsResponseDTO"""
        def validate_instance(instance):
            ServicingPublicapiTransfersTenantDataUploadsResponseDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingPublicapiTransfersTenantDataUploadsResponseDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
