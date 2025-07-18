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
from visier_platform_sdk.models.permission_dto import PermissionDTO

class TestPermissionDTO(unittest.TestCase):
    """PermissionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionDTO:
        """Test PermissionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return PermissionDTO(
                permission_id = '',
                display_name = '',
                description = '',
                data_security_profiles = [
                    visier_platform_sdk.models.data_security_profile_dto.DataSecurityProfileDTO(
                        analytic_object_id = '', 
                        property_set_config = None, 
                        all_data_point_access = True, 
                        member_filter_configs = [
                            visier_platform_sdk.models.member_filter_config_dto.MemberFilterConfigDTO(
                                dimension_filters = [
                                    visier_platform_sdk.models.dimension_filter_dto.DimensionFilterDTO(
                                        dimension_name = '', 
                                        qualifying_path = [
                                            ''
                                            ], 
                                        member_selections = [
                                            visier_platform_sdk.models.member_selection_dto.MemberSelectionDTO(
                                                name_path = [
                                                    ''
                                                    ], 
                                                is_excluded = True, )
                                            ], )
                                    ], )
                            ], 
                        inherited_access_configs = [
                            visier_platform_sdk.models.inherited_access_config_dto.InheritedAccessConfigDTO(
                                analytic_object_id = '', 
                                remove_access = True, )
                            ], 
                        inherited_reference_member_filter_config = None, 
                        analytic_object_status = 'Unset', )
                    ],
                admin_capability_config = visier_platform_sdk.models.admin_capability_config_dto.AdminCapabilityConfigDTO(
                    all_capabilities_access = True, 
                    capabilities = [
                        ''
                        ], ),
                role_modules_config = visier_platform_sdk.models.role_modules_config_dto.RoleModulesConfigDTO(
                    content_package_ids = [
                        ''
                        ], )
            )
        else:
            return PermissionDTO(
        )

    def testPermissionDTO(self):
        """Test PermissionDTO"""
        def validate_instance(instance):
            PermissionDTO.model_validate(inst_req_only)
            instance_deserialized = PermissionDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
