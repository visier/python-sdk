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
from visier_api_data_in.models.admin_transfers_set_connector_settings_request_dto import AdminTransfersSetConnectorSettingsRequestDTO

class TestAdminTransfersSetConnectorSettingsRequestDTO(unittest.TestCase):
    """AdminTransfersSetConnectorSettingsRequestDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdminTransfersSetConnectorSettingsRequestDTO:
        """Test AdminTransfersSetConnectorSettingsRequestDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return AdminTransfersSetConnectorSettingsRequestDTO(
                connectors = [
                    visier_api_data_in.models.admin/transfers/set_connector_setting_request_dto.admin.transfers.SetConnectorSettingRequestDTO(
                        connector_id = '', 
                        tenants = [
                            visier_api_data_in.models.admin/transfers/tenant_connector_settings_request_dto.admin.transfers.TenantConnectorSettingsRequestDTO(
                                connector_settings = [
                                    visier_api_data_in.models.admin/transfers/connector_setting_request_dto.admin.transfers.ConnectorSettingRequestDTO(
                                        setting_key = '', 
                                        value = '', )
                                    ], 
                                tenant_code = '', )
                            ], )
                    ]
            )
        else:
            return AdminTransfersSetConnectorSettingsRequestDTO(
        )

    def testAdminTransfersSetConnectorSettingsRequestDTO(self):
        """Test AdminTransfersSetConnectorSettingsRequestDTO"""
        def validate_instance(instance):
            AdminTransfersSetConnectorSettingsRequestDTO.model_validate(inst_req_only)
            instance_deserialized = AdminTransfersSetConnectorSettingsRequestDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
