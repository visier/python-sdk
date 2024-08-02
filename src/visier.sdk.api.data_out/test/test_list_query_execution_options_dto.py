# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1429
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.list_query_execution_options_dto import ListQueryExecutionOptionsDTO

class TestListQueryExecutionOptionsDTO(unittest.TestCase):
    """ListQueryExecutionOptionsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListQueryExecutionOptionsDTO:
        """Test ListQueryExecutionOptionsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListQueryExecutionOptionsDTO`
        """
        model = ListQueryExecutionOptionsDTO()
        if include_optional:
            return ListQueryExecutionOptionsDTO(
                calendar_type = 'TENANT_CALENDAR',
                currency_conversion_code = '',
                currency_conversion_date = '',
                currency_conversion_mode = 'TENANT_CURRENCY_CONVERSION',
                date_time_display_mode = 'EPOCH',
                limit = 56,
                multiple_tables = True,
                omit_header = True,
                page = 56,
                query_mode = 'DEFAULT',
                record_mode = 'NORMAL'
            )
        else:
            return ListQueryExecutionOptionsDTO(
        )
        """

    def testListQueryExecutionOptionsDTO(self):
        """Test ListQueryExecutionOptionsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
