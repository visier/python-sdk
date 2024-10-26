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

from visier_api_administration.api.tenants_v2_api import TenantsV2Api


class TestTenantsV2Api(unittest.TestCase):
    """TenantsV2Api unit test stubs"""

    def setUp(self) -> None:
        self.api = TenantsV2Api()

    def tearDown(self) -> None:
        pass

    def test_create_tenant_0(self) -> None:
        """Test case for create_tenant_0

        Add an analytic tenant
        """
        pass

    def test_delete_tenant_0(self) -> None:
        """Test case for delete_tenant_0

        Deprovision an analytic tenant
        """
        pass

    def test_list_tenants_0(self) -> None:
        """Test case for list_tenants_0

        Retrieve a list of all analytic tenants
        """
        pass

    def test_tenant_info(self) -> None:
        """Test case for tenant_info

        Retrieve an analytic tenant's details
        """
        pass

    def test_update_tenant_0(self) -> None:
        """Test case for update_tenant_0

        Update an analytic tenant
        """
        pass


if __name__ == '__main__':
    unittest.main()
