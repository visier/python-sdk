# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1614
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_administration.api.users_v1_api import UsersV1Api


class TestUsersV1Api(unittest.TestCase):
    """UsersV1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = UsersV1Api()

    def tearDown(self) -> None:
        pass

    def test_add_user(self) -> None:
        """Test case for add_user

        Add a user
        """
        pass

    def test_add_users_to_user_group(self) -> None:
        """Test case for add_users_to_user_group

        Assign users to user groups
        """
        pass

    def test_assign_permissions(self) -> None:
        """Test case for assign_permissions

        Assign permissions to users
        """
        pass

    def test_assign_permissions_to_user_groups(self) -> None:
        """Test case for assign_permissions_to_user_groups

        Assign permissions to user groups
        """
        pass

    def test_delete_user(self) -> None:
        """Test case for delete_user

        Delete a user
        """
        pass

    def test_get_all_permissions_xlsx(self) -> None:
        """Test case for get_all_permissions_xlsx

        Retrieve a list of all permissions in XLSX format
        """
        pass

    def test_get_all_user_groups(self) -> None:
        """Test case for get_all_user_groups

        Retrieve a list of all user groups
        """
        pass

    def test_get_all_users(self) -> None:
        """Test case for get_all_users

        Retrieve a list of all users
        """
        pass

    def test_get_application_logs_xlsx(self) -> None:
        """Test case for get_application_logs_xlsx

        Retrieve the Application Logs
        """
        pass

    def test_get_data_security_report_xlsx(self) -> None:
        """Test case for get_data_security_report_xlsx

        Retrieve the Data Security Report
        """
        pass

    def test_get_permission_assigned_users(self) -> None:
        """Test case for get_permission_assigned_users

        Retrieve users that are assigned a specific permission
        """
        pass

    def test_get_profile_assignments_xlsx(self) -> None:
        """Test case for get_profile_assignments_xlsx

        Retrieve user profile assignments in XLSX format
        """
        pass

    def test_get_user_detail(self) -> None:
        """Test case for get_user_detail

        Retrieve a user's details
        """
        pass

    def test_get_user_group_users(self) -> None:
        """Test case for get_user_group_users

        Retrieve a list of user group users
        """
        pass

    def test_get_user_permissions_xlsx(self) -> None:
        """Test case for get_user_permissions_xlsx

        Retrieve user permissions in XLSX format
        """
        pass

    def test_remove_permissions(self) -> None:
        """Test case for remove_permissions

        Remove permissions from users
        """
        pass

    def test_remove_users_from_user_group(self) -> None:
        """Test case for remove_users_from_user_group

        Remove users from user groups
        """
        pass

    def test_revoke_permissions_from_user_groups(self) -> None:
        """Test case for revoke_permissions_from_user_groups

        Remove permissions from user groups
        """
        pass

    def test_update_user(self) -> None:
        """Test case for update_user

        Update a user
        """
        pass


if __name__ == '__main__':
    unittest.main()
