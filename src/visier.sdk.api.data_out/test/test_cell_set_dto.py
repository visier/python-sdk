# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1418
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.cell_set_dto import CellSetDTO

class TestCellSetDTO(unittest.TestCase):
    """CellSetDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CellSetDTO:
        """Test CellSetDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CellSetDTO`
        """
        model = CellSetDTO()
        if include_optional:
            return CellSetDTO(
                axes = [
                    visier.sdk.api.data_out.models.cell_set_axis_dto.CellSetAxisDTO(
                        dimension = null, 
                        positions = [
                            visier.sdk.api.data_out.models.cell_set_axis_position_dto.CellSetAxisPositionDTO(
                                display_name = '', 
                                display_name_path = [
                                    ''
                                    ], 
                                path = [
                                    ''
                                    ], )
                            ], )
                    ],
                cells = [
                    visier.sdk.api.data_out.models.cell_dto.CellDTO(
                        coordinates = [
                            56
                            ], 
                        distribution = [
                            visier.sdk.api.data_out.models.cell_distribution_bin_dto.CellDistributionBinDTO(
                                support = '', 
                                value = '', )
                            ], 
                        support = '', 
                        value = '', )
                    ],
                lineage = visier.sdk.api.data_out.models.lineage_dto.LineageDTO(
                    cell_sets = [
                        visier.sdk.api.data_out.models.cell_set_dto.CellSetDTO(
                            axes = [
                                visier.sdk.api.data_out.models.cell_set_axis_dto.CellSetAxisDTO(
                                    dimension = null, 
                                    positions = [
                                        visier.sdk.api.data_out.models.cell_set_axis_position_dto.CellSetAxisPositionDTO(
                                            display_name = '', 
                                            display_name_path = [
                                                ''
                                                ], 
                                            path = [
                                                ''
                                                ], )
                                        ], )
                                ], 
                            cells = [
                                visier.sdk.api.data_out.models.cell_dto.CellDTO(
                                    coordinates = [
                                        56
                                        ], 
                                    distribution = [
                                        visier.sdk.api.data_out.models.cell_distribution_bin_dto.CellDistributionBinDTO(
                                            support = '', 
                                            value = '', )
                                        ], 
                                    support = '', 
                                    value = '', )
                                ], 
                            lineage = null, )
                        ], 
                    op = '', )
            )
        else:
            return CellSetDTO(
        )
        """

    def testCellSetDTO(self):
        """Test CellSetDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
