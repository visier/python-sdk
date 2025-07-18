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
from visier_platform_sdk.models.all_permissions_assigned_for_local_tenant_dto import AllPermissionsAssignedForLocalTenantDTO

class TestAllPermissionsAssignedForLocalTenantDTO(unittest.TestCase):
    """AllPermissionsAssignedForLocalTenantDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AllPermissionsAssignedForLocalTenantDTO:
        """Test AllPermissionsAssignedForLocalTenantDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return AllPermissionsAssignedForLocalTenantDTO(
                assigned_permissions = [
                    visier_platform_sdk.models.permission_assigned_for_local_tenant_dto.PermissionAssignedForLocalTenantDTO(
                        permission_id = '', 
                        display_name = '', 
                        description = '', )
                    ]
            )
        else:
            return AllPermissionsAssignedForLocalTenantDTO(
        )

    def testAllPermissionsAssignedForLocalTenantDTO(self):
        """Test AllPermissionsAssignedForLocalTenantDTO"""
        def validate_instance(instance):
            AllPermissionsAssignedForLocalTenantDTO.model_validate(inst_req_only)
            instance_deserialized = AllPermissionsAssignedForLocalTenantDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
