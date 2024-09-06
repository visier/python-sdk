# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_administration.models.user_group_change_users_dto import UserGroupChangeUsersDTO

class TestUserGroupChangeUsersDTO(unittest.TestCase):
    """UserGroupChangeUsersDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserGroupChangeUsersDTO:
        """Test UserGroupChangeUsersDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserGroupChangeUsersDTO`
        """
        model = UserGroupChangeUsersDTO()
        if include_optional:
            return UserGroupChangeUsersDTO(
                dynamic_filter_definition = visier_api_administration.models.user_group_filters_dto.UserGroupFiltersDTO(
                    filters = [
                        visier_api_administration.models.user_group_change_filter_dto.UserGroupChangeFilterDTO(
                            analytic_object_id = '', 
                            dimension_filters = [
                                visier_api_administration.models.user_group_change_dimension_filter_dto.UserGroupChangeDimensionFilterDTO(
                                    dimension_id = '', 
                                    member_selections = [
                                        visier_api_administration.models.user_group_change_member_selection_dto.UserGroupChangeMemberSelectionDTO(
                                            is_excluded = True, 
                                            name_path = [
                                                ''
                                                ], )
                                        ], 
                                    subject_reference_path = null, )
                                ], 
                            filter_id = '', )
                        ], ),
                include_all_users = True,
                manually_excluded_ids = visier_api_administration.models.element_ids_dto.ElementIDsDTO(
                    ids = [
                        ''
                        ], ),
                manually_included_ids = visier_api_administration.models.element_ids_dto.ElementIDsDTO(
                    ids = [
                        ''
                        ], )
            )
        else:
            return UserGroupChangeUsersDTO(
        )
        """

    def testUserGroupChangeUsersDTO(self):
        """Test UserGroupChangeUsersDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()