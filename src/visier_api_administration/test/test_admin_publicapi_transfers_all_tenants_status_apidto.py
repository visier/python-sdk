# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_administration.models
from visier_api_administration.models.admin_publicapi_transfers_all_tenants_status_apidto import AdminPublicapiTransfersAllTenantsStatusAPIDTO

class TestAdminPublicapiTransfersAllTenantsStatusAPIDTO(unittest.TestCase):
    """AdminPublicapiTransfersAllTenantsStatusAPIDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdminPublicapiTransfersAllTenantsStatusAPIDTO:
        """Test AdminPublicapiTransfersAllTenantsStatusAPIDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return AdminPublicapiTransfersAllTenantsStatusAPIDTO(
                limit = 56,
                start = 56,
                tenants = [
                    visier_api_administration.models.admin/publicapi/transfers/tenant_detail_apidto.admin.publicapi.transfers.TenantDetailAPIDTO(
                        allowed_o_auth_idp_url_domains = [
                            ''
                            ], 
                        can_administer_other_tenants = True, 
                        current_data_version = '', 
                        custom_properties = [
                            visier_api_administration.models.admin/publicapi/transfers/custom_tenant_property_dto.admin.publicapi.transfers.CustomTenantPropertyDTO(
                                key = '', 
                                value = '', )
                            ], 
                        data_version_date = '', 
                        embeddable_domains = [
                            ''
                            ], 
                        industry_code = 56, 
                        modules = [
                            visier_api_administration.models.designer/transfers/tenant_module_dto.designer.transfers.TenantModuleDTO(
                                display_name = '', 
                                module_settings = None, 
                                symbol_name = '', )
                            ], 
                        provision_date = '', 
                        sso_instance_issuers = [
                            ''
                            ], 
                        status = '', 
                        tenant_code = '', 
                        tenant_display_name = '', 
                        vanity_url_name = '', )
                    ]
            )
        else:
            return AdminPublicapiTransfersAllTenantsStatusAPIDTO(
        )

    def testAdminPublicapiTransfersAllTenantsStatusAPIDTO(self):
        """Test AdminPublicapiTransfersAllTenantsStatusAPIDTO"""
        def validate_instance(instance):
            AdminPublicapiTransfersAllTenantsStatusAPIDTO.model_validate(inst_req_only)
            instance_deserialized = AdminPublicapiTransfersAllTenantsStatusAPIDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
