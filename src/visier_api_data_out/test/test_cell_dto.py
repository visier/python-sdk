# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_out.models.cell_dto import CellDTO

class TestCellDTO(unittest.TestCase):
    """CellDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CellDTO:
        """Test CellDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CellDTO`
        """
        model = CellDTO()
        if include_optional:
            return CellDTO(
                coordinates = [
                    56
                    ],
                distribution = [
                    visier_api_data_out.models.cell_distribution_bin_dto.CellDistributionBinDTO(
                        support = '', 
                        value = '', )
                    ],
                support = '',
                value = ''
            )
        else:
            return CellDTO(
        )
        """

    def testCellDTO(self):
        """Test CellDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()