# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1481
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.disable_dv_request import DisableDVRequest

class TestDisableDVRequest(unittest.TestCase):
    """DisableDVRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DisableDVRequest:
        """Test DisableDVRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisableDVRequest`
        """
        model = DisableDVRequest()
        if include_optional:
            return DisableDVRequest(
                model = visier_api_data_in.models.disable_dv_model.DisableDVModel(
                    data_version_objects = [
                        visier_api_data_in.models.data_version_object.DataVersionObject(
                            data_versions = '', 
                            tenant_code = '', )
                        ], )
            )
        else:
            return DisableDVRequest(
        )
        """

    def testDisableDVRequest(self):
        """Test DisableDVRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
