# coding: utf-8

"""
    Visier User Management APIs

    Visier APIs for managing users within an organization

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.user_management.models.user_creation_api_response_dto import UserCreationAPIResponseDTO

class TestUserCreationAPIResponseDTO(unittest.TestCase):
    """UserCreationAPIResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserCreationAPIResponseDTO:
        """Test UserCreationAPIResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserCreationAPIResponseDTO`
        """
        model = UserCreationAPIResponseDTO()
        if include_optional:
            return UserCreationAPIResponseDTO(
                account_enabled = '',
                display_name = '',
                email = '',
                employee_id = '',
                user_id = '',
                username = ''
            )
        else:
            return UserCreationAPIResponseDTO(
        )
        """

    def testUserCreationAPIResponseDTO(self):
        """Test UserCreationAPIResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
