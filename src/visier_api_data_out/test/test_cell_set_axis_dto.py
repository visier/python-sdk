# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.99201.1475
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_out.models.cell_set_axis_dto import CellSetAxisDTO

class TestCellSetAxisDTO(unittest.TestCase):
    """CellSetAxisDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CellSetAxisDTO:
        """Test CellSetAxisDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CellSetAxisDTO`
        """
        model = CellSetAxisDTO()
        if include_optional:
            return CellSetAxisDTO(
                dimension = visier_api_data_out.models.dimension_reference_dto.DimensionReferenceDTO(
                    name = '', 
                    qualifying_path = '', ),
                positions = [
                    visier_api_data_out.models.cell_set_axis_position_dto.CellSetAxisPositionDTO(
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
            return CellSetAxisDTO(
        )
        """

    def testCellSetAxisDTO(self):
        """Test CellSetAxisDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
