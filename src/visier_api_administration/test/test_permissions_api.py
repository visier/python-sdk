# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1508
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_administration.api.permissions_api import PermissionsApi


class TestPermissionsApi(unittest.TestCase):
    """PermissionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PermissionsApi()

    def tearDown(self) -> None:
        pass

    def test_create_data_access_sets(self) -> None:
        """Test case for create_data_access_sets

        Create shareable data access sets
        """
        pass

    def test_create_permissions(self) -> None:
        """Test case for create_permissions

        Create permissions
        """
        pass

    def test_delete_permissions(self) -> None:
        """Test case for delete_permissions

        Delete permissions
        """
        pass

    def test_get_capabilities(self) -> None:
        """Test case for get_capabilities

        Retrieve a list of all permission capabilities
        """
        pass

    def test_get_capability(self) -> None:
        """Test case for get_capability

        Retrieve a permission capability's details
        """
        pass

    def test_get_content_package(self) -> None:
        """Test case for get_content_package

        Retrieve a content package's details
        """
        pass

    def test_get_content_packages(self) -> None:
        """Test case for get_content_packages

        Retrieve a list of all content packages
        """
        pass

    def test_get_data_access_set(self) -> None:
        """Test case for get_data_access_set

        Retrieve a data access set's details
        """
        pass

    def test_get_data_access_sets(self) -> None:
        """Test case for get_data_access_sets

        Retrieve a list of all data access sets
        """
        pass

    def test_get_data_security_objects(self) -> None:
        """Test case for get_data_security_objects

        Retrieve a list of data security objects
        """
        pass

    def test_get_permission(self) -> None:
        """Test case for get_permission

        Retrieve a permission's details
        """
        pass

    def test_get_permissions(self) -> None:
        """Test case for get_permissions

        Retrieve a list of all permissions
        """
        pass

    def test_update_permissions(self) -> None:
        """Test case for update_permissions

        Update permissions
        """
        pass


if __name__ == '__main__':
    unittest.main()
