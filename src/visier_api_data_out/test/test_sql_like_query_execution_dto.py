# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1614
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.sql_like_query_execution_dto import SqlLikeQueryExecutionDTO

class TestSqlLikeQueryExecutionDTO(unittest.TestCase):
    """SqlLikeQueryExecutionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SqlLikeQueryExecutionDTO:
        """Test SqlLikeQueryExecutionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return SqlLikeQueryExecutionDTO(
                options = visier_api_data_out.models.query_execution_options_dto.QueryExecutionOptionsDTO(
                    axis_visibility = 'SIMPLE', 
                    calendar_type = 'TENANT_CALENDAR', 
                    cell_distribution_options = visier_api_data_out.models.cell_distribution_options_dto.CellDistributionOptionsDTO(
                        bin_count = 56, ), 
                    currency_conversion_code = '', 
                    currency_conversion_date = '', 
                    currency_conversion_mode = 'TENANT_CURRENCY_CONVERSION', 
                    enable_descending_space = True, 
                    enable_sparse_results = True, 
                    internal = visier_api_data_out.models.internal_query_execution_options_dto.InternalQueryExecutionOptionsDTO(
                        align_time_axis_to_period_end = True, 
                        sparse_handling_mode = 'ALLOW', ), 
                    lineage_depth = 56, 
                    member_display_mode = 'DEFAULT', 
                    null_visibility = 'SHOW', 
                    zero_visibility = 'SHOW', ),
                query = ''
            )
        else:
            return SqlLikeQueryExecutionDTO(
        )

    def testSqlLikeQueryExecutionDTO(self):
        """Test SqlLikeQueryExecutionDTO"""
        def validate_instance(instance):
            SqlLikeQueryExecutionDTO.model_validate(inst_req_only)
            instance_deserialized = SqlLikeQueryExecutionDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
