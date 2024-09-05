# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.data_version_export_file_dto import DataVersionExportFileDTO

class TestDataVersionExportFileDTO(unittest.TestCase):
    """DataVersionExportFileDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataVersionExportFileDTO:
        """Test DataVersionExportFileDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataVersionExportFileDTO`
        """
        model = DataVersionExportFileDTO()
        if include_optional:
            return DataVersionExportFileDTO(
                columns = [
                    visier.sdk.api.data_out.models.data_version_export_column_dto.DataVersionExportColumnDTO(
                        name = '', 
                        data_type = '', 
                        allows_null = True, 
                        is_primary_key_component = True, )
                    ],
                files = [
                    visier.sdk.api.data_out.models.data_version_export_part_file_dto.DataVersionExportPartFileDTO(
                        file_id = 56, 
                        filename = '', )
                    ]
            )
        else:
            return DataVersionExportFileDTO(
        )
        """

    def testDataVersionExportFileDTO(self):
        """Test DataVersionExportFileDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
