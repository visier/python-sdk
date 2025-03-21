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
from visier_api_data_in.models.designer_transfers_workday_auth_params_dto import DesignerTransfersWorkdayAuthParamsDTO

class TestDesignerTransfersWorkdayAuthParamsDTO(unittest.TestCase):
    """DesignerTransfersWorkdayAuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DesignerTransfersWorkdayAuthParamsDTO:
        """Test DesignerTransfersWorkdayAuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DesignerTransfersWorkdayAuthParamsDTO(
                api_key = '',
                domain_name = '',
                implementation_name = '',
                integration_system_id = '',
                o_auth = visier_api_data_in.models.designer/transfers/workday_o_auth_params_dto.designer.transfers.WorkdayOAuthParamsDTO(
                    api_client_id = '', 
                    private_x509_key = '', 
                    public_x509_cert = '', ),
                password = '',
                ref_token = visier_api_data_in.models.designer/transfers/workday_refresh_token_params_dto.designer.transfers.WorkdayRefreshTokenParamsDTO(
                    api_client_id = '', 
                    client_secret = '', 
                    refresh_token = '', ),
                user_id = ''
            )
        else:
            return DesignerTransfersWorkdayAuthParamsDTO(
        )

    def testDesignerTransfersWorkdayAuthParamsDTO(self):
        """Test DesignerTransfersWorkdayAuthParamsDTO"""
        def validate_instance(instance):
            DesignerTransfersWorkdayAuthParamsDTO.model_validate(inst_req_only)
            instance_deserialized = DesignerTransfersWorkdayAuthParamsDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
