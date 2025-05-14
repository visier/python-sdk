# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1905
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_administration.models
from visier_api_administration.models.admin_tenant_management_api_update_request_dto import AdminTenantManagementAPIUpdateRequestDTO

class TestAdminTenantManagementAPIUpdateRequestDTO(unittest.TestCase):
    """AdminTenantManagementAPIUpdateRequestDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdminTenantManagementAPIUpdateRequestDTO:
        """Test AdminTenantManagementAPIUpdateRequestDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return AdminTenantManagementAPIUpdateRequestDTO(
                tenant_code = '',
                tenant_display_name = '',
                tenant_short_name = '',
                vanity_url_name = '',
                industry_code = 56,
                primary_business_location = visier_api_administration.models.admin/business_location_dto.admin.BusinessLocationDTO(
                    country_code = '', 
                    postal_code = '', ),
                purchased_modules = [
                    ''
                    ],
                embeddable_domains = [
                    ''
                    ],
                custom_properties = [
                    visier_api_administration.models.admin/custom_property_dto.admin.CustomPropertyDTO(
                        key = '', 
                        value = '', )
                    ],
                sso_instance_issuers = [
                    ''
                    ],
                home_analysis_id = '',
                home_analysis_by_user_group = [
                    visier_api_administration.models.admin/home_analysis_by_user_group_dto.admin.HomeAnalysisByUserGroupDTO(
                        user_group_id = '', 
                        home_analysis_id = '', )
                    ],
                update_action = 'MERGE',
                enabled = True,
                click_through_link = '',
                default_currency = '',
                allowed_o_auth_idp_url_domains = [
                    ''
                    ],
                traits = visier_api_administration.models.admin/tenant_details_traits_dto.admin.TenantDetailsTraitsDTO(
                    aggregation_rights = True, 
                    tenant_type = 'ROOT_ADMIN', 
                    data_profile_type = 'Regular', )
            )
        else:
            return AdminTenantManagementAPIUpdateRequestDTO(
        )

    def testAdminTenantManagementAPIUpdateRequestDTO(self):
        """Test AdminTenantManagementAPIUpdateRequestDTO"""
        def validate_instance(instance):
            AdminTenantManagementAPIUpdateRequestDTO.model_validate(inst_req_only)
            instance_deserialized = AdminTenantManagementAPIUpdateRequestDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
