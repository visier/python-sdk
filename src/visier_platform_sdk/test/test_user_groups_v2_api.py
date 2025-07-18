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

from visier_platform_sdk.api.user_groups_v2_api import UserGroupsV2Api


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
