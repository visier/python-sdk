# coding: utf-8

"""
    Visier Consolidated Analytics APIs

    Visier APIs for managing consolidated analytics (CA) tenants.

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.consolidated_analytics.api.consolidated_analytics_v1_alpha_api import ConsolidatedAnalyticsV1AlphaApi


class TestConsolidatedAnalyticsV1AlphaApi(unittest.TestCase):
    """ConsolidatedAnalyticsV1AlphaApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConsolidatedAnalyticsV1AlphaApi()

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
