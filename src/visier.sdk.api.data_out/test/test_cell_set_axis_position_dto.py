# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.cell_set_axis_position_dto import CellSetAxisPositionDTO

class TestCellSetAxisPositionDTO(unittest.TestCase):
    """CellSetAxisPositionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CellSetAxisPositionDTO:
        """Test CellSetAxisPositionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CellSetAxisPositionDTO`
        """
        model = CellSetAxisPositionDTO()
        if include_optional:
            return CellSetAxisPositionDTO(
                display_name = '',
                display_name_path = [
                    ''
                    ],
                path = [
                    ''
                    ]
            )
        else:
            return CellSetAxisPositionDTO(
        )
        """

    def testCellSetAxisPositionDTO(self):
        """Test CellSetAxisPositionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
