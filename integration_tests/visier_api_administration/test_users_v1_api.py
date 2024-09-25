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
from visier_api_administration import UserCreationAPIRequestDTO, UserCreationAPIResponseDTO
from visier_api_administration.api.users_v1_api import UsersV1Api


class TestUsersV1Api(unittest.TestCase):
    """UsersV1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = create_api(UsersV1Api)

    def tearDown(self) -> None:
        pass

    def test_add_user(self) -> None:
        """Test case for add_user

        Add a user
        """

        # Deleting test user if exists
        test_user_email = 'creation_test_visier_python_sdk@mail.com'
        all_users_dto = self.api.get_all_users(tenant_code=TENANT_CODE)
        self.assertIsNotNone(all_users_dto)
        self.assertGreater(len(all_users_dto.users), 0)
        test_user = next((user for user in all_users_dto.users if user.email == test_user_email), None)
        if test_user:
            api_response = self.api.delete_user_with_http_info(test_user.user_id, tenant_code=TENANT_CODE)
            self.assertEqual(api_response.status_code, 204)

        creation_request_dto = UserCreationAPIRequestDTO(
            account_enabled='true',
            display_name='Creation test User Visier Python SDK',
            email=test_user_email,
            username=test_user_email
        )

        created_api_response = self.api.add_user_with_http_info(
            user_creation_api_request_dto=creation_request_dto,
            tenant_code=TENANT_CODE
        )
        self.assertEqual(created_api_response.status_code, 201)
        creation_user_dto = UserCreationAPIResponseDTO.from_json(created_api_response.raw_data.decode())
        self.assertIsNotNone(creation_user_dto)
        self.assertEqual(creation_request_dto.display_name, creation_user_dto.display_name)
        self.assertEqual(creation_request_dto.email, creation_user_dto.email)
        self.assertEqual(creation_request_dto.username, creation_user_dto.username)

    def test_get_all_users(self) -> None:
        """Test case for get_all_users

        Retrieve a list of all users
        """
        users_dto = self.api.get_all_users(tenant_code=TENANT_CODE)
        self.assertIsNotNone(users_dto)
        self.assertIsNotNone(users_dto.users)
        self.assertGreater(len(users_dto.users), 0)


if __name__ == '__main__':
    unittest.main()
