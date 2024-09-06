# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_administration.models.all_profile_assigned_for_local_tenant_dto import AllProfileAssignedForLocalTenantDTO

class TestAllProfileAssignedForLocalTenantDTO(unittest.TestCase):
    """AllProfileAssignedForLocalTenantDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AllProfileAssignedForLocalTenantDTO:
        """Test AllProfileAssignedForLocalTenantDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AllProfileAssignedForLocalTenantDTO`
        """
        model = AllProfileAssignedForLocalTenantDTO()
        if include_optional:
            return AllProfileAssignedForLocalTenantDTO(
                assigned_profiles = [
                    visier_api_administration.models.profile_assigned_for_local_tenant_dto.ProfileAssignedForLocalTenantDTO(
                        additional_capabilities = null, 
                        capabilities = [
                            visier_api_administration.models.capabilities_dto.CapabilitiesDTO(
                                access_level = '', 
                                capability = '', 
                                view_level = '', )
                            ], 
                        display_name = '', 
                        profile_id = '', 
                        validity_end_time = '', 
                        validity_start_time = '', )
                    ]
            )
        else:
            return AllProfileAssignedForLocalTenantDTO(
        )
        """

    def testAllProfileAssignedForLocalTenantDTO(self):
        """Test AllProfileAssignedForLocalTenantDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()