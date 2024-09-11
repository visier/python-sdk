# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.99201.1475
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.big_query_auth_params_dto import BigQueryAuthParamsDTO

class TestBigQueryAuthParamsDTO(unittest.TestCase):
    """BigQueryAuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BigQueryAuthParamsDTO:
        """Test BigQueryAuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BigQueryAuthParamsDTO`
        """
        model = BigQueryAuthParamsDTO()
        if include_optional:
            return BigQueryAuthParamsDTO(
                client_id = '',
                client_secret = '',
                dataset_location = '',
                default_dataset = '',
                project_id = '',
                refresh_token = '',
                service_account_params = visier_api_data_in.models.big_query_service_account_params_dto.BigQueryServiceAccountParamsDTO(
                    private_key = '', 
                    service_account_email = '', )
            )
        else:
            return BigQueryAuthParamsDTO(
        )
        """

    def testBigQueryAuthParamsDTO(self):
        """Test BigQueryAuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
