# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.99201.1474
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.big_query_service_account_params_dto import BigQueryServiceAccountParamsDTO

class TestBigQueryServiceAccountParamsDTO(unittest.TestCase):
    """BigQueryServiceAccountParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BigQueryServiceAccountParamsDTO:
        """Test BigQueryServiceAccountParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BigQueryServiceAccountParamsDTO`
        """
        model = BigQueryServiceAccountParamsDTO()
        if include_optional:
            return BigQueryServiceAccountParamsDTO(
                private_key = '',
                service_account_email = ''
            )
        else:
            return BigQueryServiceAccountParamsDTO(
        )
        """

    def testBigQueryServiceAccountParamsDTO(self):
        """Test BigQueryServiceAccountParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
