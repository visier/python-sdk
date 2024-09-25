# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1474
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501

import unittest

from integration_tests.utils import TENANT_CODE, create_api
from visier_api_administration.api.permissions_api import PermissionsApi


class TestPermissionsApi(unittest.TestCase):
    """PermissionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = create_api(PermissionsApi)

    def tearDown(self) -> None:
        pass

    # @unittest.skip("To be implemented")
    def test_get_data_security_objects(self) -> None:
        """Test case for get_data_security_objects

        Retrieve a list of data security objects
        """

        # Retrieving all security objects
        security_objects_dto = self.api.get_data_security_objects(include_details=True, tenant_code=TENANT_CODE)

        self.assertIsNotNone(security_objects_dto)
        self.assertIsNotNone(security_objects_dto.analytic_objects)
        self.assertGreater(len(security_objects_dto.analytic_objects), 0)

        # Retrieving single security object
        analytic_object = security_objects_dto.analytic_objects[0]
        security_objects_dto = self.api.get_data_security_objects(
            id=[analytic_object.analytic_object_id],
            include_details=True,
            tenant_code=TENANT_CODE
        )

        self.assertIsNotNone(security_objects_dto)
        self.assertIsNotNone(security_objects_dto.analytic_objects)
        self.assertEqual(len(security_objects_dto.analytic_objects), 1)
        self.assertEqual(analytic_object, security_objects_dto.analytic_objects[0])

    def test_get_permissions(self) -> None:
        """Test case for get_permissions

        Retrieve a list of all permissions
        """
        permissions_dto = self.api.get_permissions(TENANT_CODE)
        self.assertIsNotNone(permissions_dto.permissions)
        self.assertGreater(len(permissions_dto.permissions), 0)


if __name__ == '__main__':
    unittest.main()
