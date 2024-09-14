# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1482
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.workday_auth_params_dto import WorkdayAuthParamsDTO

class TestWorkdayAuthParamsDTO(unittest.TestCase):
    """WorkdayAuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkdayAuthParamsDTO:
        """Test WorkdayAuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkdayAuthParamsDTO`
        """
        model = WorkdayAuthParamsDTO()
        if include_optional:
            return WorkdayAuthParamsDTO(
                api_key = '',
                domain_name = '',
                implementation_name = '',
                integration_system_id = '',
                o_auth = visier_api_data_in.models.workday_o_auth_params_dto.WorkdayOAuthParamsDTO(
                    api_client_id = '', 
                    private_x509_key = '', 
                    public_x509_cert = '', ),
                password = '',
                ref_token = visier_api_data_in.models.workday_refresh_token_params_dto.WorkdayRefreshTokenParamsDTO(
                    api_client_id = '', 
                    client_secret = '', 
                    refresh_token = '', ),
                user_id = ''
            )
        else:
            return WorkdayAuthParamsDTO(
        )
        """

    def testWorkdayAuthParamsDTO(self):
        """Test WorkdayAuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
