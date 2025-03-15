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
from visier_api_data_out.models.dataservices_query_transfers_query_axis_dto import DataservicesQueryTransfersQueryAxisDTO

class TestDataservicesQueryTransfersQueryAxisDTO(unittest.TestCase):
    """DataservicesQueryTransfersQueryAxisDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesQueryTransfersQueryAxisDTO:
        """Test DataservicesQueryTransfersQueryAxisDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesQueryTransfersQueryAxisDTO(
                dimension_data_member_selection = visier_api_data_out.models.dataservices/query/transfers/query_dimension_data_member_selection_dto.dataservices.query.transfers.QueryDimensionDataMemberSelectionDTO(
                    dimension = None, ),
                dimension_leaf_member_selection = visier_api_data_out.models.dataservices/query/transfers/query_dimension_leaf_selection_dto.dataservices.query.transfers.QueryDimensionLeafSelectionDTO(
                    dimension = None, ),
                dimension_level_selection = visier_api_data_out.models.dataservices/query/transfers/query_dimension_level_selection_dto.dataservices.query.transfers.QueryDimensionLevelSelectionDTO(
                    dimension = None, 
                    level_ids = [
                        ''
                        ], ),
                dimension_level_with_uncategorized_value_selection = visier_api_data_out.models.dataservices/query/transfers/query_dimension_level_selection_dto.dataservices.query.transfers.QueryDimensionLevelSelectionDTO(
                    dimension = None, 
                    level_ids = [
                        ''
                        ], ),
                dimension_member_selection = visier_api_data_out.models.dataservices/query/transfers/query_dimension_member_selection_dto.dataservices.query.transfers.QueryDimensionMemberSelectionDTO(
                    dimension = None, 
                    members = [
                        visier_api_data_out.models.dataservices/common/dimension_member_reference_dto.dataservices.common.DimensionMemberReferenceDTO(
                            path = [
                                ''
                                ], )
                        ], ),
                formula = '',
                member_map_selection = visier_api_data_out.models.dataservices/query/transfers/query_member_map_selection_dto.dataservices.query.transfers.QueryMemberMapSelectionDTO(
                    member_map = None, 
                    members = [
                        visier_api_data_out.models.dataservices/common/dimension_member_reference_dto.dataservices.common.DimensionMemberReferenceDTO(
                            path = [
                                ''
                                ], )
                        ], 
                    target_dimension_name = '', ),
                numeric_ranges = visier_api_data_out.models.dataservices/query/transfers/query_numeric_ranges_dto.dataservices.query.transfers.QueryNumericRangesDTO(
                    include_all_member = True, 
                    include_independent_zero_range = True, 
                    include_negative = True, 
                    property = None, 
                    ranges = '', ),
                selection_concept = visier_api_data_out.models.dataservices/datamodel/transfers/selection_concept_reference_dto.dataservices.datamodel.transfers.SelectionConceptReferenceDTO(
                    name = '', 
                    qualifying_path = '', ),
                table_axis_options = visier_api_data_out.models.dataservices/query/transfers/query_axis_options_dto.dataservices.query.transfers.QueryAxisOptionsDTO(
                    column_name = '', 
                    member_display_mode = 'UNCHANGED', )
            )
        else:
            return DataservicesQueryTransfersQueryAxisDTO(
        )

    def testDataservicesQueryTransfersQueryAxisDTO(self):
        """Test DataservicesQueryTransfersQueryAxisDTO"""
        def validate_instance(instance):
            DataservicesQueryTransfersQueryAxisDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesQueryTransfersQueryAxisDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
