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

from visier_api_administration.api.production_versions_api import ProductionVersionsApi


class TestProductionVersionsApi(unittest.TestCase):
    """ProductionVersionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProductionVersionsApi()

    def tearDown(self) -> None:
        pass

    def test_get_production_versions(self) -> None:
        """Test case for get_production_versions

        Retrieve a list of all production versions
        """
        pass

    def test_post_production_version(self) -> None:
        """Test case for post_production_version

        Perform an operation on a production version
        """
        pass

    def test_post_production_versions(self) -> None:
        """Test case for post_production_versions

        Perform an operation on production versions
        """
        pass


if __name__ == '__main__':
    unittest.main()
