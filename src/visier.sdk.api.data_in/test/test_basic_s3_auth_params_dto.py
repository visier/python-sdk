# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.basic_s3_auth_params_dto import BasicS3AuthParamsDTO

class TestBasicS3AuthParamsDTO(unittest.TestCase):
    """BasicS3AuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BasicS3AuthParamsDTO:
        """Test BasicS3AuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BasicS3AuthParamsDTO`
        """
        model = BasicS3AuthParamsDTO()
        if include_optional:
            return BasicS3AuthParamsDTO(
                access_key = '',
                bucket_name = '',
                bucket_region = '',
                path = '',
                secret_key = ''
            )
        else:
            return BasicS3AuthParamsDTO(
        )
        """

    def testBasicS3AuthParamsDTO(self):
        """Test BasicS3AuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
