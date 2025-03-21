# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_administration.api.user_groups_v2_api import UserGroupsV2Api


class TestUserGroupsV2Api(unittest.TestCase):
    """UserGroupsV2Api unit test stubs"""

    def setUp(self) -> None:
        self.api = UserGroupsV2Api()

    def tearDown(self) -> None:
        pass

    def test_create_user_groups(self) -> None:
        """Test case for create_user_groups

        Create multiple user groups
        """
        pass

    def test_delete_user_group(self) -> None:
        """Test case for delete_user_group

        Delete a user group
        """
        pass

    def test_delete_user_groups(self) -> None:
        """Test case for delete_user_groups

        Delete multiple user groups
        """
        pass

    def test_get_user_group(self) -> None:
        """Test case for get_user_group

        Retrieve the details of a user group
        """
        pass

    def test_get_user_groups(self) -> None:
        """Test case for get_user_groups

        Retrieve a list of user groups
        """
        pass

    def test_patch_user_groups(self) -> None:
        """Test case for patch_user_groups

        Patch multiple user groups
        """
        pass

    def test_put_user_groups(self) -> None:
        """Test case for put_user_groups

        Update multiple user groups
        """
        pass


if __name__ == '__main__':
    unittest.main()
