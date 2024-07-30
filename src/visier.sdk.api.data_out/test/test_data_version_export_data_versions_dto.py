# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1418
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.data_version_export_data_versions_dto import DataVersionExportDataVersionsDTO

class TestDataVersionExportDataVersionsDTO(unittest.TestCase):
    """DataVersionExportDataVersionsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataVersionExportDataVersionsDTO:
        """Test DataVersionExportDataVersionsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataVersionExportDataVersionsDTO`
        """
        model = DataVersionExportDataVersionsDTO()
        if include_optional:
            return DataVersionExportDataVersionsDTO(
                data_versions = [
                    visier.sdk.api.data_out.models.data_version_export_data_version_summary_dto.DataVersionExportDataVersionSummaryDTO(
                        created = '', 
                        data_category = '', 
                        data_version = '', )
                    ]
            )
        else:
            return DataVersionExportDataVersionsDTO(
        )
        """

    def testDataVersionExportDataVersionsDTO(self):
        """Test DataVersionExportDataVersionsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
