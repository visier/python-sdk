# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1547
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_administration.api.tenants_v1_api import TenantsV1Api


class TestTenantsV1Api(unittest.TestCase):
    """TenantsV1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = TenantsV1Api()

    def tearDown(self) -> None:
        pass

    def test_add_tenant(self) -> None:
        """Test case for add_tenant

        Add an analytic tenant
        """
        pass

    def test_delete_tenant(self) -> None:
        """Test case for delete_tenant

        Deprovision an analytic tenant
        """
        pass

    def test_disable_tenant(self) -> None:
        """Test case for disable_tenant

        Disable an analytic tenant
        """
        pass

    def test_enable_tenant(self) -> None:
        """Test case for enable_tenant

        Enable an analytic tenant
        """
        pass

    def test_get_tenant(self) -> None:
        """Test case for get_tenant

        Retrieve an analytic tenant's details
        """
        pass

    def test_get_tenants(self) -> None:
        """Test case for get_tenants

        Retrieve a list of all analytic tenants
        """
        pass

    def test_update_tenant(self) -> None:
        """Test case for update_tenant

        Update an analytic tenant
        """
        pass

    def test_validate_tenant(self) -> None:
        """Test case for validate_tenant

        Validate an analytic tenant's metric values
        """
        pass

    def test_validate_tenants(self) -> None:
        """Test case for validate_tenants

        Validate metric values for all analytic tenants
        """
        pass


if __name__ == '__main__':
    unittest.main()
