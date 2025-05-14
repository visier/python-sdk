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
from visier_api_data_out.models.dataservices_query_query_axis_dto import DataservicesQueryQueryAxisDTO

class TestDataservicesQueryQueryAxisDTO(unittest.TestCase):
    """DataservicesQueryQueryAxisDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesQueryQueryAxisDTO:
        """Test DataservicesQueryQueryAxisDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesQueryQueryAxisDTO(
                formula = '',
                selection_concept = visier_api_data_out.models.dataservices/datamodel/selection_concept_reference_dto.dataservices.datamodel.SelectionConceptReferenceDTO(
                    name = '', 
                    qualifying_path = '', ),
                dimension_member_selection = visier_api_data_out.models.dataservices/query/query_dimension_member_selection_dto.dataservices.query.QueryDimensionMemberSelectionDTO(
                    dimension = None, 
                    members = [
                        visier_api_data_out.models.dataservices/common/dimension_member_reference_dto.dataservices.common.DimensionMemberReferenceDTO(
                            path = [
                                ''
                                ], 
                            member_id = '', )
                        ], ),
                member_map_selection = visier_api_data_out.models.dataservices/query/query_member_map_selection_dto.dataservices.query.QueryMemberMapSelectionDTO(
                    member_map = None, 
                    target_dimension_name = '', 
                    members = [
                        visier_api_data_out.models.dataservices/common/dimension_member_reference_dto.dataservices.common.DimensionMemberReferenceDTO(
                            path = [
                                ''
                                ], 
                            member_id = '', )
                        ], ),
                numeric_ranges = visier_api_data_out.models.dataservices/query/query_numeric_ranges_dto.dataservices.query.QueryNumericRangesDTO(
                    property = None, 
                    ranges = '', 
                    include_negative = True, 
                    include_independent_zero_range = True, 
                    include_all_member = True, ),
                dimension_level_selection = visier_api_data_out.models.dataservices/query/query_dimension_level_selection_dto.dataservices.query.QueryDimensionLevelSelectionDTO(
                    dimension = None, 
                    level_ids = [
                        ''
                        ], 
                    level_depths = [
                        56
                        ], ),
                dimension_leaf_member_selection = visier_api_data_out.models.dataservices/query/query_dimension_leaf_selection_dto.dataservices.query.QueryDimensionLeafSelectionDTO(
                    dimension = None, ),
                dimension_data_member_selection = visier_api_data_out.models.dataservices/query/query_dimension_data_member_selection_dto.dataservices.query.QueryDimensionDataMemberSelectionDTO(
                    dimension = None, ),
                dimension_level_with_uncategorized_value_selection = visier_api_data_out.models.dataservices/query/query_dimension_level_selection_dto.dataservices.query.QueryDimensionLevelSelectionDTO(
                    dimension = None, 
                    level_ids = [
                        ''
                        ], 
                    level_depths = [
                        56
                        ], ),
                table_axis_options = visier_api_data_out.models.dataservices/query/query_axis_options_dto.dataservices.query.QueryAxisOptionsDTO(
                    member_display_mode = 'UNCHANGED', 
                    column_name = '', )
            )
        else:
            return DataservicesQueryQueryAxisDTO(
        )

    def testDataservicesQueryQueryAxisDTO(self):
        """Test DataservicesQueryQueryAxisDTO"""
        def validate_instance(instance):
            DataservicesQueryQueryAxisDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesQueryQueryAxisDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
