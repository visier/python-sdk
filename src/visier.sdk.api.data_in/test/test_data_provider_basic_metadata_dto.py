# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1429
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.data_provider_basic_metadata_dto import DataProviderBasicMetadataDTO

class TestDataProviderBasicMetadataDTO(unittest.TestCase):
    """DataProviderBasicMetadataDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataProviderBasicMetadataDTO:
        """Test DataProviderBasicMetadataDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataProviderBasicMetadataDTO`
        """
        model = DataProviderBasicMetadataDTO()
        if include_optional:
            return DataProviderBasicMetadataDTO(
                can_children_inherit = True
            )
        else:
            return DataProviderBasicMetadataDTO(
        )
        """

    def testDataProviderBasicMetadataDTO(self):
        """Test DataProviderBasicMetadataDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
