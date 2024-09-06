# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.internal_s3_auth_params_dto import InternalS3AuthParamsDTO

class TestInternalS3AuthParamsDTO(unittest.TestCase):
    """InternalS3AuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InternalS3AuthParamsDTO:
        """Test InternalS3AuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InternalS3AuthParamsDTO`
        """
        model = InternalS3AuthParamsDTO()
        if include_optional:
            return InternalS3AuthParamsDTO(
                bucket_name = '',
                path = ''
            )
        else:
            return InternalS3AuthParamsDTO(
        )
        """

    def testInternalS3AuthParamsDTO(self):
        """Test InternalS3AuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
