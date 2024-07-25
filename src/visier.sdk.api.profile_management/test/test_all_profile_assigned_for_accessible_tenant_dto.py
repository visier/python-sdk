# coding: utf-8

"""
    Visier Profile Management APIs

    Visier APIs for managing the profiles assigned to users

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.profile_management.models.all_profile_assigned_for_accessible_tenant_dto import AllProfileAssignedForAccessibleTenantDTO

class TestAllProfileAssignedForAccessibleTenantDTO(unittest.TestCase):
    """AllProfileAssignedForAccessibleTenantDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AllProfileAssignedForAccessibleTenantDTO:
        """Test AllProfileAssignedForAccessibleTenantDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AllProfileAssignedForAccessibleTenantDTO`
        """
        model = AllProfileAssignedForAccessibleTenantDTO()
        if include_optional:
            return AllProfileAssignedForAccessibleTenantDTO(
                assigned_profiles_for_accessible_tenant = [
                    visier.sdk.api.profile_management.models.profile_assigned_for_accessible_tenant_dto.ProfileAssignedForAccessibleTenantDTO(
                        display_name = '', 
                        for_all_children = True, 
                        profile_id = '', 
                        tenant_code = '', 
                        validity_end_time = '', 
                        validity_start_time = '', )
                    ]
            )
        else:
            return AllProfileAssignedForAccessibleTenantDTO(
        )
        """

    def testAllProfileAssignedForAccessibleTenantDTO(self):
        """Test AllProfileAssignedForAccessibleTenantDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
