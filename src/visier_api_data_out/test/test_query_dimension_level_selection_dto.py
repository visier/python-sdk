# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.99201.1474
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_out.models.query_dimension_level_selection_dto import QueryDimensionLevelSelectionDTO

class TestQueryDimensionLevelSelectionDTO(unittest.TestCase):
    """QueryDimensionLevelSelectionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryDimensionLevelSelectionDTO:
        """Test QueryDimensionLevelSelectionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryDimensionLevelSelectionDTO`
        """
        model = QueryDimensionLevelSelectionDTO()
        if include_optional:
            return QueryDimensionLevelSelectionDTO(
                dimension = visier_api_data_out.models.dimension_reference_dto.DimensionReferenceDTO(
                    name = '', 
                    qualifying_path = '', ),
                level_ids = [
                    ''
                    ]
            )
        else:
            return QueryDimensionLevelSelectionDTO(
        )
        """

    def testQueryDimensionLevelSelectionDTO(self):
        """Test QueryDimensionLevelSelectionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
