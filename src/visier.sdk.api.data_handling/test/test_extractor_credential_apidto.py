# coding: utf-8

"""
    Visier Data and Job Handling APIs

    Visier APIs for data and job handling

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_handling.models.extractor_credential_apidto import ExtractorCredentialAPIDTO

class TestExtractorCredentialAPIDTO(unittest.TestCase):
    """ExtractorCredentialAPIDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExtractorCredentialAPIDTO:
        """Test ExtractorCredentialAPIDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtractorCredentialAPIDTO`
        """
        model = ExtractorCredentialAPIDTO()
        if include_optional:
            return ExtractorCredentialAPIDTO(
                auth_context = '',
                credential_id = '',
                data_provider = '',
                display_name = '',
                is_inherited = True
            )
        else:
            return ExtractorCredentialAPIDTO(
        )
        """

    def testExtractorCredentialAPIDTO(self):
        """Test ExtractorCredentialAPIDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
