# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.disable_dv_model import DisableDVModel

class TestDisableDVModel(unittest.TestCase):
    """DisableDVModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DisableDVModel:
        """Test DisableDVModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisableDVModel`
        """
        model = DisableDVModel()
        if include_optional:
            return DisableDVModel(
                data_version_objects = [
                    visier.sdk.api.data_in.models.data_version_object.DataVersionObject(
                        data_versions = '', 
                        tenant_code = '', )
                    ]
            )
        else:
            return DisableDVModel(
        )
        """

    def testDisableDVModel(self):
        """Test DisableDVModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
