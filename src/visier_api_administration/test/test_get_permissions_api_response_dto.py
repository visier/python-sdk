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
from visier_api_administration.models.get_permissions_api_response_dto import GetPermissionsAPIResponseDTO

class TestGetPermissionsAPIResponseDTO(unittest.TestCase):
    """GetPermissionsAPIResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPermissionsAPIResponseDTO:
        """Test GetPermissionsAPIResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return GetPermissionsAPIResponseDTO(
                permissions = [
                    visier_api_administration.models.permission_dto.PermissionDTO(
                        admin_capability_config = None, 
                        data_security_profiles = [
                            visier_api_administration.models.data_security_profile_dto.DataSecurityProfileDTO(
                                all_data_point_access = True, 
                                analytic_object_id = '', 
                                analytic_object_status = 'Unset', 
                                inherited_access_configs = [
                                    visier_api_administration.models.inherited_access_config_dto.InheritedAccessConfigDTO(
                                        analytic_object_id = '', 
                                        member_filter_configs = [
                                            visier_api_administration.models.member_filter_config_dto.MemberFilterConfigDTO(
                                                dimension_filters = [
                                                    visier_api_administration.models.dimension_filter_dto.DimensionFilterDTO(
                                                        dynamic_dimension_filter = visier_api_administration.models.dynamic_dimension_filter_dto.DynamicDimensionFilterDTO(
                                                            dimension_id = '', 
                                                            dimension_status = 'Unset', 
                                                            dynamic_property_mappings = [
                                                                visier_api_administration.models.dynamic_property_mapping_dto.DynamicPropertyMappingDTO(
                                                                    hierarchy_property_id = '', 
                                                                    hierarchy_property_status = 'Unset', 
                                                                    user_property = None, )
                                                                ], 
                                                            subject_reference_path = [
                                                                ''
                                                                ], ), 
                                                        static_dimension_filter = visier_api_administration.models.static_dimension_filter_dto.StaticDimensionFilterDTO(
                                                            dimension_id = '', 
                                                            dimension_status = 'Unset', 
                                                            member_selections = [
                                                                visier_api_administration.models.member_selection_dto.MemberSelectionDTO(
                                                                    dimension_member_status = 'Unset', 
                                                                    excluded = True, 
                                                                    name_path = [
                                                                        ''
                                                                        ], )
                                                                ], ), )
                                                    ], )
                                            ], 
                                        remove_access = True, )
                                    ], 
                                inherited_reference_member_filter_config = None, 
                                member_filter_configs = [
                                    visier_api_administration.models.member_filter_config_dto.MemberFilterConfigDTO()
                                    ], 
                                property_set_config = None, )
                            ], 
                        description = '', 
                        display_name = '', 
                        permission_id = '', 
                        role_modules_config = None, )
                    ]
            )
        else:
            return GetPermissionsAPIResponseDTO(
        )

    def testGetPermissionsAPIResponseDTO(self):
        """Test GetPermissionsAPIResponseDTO"""
        def validate_instance(instance):
            GetPermissionsAPIResponseDTO.model_validate(inst_req_only)
            instance_deserialized = GetPermissionsAPIResponseDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
