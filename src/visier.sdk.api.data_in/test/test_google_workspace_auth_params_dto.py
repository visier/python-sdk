# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1429
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.google_workspace_auth_params_dto import GoogleWorkspaceAuthParamsDTO

class TestGoogleWorkspaceAuthParamsDTO(unittest.TestCase):
    """GoogleWorkspaceAuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoogleWorkspaceAuthParamsDTO:
        """Test GoogleWorkspaceAuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoogleWorkspaceAuthParamsDTO`
        """
        model = GoogleWorkspaceAuthParamsDTO()
        if include_optional:
            return GoogleWorkspaceAuthParamsDTO(
                auth_code = '',
                client_id = '',
                client_secret = '',
                privacy_mode = '',
                service_account = ''
            )
        else:
            return GoogleWorkspaceAuthParamsDTO(
        )
        """

    def testGoogleWorkspaceAuthParamsDTO(self):
        """Test GoogleWorkspaceAuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
