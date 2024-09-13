# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1481
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_out.models.cell_distribution_bin_dto import CellDistributionBinDTO

class TestCellDistributionBinDTO(unittest.TestCase):
    """CellDistributionBinDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CellDistributionBinDTO:
        """Test CellDistributionBinDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CellDistributionBinDTO`
        """
        model = CellDistributionBinDTO()
        if include_optional:
            return CellDistributionBinDTO(
                support = '',
                value = ''
            )
        else:
            return CellDistributionBinDTO(
        )
        """

    def testCellDistributionBinDTO(self):
        """Test CellDistributionBinDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
