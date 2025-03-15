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
from visier_api_data_in.models.designer_transfers_success_factors_auth_params_dto import DesignerTransfersSuccessFactorsAuthParamsDTO

class TestDesignerTransfersSuccessFactorsAuthParamsDTO(unittest.TestCase):
    """DesignerTransfersSuccessFactorsAuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DesignerTransfersSuccessFactorsAuthParamsDTO:
        """Test DesignerTransfersSuccessFactorsAuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DesignerTransfersSuccessFactorsAuthParamsDTO(
                company_id = '',
                host_domain_name = '',
                o_auth = visier_api_data_in.models.designer/transfers/success_factors_o_auth_params_dto.designer.transfers.SuccessFactorsOAuthParamsDTO(
                    api_key = '', 
                    private_x509_key = '', 
                    public_x509_cert = '', ),
                password = '',
                username = ''
            )
        else:
            return DesignerTransfersSuccessFactorsAuthParamsDTO(
        )

    def testDesignerTransfersSuccessFactorsAuthParamsDTO(self):
        """Test DesignerTransfersSuccessFactorsAuthParamsDTO"""
        def validate_instance(instance):
            DesignerTransfersSuccessFactorsAuthParamsDTO.model_validate(inst_req_only)
            instance_deserialized = DesignerTransfersSuccessFactorsAuthParamsDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
