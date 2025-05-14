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
from visier_api_administration.models.servicing_user_get_api_response_dto import ServicingUserGetAPIResponseDTO

class TestServicingUserGetAPIResponseDTO(unittest.TestCase):
    """ServicingUserGetAPIResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingUserGetAPIResponseDTO:
        """Test ServicingUserGetAPIResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingUserGetAPIResponseDTO(
                user_id = '',
                username = '',
                display_name = '',
                employee_id = '',
                account_enabled = True,
                profiles = visier_api_administration.models.servicing/all_profile_assigned_for_local_tenant_dto.servicing.AllProfileAssignedForLocalTenantDTO(
                    assigned_profiles = [
                        visier_api_administration.models.servicing/profile_assigned_for_local_tenant_dto.servicing.ProfileAssignedForLocalTenantDTO(
                            profile_id = '', 
                            display_name = '', 
                            validity_start_time = '', 
                            validity_end_time = '', 
                            capabilities = [
                                visier_api_administration.models.servicing/capabilities_dto.servicing.CapabilitiesDTO(
                                    capability = '', 
                                    access_level = '', 
                                    view_level = '', )
                                ], 
                            additional_capabilities = None, )
                        ], ),
                permissions = visier_api_administration.models.servicing/all_permissions_assigned_for_local_tenant_dto.servicing.AllPermissionsAssignedForLocalTenantDTO(
                    assigned_permissions = [
                        visier_api_administration.models.servicing/permission_assigned_for_local_tenant_dto.servicing.PermissionAssignedForLocalTenantDTO(
                            permission_id = '', 
                            display_name = '', 
                            description = '', )
                        ], ),
                user_groups = visier_api_administration.models.servicing/all_user_groups_assigned_for_local_tenant_dto.servicing.AllUserGroupsAssignedForLocalTenantDTO(
                    assigned_user_groups = [
                        visier_api_administration.models.servicing/user_group_assigned_for_local_tenant_dto.servicing.UserGroupAssignedForLocalTenantDTO(
                            user_group_id = '', 
                            display_name = '', )
                        ], ),
                last_login = visier_api_administration.models.servicing/last_login_dto.servicing.LastLoginDTO(
                    timestamp = '', ),
                email = ''
            )
        else:
            return ServicingUserGetAPIResponseDTO(
        )

    def testServicingUserGetAPIResponseDTO(self):
        """Test ServicingUserGetAPIResponseDTO"""
        def validate_instance(instance):
            ServicingUserGetAPIResponseDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingUserGetAPIResponseDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
