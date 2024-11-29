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

from visier_api_administration.api.consolidated_analytics_api import ConsolidatedAnalyticsApi


class TestConsolidatedAnalyticsApi(unittest.TestCase):
    """ConsolidatedAnalyticsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConsolidatedAnalyticsApi()

    def tearDown(self) -> None:
        pass

    def test_add_excluded_sources(self) -> None:
        """Test case for add_excluded_sources

        Add excluded sources to a consolidated analytics tenant
        """
        pass

    def test_add_source_tenants(self) -> None:
        """Test case for add_source_tenants

        Add source tenants to a consolidated analytics tenant
        """
        pass

    def test_create_tenant(self) -> None:
        """Test case for create_tenant

        Create a consolidated analytics tenant
        """
        pass

    def test_list_excluded_sources(self) -> None:
        """Test case for list_excluded_sources

        Retrieve a consolidated analytics tenant's excluded sources
        """
        pass

    def test_list_source_tenants(self) -> None:
        """Test case for list_source_tenants

        Retrieve a consolidated analytics tenant's source tenants
        """
        pass

    def test_list_tenants(self) -> None:
        """Test case for list_tenants

        Retrieve a list of all consolidated analytics tenants
        """
        pass

    def test_list_tenants_with_details(self) -> None:
        """Test case for list_tenants_with_details

        Retrieve the details of all consolidated analytics tenants
        """
        pass

    def test_remove_excluded_sources(self) -> None:
        """Test case for remove_excluded_sources

        Remove excluded sources from a consolidated analytics tenants
        """
        pass

    def test_remove_source_tenants(self) -> None:
        """Test case for remove_source_tenants

        Remove source tenants from a consolidated analytics tenants
        """
        pass

    def test_set_excluded_sources(self) -> None:
        """Test case for set_excluded_sources

        Set a consolidated analytics tenant's excluded sources
        """
        pass

    def test_set_source_tenants(self) -> None:
        """Test case for set_source_tenants

        Set a consolidated analytics tenant's source tenants
        """
        pass


if __name__ == '__main__':
    unittest.main()
