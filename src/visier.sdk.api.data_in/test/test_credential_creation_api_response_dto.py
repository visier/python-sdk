# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1418
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.credential_creation_api_response_dto import CredentialCreationAPIResponseDTO

class TestCredentialCreationAPIResponseDTO(unittest.TestCase):
    """CredentialCreationAPIResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CredentialCreationAPIResponseDTO:
        """Test CredentialCreationAPIResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CredentialCreationAPIResponseDTO`
        """
        model = CredentialCreationAPIResponseDTO()
        if include_optional:
            return CredentialCreationAPIResponseDTO(
                missing_connection_properties = [
                    visier.sdk.api.data_in.models.subject_missing_access_dto.SubjectMissingAccessDTO(
                        attributes = [
                            ''
                            ], 
                        subject = 'Employee', )
                    ],
                object_name = '',
                symbol_name = '',
                uuid = ''
            )
        else:
            return CredentialCreationAPIResponseDTO(
        )
        """

    def testCredentialCreationAPIResponseDTO(self):
        """Test CredentialCreationAPIResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
