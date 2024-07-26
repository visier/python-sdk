# coding: utf-8

"""
    Visier Tenant Management APIs

    Visier APIs for managing tenants

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.tenant_management.models.tenant_management_api_update_request_dto import TenantManagementAPIUpdateRequestDTO

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
        # uncomment below to create an instance of `TenantManagementAPIUpdateRequestDTO`
        """
        model = TenantManagementAPIUpdateRequestDTO()
        if include_optional:
            return TenantManagementAPIUpdateRequestDTO(
                click_through_link = '',
                custom_properties = [
                    visier.sdk.api.tenant_management.models.custom_property_dto.CustomPropertyDTO(
                        key = '', 
                        value = '', )
                    ],
                default_currency = '',
                embeddable_domains = [
                    ''
                    ],
                enabled = True,
                home_analysis_by_user_group = [
                    visier.sdk.api.tenant_management.models.home_analysis_by_user_group_dto.HomeAnalysisByUserGroupDTO(
                        home_analysis_id = '', 
                        user_group_id = '', )
                    ],
                home_analysis_id = '',
                industry_code = 56,
                primary_business_location = visier.sdk.api.tenant_management.models.business_location_dto.BusinessLocationDTO(
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
        """

    def testTenantManagementAPIUpdateRequestDTO(self):
        """Test TenantManagementAPIUpdateRequestDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
