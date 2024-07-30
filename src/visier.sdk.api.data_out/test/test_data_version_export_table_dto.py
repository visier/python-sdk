# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.data_version_export_table_dto import DataVersionExportTableDTO

class TestDataVersionExportTableDTO(unittest.TestCase):
    """DataVersionExportTableDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataVersionExportTableDTO:
        """Test DataVersionExportTableDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataVersionExportTableDTO`
        """
        model = DataVersionExportTableDTO()
        if include_optional:
            return DataVersionExportTableDTO(
                common_columns = visier.sdk.api.data_out.models.data_version_export_file_dto.DataVersionExportFileDTO(
                    columns = [
                        visier.sdk.api.data_out.models.data_version_export_column_dto.DataVersionExportColumnDTO(
                            allows_null = True, 
                            data_type = '', 
                            is_primary_key_component = True, 
                            name = '', )
                        ], 
                    files = [
                        visier.sdk.api.data_out.models.data_version_export_part_file_dto.DataVersionExportPartFileDTO(
                            file_id = 56, 
                            filename = '', )
                        ], ),
                deleted_columns = [
                    ''
                    ],
                name = '',
                new_columns = visier.sdk.api.data_out.models.data_version_export_file_dto.DataVersionExportFileDTO(
                    columns = [
                        visier.sdk.api.data_out.models.data_version_export_column_dto.DataVersionExportColumnDTO(
                            allows_null = True, 
                            data_type = '', 
                            is_primary_key_component = True, 
                            name = '', )
                        ], 
                    files = [
                        visier.sdk.api.data_out.models.data_version_export_part_file_dto.DataVersionExportPartFileDTO(
                            file_id = 56, 
                            filename = '', )
                        ], )
            )
        else:
            return DataVersionExportTableDTO(
        )
        """

    def testDataVersionExportTableDTO(self):
        """Test DataVersionExportTableDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
