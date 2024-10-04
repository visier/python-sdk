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

from visier_api_administration.api.profiles_api import ProfilesApi


class TestProfilesApi(unittest.TestCase):
    """ProfilesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProfilesApi()

    def tearDown(self) -> None:
        pass

    def test_assign_analytic_profile(self) -> None:
        """Test case for assign_analytic_profile

        Assign an analytic tenant profile to administrating tenant users
        """
        pass

    def test_assign_profile(self) -> None:
        """Test case for assign_profile

        Assign a profile to a list of users
        """
        pass

    def test_get_all_profiles(self) -> None:
        """Test case for get_all_profiles

        Retrieve a list of all profiles
        """
        pass

    def test_get_analytic_profile_detail(self) -> None:
        """Test case for get_analytic_profile_detail

        Retrieve the details of an analytic tenant profile
        """
        pass

    def test_get_analytic_profiles(self) -> None:
        """Test case for get_analytic_profiles

        Retrieve a list of analytic tenant profiles
        """
        pass

    def test_get_analytic_user_profile(self) -> None:
        """Test case for get_analytic_user_profile

        Retrieve an administrating tenant user's analytic tenant profiles
        """
        pass

    def test_get_profile_detail(self) -> None:
        """Test case for get_profile_detail

        Retrieve the details of a profile
        """
        pass

    def test_get_user_profile(self) -> None:
        """Test case for get_user_profile

        Retrieve a user's profiles
        """
        pass

    def test_remove_analytic_profile(self) -> None:
        """Test case for remove_analytic_profile

        Remove an analytic tenant profile from administrating tenant users
        """
        pass

    def test_remove_profile(self) -> None:
        """Test case for remove_profile

        Remove a profile from a list of users
        """
        pass


if __name__ == '__main__':
    unittest.main()
