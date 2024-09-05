# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.assign_connector_credential_request import AssignConnectorCredentialRequest

class TestAssignConnectorCredentialRequest(unittest.TestCase):
    """AssignConnectorCredentialRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssignConnectorCredentialRequest:
        """Test AssignConnectorCredentialRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AssignConnectorCredentialRequest`
        """
        model = AssignConnectorCredentialRequest()
        if include_optional:
            return AssignConnectorCredentialRequest(
                connectors = [
                    visier.sdk.api.data_in.models.connector.Connector(
                        connector_id = '', 
                        tenants = [
                            visier.sdk.api.data_in.models.tenant_and_credential.TenantAndCredential(
                                credential_id = '', 
                                tenant_code = '', )
                            ], )
                    ]
            )
        else:
            return AssignConnectorCredentialRequest(
        )
        """

    def testAssignConnectorCredentialRequest(self):
        """Test AssignConnectorCredentialRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
