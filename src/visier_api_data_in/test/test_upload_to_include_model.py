# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.99201.1476
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.upload_to_include_model import UploadToIncludeModel

class TestUploadToIncludeModel(unittest.TestCase):
    """UploadToIncludeModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UploadToIncludeModel:
        """Test UploadToIncludeModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UploadToIncludeModel`
        """
        model = UploadToIncludeModel()
        if include_optional:
            return UploadToIncludeModel(
                uploads = [
                    visier_api_data_in.models.upload_to_include.UploadToInclude(
                        include_all = True, 
                        max_upload_time = '', 
                        min_upload_time = '', 
                        sources = [
                            ''
                            ], 
                        tenant_code = '', 
                        upload_times = [
                            ''
                            ], )
                    ]
            )
        else:
            return UploadToIncludeModel(
        )
        """

    def testUploadToIncludeModel(self):
        """Test UploadToIncludeModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
