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

from visier_api_administration.api.users_v2_api import UsersV2Api


class TestUsersV2Api(unittest.TestCase):
    """UsersV2Api unit test stubs"""

    def setUp(self) -> None:
        self.api = UsersV2Api()

    def tearDown(self) -> None:
        pass

    def test_add_users(self) -> None:
        """Test case for add_users

        Add users
        """
        pass

    def test_delete_users(self) -> None:
        """Test case for delete_users

        Delete users
        """
        pass

    def test_update_users(self) -> None:
        """Test case for update_users

        Update users
        """
        pass


if __name__ == '__main__':
    unittest.main()
