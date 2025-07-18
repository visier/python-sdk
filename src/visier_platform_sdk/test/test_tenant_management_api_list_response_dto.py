# coding: utf-8

"""
    API Reference

    Detailed API reference documentation for Visier APIs. Includes all endpoints, headers, path parameters, query parameters, request body schema, response schema, JSON request samples, and JSON response samples.

    The version of the OpenAPI document: 22222222.99201.2050
    Contact: alpine@visier.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import visier_platform_sdk.models
from visier_platform_sdk.models.tenant_management_api_list_response_dto import TenantManagementAPIListResponseDTO

class TestTenantManagementAPIListResponseDTO(unittest.TestCase):
    """TenantManagementAPIListResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantManagementAPIListResponseDTO:
        """Test TenantManagementAPIListResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return TenantManagementAPIListResponseDTO(
                tenants = [
                    visier_platform_sdk.models.tenant_management_api_get_response_dto.TenantManagementAPIGetResponseDTO(
                        tenant_code = '', 
                        tenant_display_name = '', 
                        status = '', 
                        provision_date = '', 
                        current_data_version = '', 
                        data_version_date = '', 
                        purchased_modules = [
                            ''
                            ], 
                        industry_code = 56, 
                        primary_business_location = None, 
                        can_administer_other_tenants = True, 
                        embeddable_domains = [
                            ''
                            ], 
                        custom_properties = [
                            visier_platform_sdk.models.custom_property_dto.CustomPropertyDTO(
                                key = '', 
                                value = '', )
                            ], 
                        sso_instance_issuers = [
                            ''
                            ], 
                        vanity_url_name = '', 
                        home_analysis_id = '', 
                        home_analysis_by_user_group = [
                            visier_platform_sdk.models.home_analysis_by_user_group_dto.HomeAnalysisByUserGroupDTO(
                                user_group_id = '', 
                                home_analysis_id = '', )
                            ], 
                        click_through_link = '', 
                        click_through_link_enabled = '', 
                        default_currency = '', 
                        allowed_o_auth_idp_url_domains = [
                            ''
                            ], 
                        effective_industry_code = 56, 
                        company_size = 56, 
                        traits = None, )
                    ],
                limit = 56,
                start = 56
            )
        else:
            return TenantManagementAPIListResponseDTO(
        )

    def testTenantManagementAPIListResponseDTO(self):
        """Test TenantManagementAPIListResponseDTO"""
        def validate_instance(instance):
            TenantManagementAPIListResponseDTO.model_validate(inst_req_only)
            instance_deserialized = TenantManagementAPIListResponseDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
