# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.99201.1474
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.data_load_request import DataLoadRequest

class TestDataLoadRequest(unittest.TestCase):
    """DataLoadRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataLoadRequest:
        """Test DataLoadRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataLoadRequest`
        """
        model = DataLoadRequest()
        if include_optional:
            return DataLoadRequest(
                model = visier_api_data_in.models.data_load_request_model.DataLoadRequestModel(
                    files = [
                        ''
                        ], 
                    skip_data_load = True, )
            )
        else:
            return DataLoadRequest(
        )
        """

    def testDataLoadRequest(self):
        """Test DataLoadRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
