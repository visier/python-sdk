# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.dataservices_query_transfers_cell_set_axis_dto import DataservicesQueryTransfersCellSetAxisDTO

class TestDataservicesQueryTransfersCellSetAxisDTO(unittest.TestCase):
    """DataservicesQueryTransfersCellSetAxisDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesQueryTransfersCellSetAxisDTO:
        """Test DataservicesQueryTransfersCellSetAxisDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesQueryTransfersCellSetAxisDTO(
                dimension = visier_api_data_out.models.dataservices/datamodel/transfers/dimension_reference_dto.dataservices.datamodel.transfers.DimensionReferenceDTO(
                    name = '', 
                    qualifying_path = '', ),
                positions = [
                    visier_api_data_out.models.dataservices/query/transfers/cell_set_axis_position_dto.dataservices.query.transfers.CellSetAxisPositionDTO(
                        display_name = '', 
                        display_name_path = [
                            ''
                            ], 
                        path = [
                            ''
                            ], )
                    ]
            )
        else:
            return DataservicesQueryTransfersCellSetAxisDTO(
        )

    def testDataservicesQueryTransfersCellSetAxisDTO(self):
        """Test DataservicesQueryTransfersCellSetAxisDTO"""
        def validate_instance(instance):
            DataservicesQueryTransfersCellSetAxisDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesQueryTransfersCellSetAxisDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
