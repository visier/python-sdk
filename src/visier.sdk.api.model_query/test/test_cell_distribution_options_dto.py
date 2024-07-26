# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.model_query.models.cell_distribution_options_dto import CellDistributionOptionsDTO

class TestCellDistributionOptionsDTO(unittest.TestCase):
    """CellDistributionOptionsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CellDistributionOptionsDTO:
        """Test CellDistributionOptionsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CellDistributionOptionsDTO`
        """
        model = CellDistributionOptionsDTO()
        if include_optional:
            return CellDistributionOptionsDTO(
                bin_count = 56
            )
        else:
            return CellDistributionOptionsDTO(
        )
        """

    def testCellDistributionOptionsDTO(self):
        """Test CellDistributionOptionsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
