# coding: utf-8

"""
    Visier Data and Job Handling APIs

    Visier APIs for data and job handling

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_handling.models.oracle_db_auth_params_dto import OracleDbAuthParamsDTO

class TestOracleDbAuthParamsDTO(unittest.TestCase):
    """OracleDbAuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OracleDbAuthParamsDTO:
        """Test OracleDbAuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OracleDbAuthParamsDTO`
        """
        model = OracleDbAuthParamsDTO()
        if include_optional:
            return OracleDbAuthParamsDTO(
                host = '',
                password = '',
                port = '',
                service_name = '',
                username = ''
            )
        else:
            return OracleDbAuthParamsDTO(
        )
        """

    def testOracleDbAuthParamsDTO(self):
        """Test OracleDbAuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
