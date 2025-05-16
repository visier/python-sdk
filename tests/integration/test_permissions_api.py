import unittest

from test_utils import create_api, TENANT_CODE
from visier_platform_sdk import PermissionsApi


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
