# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.99201.1475
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.disable_dv_response import DisableDVResponse

class TestDisableDVResponse(unittest.TestCase):
    """DisableDVResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DisableDVResponse:
        """Test DisableDVResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisableDVResponse`
        """
        model = DisableDVResponse()
        if include_optional:
            return DisableDVResponse(
                results = [
                    visier_api_data_in.models.result.Result(
                        data_version = '', 
                        job_id = '', 
                        message = '', 
                        status = '', 
                        tenant_code = '', )
                    ],
                total_failures = 56,
                total_success = 56
            )
        else:
            return DisableDVResponse(
        )
        """

    def testDisableDVResponse(self):
        """Test DisableDVResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
