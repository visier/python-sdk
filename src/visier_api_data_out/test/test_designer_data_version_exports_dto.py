# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1905
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.designer_data_version_exports_dto import DesignerDataVersionExportsDTO

class TestDesignerDataVersionExportsDTO(unittest.TestCase):
    """DesignerDataVersionExportsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DesignerDataVersionExportsDTO:
        """Test DesignerDataVersionExportsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DesignerDataVersionExportsDTO(
                data_version_exports = [
                    visier_api_data_out.models.designer/data_version_export_dto.designer.DataVersionExportDTO(
                        uuid = '', 
                        timestamp = '', 
                        data_version_number = '', 
                        base_data_version_number = '', 
                        tables = [
                            visier_api_data_out.models.designer/data_version_export_table_dto.designer.DataVersionExportTableDTO(
                                name = '', 
                                common_columns = None, 
                                new_columns = None, 
                                deleted_columns = [
                                    ''
                                    ], )
                            ], 
                        new_tables = [
                            ''
                            ], 
                        deleted_tables = [
                            ''
                            ], )
                    ]
            )
        else:
            return DesignerDataVersionExportsDTO(
        )

    def testDesignerDataVersionExportsDTO(self):
        """Test DesignerDataVersionExportsDTO"""
        def validate_instance(instance):
            DesignerDataVersionExportsDTO.model_validate(inst_req_only)
            instance_deserialized = DesignerDataVersionExportsDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
