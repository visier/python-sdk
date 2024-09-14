# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1482
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_administration.models.tenant_detail_apidto import TenantDetailAPIDTO

class TestTenantDetailAPIDTO(unittest.TestCase):
    """TenantDetailAPIDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantDetailAPIDTO:
        """Test TenantDetailAPIDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantDetailAPIDTO`
        """
        model = TenantDetailAPIDTO()
        if include_optional:
            return TenantDetailAPIDTO(
                can_administer_other_tenants = True,
                current_data_version = '',
                custom_properties = [
                    visier_api_administration.models.custom_tenant_property_dto.CustomTenantPropertyDTO(
                        key = '', 
                        value = '', )
                    ],
                data_version_date = '',
                embeddable_domains = [
                    ''
                    ],
                industry_code = 56,
                modules = [
                    visier_api_administration.models.tenant_module_dto.TenantModuleDTO(
                        display_name = '', 
                        module_settings = null, 
                        symbol_name = '', )
                    ],
                provision_date = '',
                sso_instance_issuers = [
                    ''
                    ],
                status = '',
                tenant_code = '',
                tenant_display_name = '',
                vanity_url_name = ''
            )
        else:
            return TenantDetailAPIDTO(
        )
        """

    def testTenantDetailAPIDTO(self):
        """Test TenantDetailAPIDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
