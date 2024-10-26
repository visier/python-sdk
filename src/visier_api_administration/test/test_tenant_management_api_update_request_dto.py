# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1547
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_administration.models
from visier_api_administration.models.tenant_management_api_update_request_dto import TenantManagementAPIUpdateRequestDTO

class TestTenantManagementAPIUpdateRequestDTO(unittest.TestCase):
    """TenantManagementAPIUpdateRequestDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantManagementAPIUpdateRequestDTO:
        """Test TenantManagementAPIUpdateRequestDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return TenantManagementAPIUpdateRequestDTO(
                click_through_link = '',
                custom_properties = [
                    visier_api_administration.models.custom_property_dto.CustomPropertyDTO(
                        key = '', 
                        value = '', )
                    ],
                default_currency = '',
                embeddable_domains = [
                    ''
                    ],
                enabled = True,
                home_analysis_by_user_group = [
                    visier_api_administration.models.home_analysis_by_user_group_dto.HomeAnalysisByUserGroupDTO(
                        home_analysis_id = '', 
                        user_group_id = '', )
                    ],
                home_analysis_id = '',
                industry_code = 56,
                primary_business_location = visier_api_administration.models.business_location_dto.BusinessLocationDTO(
                    country_code = '', 
                    postal_code = '', ),
                purchased_modules = [
                    ''
                    ],
                sso_instance_issuers = [
                    ''
                    ],
                tenant_code = '',
                tenant_display_name = '',
                tenant_short_name = '',
                update_action = 'MERGE',
                vanity_url_name = ''
            )
        else:
            return TenantManagementAPIUpdateRequestDTO(
        )

    def testTenantManagementAPIUpdateRequestDTO(self):
        """Test TenantManagementAPIUpdateRequestDTO"""
        def validate_instance(instance):
            TenantManagementAPIUpdateRequestDTO.model_validate(inst_req_only)
            instance_deserialized = TenantManagementAPIUpdateRequestDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
