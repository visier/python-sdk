# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.99201.1474
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.data_version_object import DataVersionObject

class TestDataVersionObject(unittest.TestCase):
    """DataVersionObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataVersionObject:
        """Test DataVersionObject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataVersionObject`
        """
        model = DataVersionObject()
        if include_optional:
            return DataVersionObject(
                data_versions = '',
                tenant_code = ''
            )
        else:
            return DataVersionObject(
        )
        """

    def testDataVersionObject(self):
        """Test DataVersionObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
