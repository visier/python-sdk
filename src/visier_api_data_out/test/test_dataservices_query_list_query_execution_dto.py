# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1876
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.dataservices_query_list_query_execution_dto import DataservicesQueryListQueryExecutionDTO

class TestDataservicesQueryListQueryExecutionDTO(unittest.TestCase):
    """DataservicesQueryListQueryExecutionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesQueryListQueryExecutionDTO:
        """Test DataservicesQueryListQueryExecutionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesQueryListQueryExecutionDTO(
                source = visier_api_data_out.models.dataservices/query/list_query_source_dto.dataservices.query.ListQuerySourceDTO(
                    formula = '', 
                    metric = '', 
                    analytic_object = '', 
                    text_concept = '', ),
                columns = [
                    visier_api_data_out.models.dataservices/query/property_column_dto.dataservices.query.PropertyColumnDTO(
                        column_name = '', 
                        column_definition = None, )
                    ],
                sort_options = [
                    visier_api_data_out.models.dataservices/query/sort_option_dto.dataservices.query.SortOptionDTO(
                        column_index = 56, 
                        sort_direction = 'SORT_ASCENDING', )
                    ],
                filters = [
                    visier_api_data_out.models.dataservices/query/query_filter_dto.dataservices.query.QueryFilterDTO(
                        formula = '', 
                        selection_concept = None, 
                        member_set = None, 
                        cohort = None, )
                    ],
                time_interval = visier_api_data_out.models.dataservices/query/query_time_interval_dto.dataservices.query.QueryTimeIntervalDTO(
                    from_instant = '', 
                    from_date_time = '', 
                    dynamic_date_from = 'SOURCE', 
                    interval_period_type = 'MONTH', 
                    interval_period_count = 56, 
                    direction = 'BACKWARD', 
                    shift = None, ),
                parameter_values = [
                    visier_api_data_out.models.dataservices/query/query_parameter_value_dto.dataservices.query.QueryParameterValueDTO(
                        member_value = None, 
                        numeric_value = None, 
                        plan_value = None, 
                        aggregation_type_value = None, )
                    ],
                options = visier_api_data_out.models.dataservices/query/list_query_execution_options_dto.dataservices.query.ListQueryExecutionOptionsDTO(
                    limit = 56, 
                    query_mode = 'DEFAULT', 
                    omit_header = True, 
                    calendar_type = 'TENANT_CALENDAR', 
                    currency_conversion_mode = 'TENANT_CURRENCY_CONVERSION', 
                    currency_conversion_date = '', 
                    page = 56, 
                    multiple_tables = True, 
                    currency_conversion_code = '', 
                    record_mode = 'NORMAL', 
                    date_time_display_mode = 'EPOCH', )
            )
        else:
            return DataservicesQueryListQueryExecutionDTO(
        )

    def testDataservicesQueryListQueryExecutionDTO(self):
        """Test DataservicesQueryListQueryExecutionDTO"""
        def validate_instance(instance):
            DataservicesQueryListQueryExecutionDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesQueryListQueryExecutionDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
