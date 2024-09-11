# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.99201.1475
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.workday_raas_auth_params_dto import WorkdayRaasAuthParamsDTO

class TestWorkdayRaasAuthParamsDTO(unittest.TestCase):
    """WorkdayRaasAuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkdayRaasAuthParamsDTO:
        """Test WorkdayRaasAuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkdayRaasAuthParamsDTO`
        """
        model = WorkdayRaasAuthParamsDTO()
        if include_optional:
            return WorkdayRaasAuthParamsDTO(
                domain_name = '',
                implementation_name = '',
                password = '',
                test_report_url = '',
                user_id = ''
            )
        else:
            return WorkdayRaasAuthParamsDTO(
        )
        """

    def testWorkdayRaasAuthParamsDTO(self):
        """Test WorkdayRaasAuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
