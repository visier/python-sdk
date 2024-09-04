# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.data_version_export_dto import DataVersionExportDTO

class TestDataVersionExportDTO(unittest.TestCase):
    """DataVersionExportDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataVersionExportDTO:
        """Test DataVersionExportDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataVersionExportDTO`
        """
        model = DataVersionExportDTO()
        if include_optional:
            return DataVersionExportDTO(
                uuid = '',
                timestamp = '',
                data_version_number = '',
                base_data_version_number = '',
                tables = [
                    visier.sdk.api.data_out.models.data_version_export_table_dto.DataVersionExportTableDTO(
                        name = '', 
                        common_columns = null, 
                        new_columns = null, 
                        deleted_columns = [
                            ''
                            ], )
                    ],
                new_tables = [
                    ''
                    ],
                deleted_tables = [
                    ''
                    ]
            )
        else:
            return DataVersionExportDTO(
        )
        """

    def testDataVersionExportDTO(self):
        """Test DataVersionExportDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
