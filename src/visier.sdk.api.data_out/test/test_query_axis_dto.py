# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.query_axis_dto import QueryAxisDTO

class TestQueryAxisDTO(unittest.TestCase):
    """QueryAxisDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryAxisDTO:
        """Test QueryAxisDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryAxisDTO`
        """
        model = QueryAxisDTO()
        if include_optional:
            return QueryAxisDTO(
                formula = '',
                selection_concept = visier.sdk.api.data_out.models.selection_concept_reference_dto.SelectionConceptReferenceDTO(
                    name = '', 
                    qualifying_path = '', ),
                dimension_member_selection = visier.sdk.api.data_out.models.query_dimension_member_selection_dto.QueryDimensionMemberSelectionDTO(
                    dimension = null, 
                    members = [
                        visier.sdk.api.data_out.models.dimension_member_reference_dto.DimensionMemberReferenceDTO(
                            path = [
                                ''
                                ], )
                        ], ),
                member_map_selection = visier.sdk.api.data_out.models.query_member_map_selection_dto.QueryMemberMapSelectionDTO(
                    member_map = null, 
                    target_dimension_name = '', 
                    members = [
                        visier.sdk.api.data_out.models.dimension_member_reference_dto.DimensionMemberReferenceDTO(
                            path = [
                                ''
                                ], )
                        ], ),
                numeric_ranges = visier.sdk.api.data_out.models.query_numeric_ranges_dto.QueryNumericRangesDTO(
                    property = null, 
                    ranges = '', 
                    include_negative = True, 
                    include_independent_zero_range = True, 
                    include_all_member = True, ),
                dimension_level_selection = visier.sdk.api.data_out.models.query_dimension_level_selection_dto.QueryDimensionLevelSelectionDTO(
                    dimension = null, 
                    level_ids = [
                        ''
                        ], ),
                dimension_leaf_member_selection = visier.sdk.api.data_out.models.query_dimension_leaf_selection_dto.QueryDimensionLeafSelectionDTO(
                    dimension = null, ),
                dimension_data_member_selection = visier.sdk.api.data_out.models.query_dimension_data_member_selection_dto.QueryDimensionDataMemberSelectionDTO(
                    dimension = null, ),
                dimension_level_with_uncategorized_value_selection = visier.sdk.api.data_out.models.query_dimension_level_selection_dto.QueryDimensionLevelSelectionDTO(
                    dimension = null, 
                    level_ids = [
                        ''
                        ], ),
                table_axis_options = visier.sdk.api.data_out.models.query_axis_options_dto.QueryAxisOptionsDTO(
                    member_display_mode = 'UNCHANGED', 
                    column_name = '', )
            )
        else:
            return QueryAxisDTO(
        )
        """

    def testQueryAxisDTO(self):
        """Test QueryAxisDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
