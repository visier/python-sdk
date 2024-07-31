# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.include_data_uploads_request import IncludeDataUploadsRequest

class TestIncludeDataUploadsRequest(unittest.TestCase):
    """IncludeDataUploadsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IncludeDataUploadsRequest:
        """Test IncludeDataUploadsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IncludeDataUploadsRequest`
        """
        model = IncludeDataUploadsRequest()
        if include_optional:
            return IncludeDataUploadsRequest(
                model = visier.sdk.api.data_in.models.upload_to_include_model.UploadToIncludeModel(
                    uploads = [
                        visier.sdk.api.data_in.models.upload_to_include.UploadToInclude(
                            include_all = True, 
                            tenant_code = '', 
                            upload_times = [
                                ''
                                ], )
                        ], )
            )
        else:
            return IncludeDataUploadsRequest(
        )
        """

    def testIncludeDataUploadsRequest(self):
        """Test IncludeDataUploadsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
