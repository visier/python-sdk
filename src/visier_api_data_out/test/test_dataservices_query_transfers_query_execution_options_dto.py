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
from visier_api_data_out.models.dataservices_query_transfers_query_execution_options_dto import DataservicesQueryTransfersQueryExecutionOptionsDTO

class TestDataservicesQueryTransfersQueryExecutionOptionsDTO(unittest.TestCase):
    """DataservicesQueryTransfersQueryExecutionOptionsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesQueryTransfersQueryExecutionOptionsDTO:
        """Test DataservicesQueryTransfersQueryExecutionOptionsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesQueryTransfersQueryExecutionOptionsDTO(
                axes_overall_value_mode = 'NONE',
                axis_visibility = 'SIMPLE',
                calendar_type = 'TENANT_CALENDAR',
                cell_distribution_options = visier_api_data_out.models.dataservices/query/transfers/cell_distribution_options_dto.dataservices.query.transfers.CellDistributionOptionsDTO(
                    bin_count = 56, ),
                currency_conversion_code = '',
                currency_conversion_date = '',
                currency_conversion_mode = 'TENANT_CURRENCY_CONVERSION',
                enable_descending_space = True,
                enable_sparse_results = True,
                internal = visier_api_data_out.models.dataservices/query/transfers/internal_query_execution_options_dto.dataservices.query.transfers.InternalQueryExecutionOptionsDTO(
                    align_time_axis_to_period_end = True, 
                    sparse_handling_mode = 'ALLOW', ),
                lineage_depth = 56,
                member_display_mode = 'DEFAULT',
                null_visibility = 'SHOW',
                zero_visibility = 'SHOW'
            )
        else:
            return DataservicesQueryTransfersQueryExecutionOptionsDTO(
        )

    def testDataservicesQueryTransfersQueryExecutionOptionsDTO(self):
        """Test DataservicesQueryTransfersQueryExecutionOptionsDTO"""
        def validate_instance(instance):
            DataservicesQueryTransfersQueryExecutionOptionsDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesQueryTransfersQueryExecutionOptionsDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
