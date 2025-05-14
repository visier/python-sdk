# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1905
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_administration.api.release_version_configuration_api import ReleaseVersionConfigurationApi


class TestReleaseVersionConfigurationApi(unittest.TestCase):
    """ReleaseVersionConfigurationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReleaseVersionConfigurationApi()

    def tearDown(self) -> None:
        pass

    def test_get_available_releases(self) -> None:
        """Test case for get_available_releases

        Retrieve available product releases
        """
        pass

    def test_get_release_versions(self) -> None:
        """Test case for get_release_versions

        Retrieve active product release versions
        """
        pass

    def test_set_release_versions(self) -> None:
        """Test case for set_release_versions

        Activate product release versions
        """
        pass


if __name__ == '__main__':
    unittest.main()
