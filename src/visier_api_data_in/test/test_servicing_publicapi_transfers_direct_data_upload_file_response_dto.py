# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_in.models
from visier_api_data_in.models.servicing_publicapi_transfers_direct_data_upload_file_response_dto import ServicingPublicapiTransfersDirectDataUploadFileResponseDTO

class TestServicingPublicapiTransfersDirectDataUploadFileResponseDTO(unittest.TestCase):
    """ServicingPublicapiTransfersDirectDataUploadFileResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingPublicapiTransfersDirectDataUploadFileResponseDTO:
        """Test ServicingPublicapiTransfersDirectDataUploadFileResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingPublicapiTransfersDirectDataUploadFileResponseDTO(
                message = '',
                status = '',
                transaction_id = ''
            )
        else:
            return ServicingPublicapiTransfersDirectDataUploadFileResponseDTO(
        )

    def testServicingPublicapiTransfersDirectDataUploadFileResponseDTO(self):
        """Test ServicingPublicapiTransfersDirectDataUploadFileResponseDTO"""
        def validate_instance(instance):
            ServicingPublicapiTransfersDirectDataUploadFileResponseDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingPublicapiTransfersDirectDataUploadFileResponseDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
