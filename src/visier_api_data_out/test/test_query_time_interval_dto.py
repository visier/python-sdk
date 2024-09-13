# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1481
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_out.models.query_time_interval_dto import QueryTimeIntervalDTO

class TestQueryTimeIntervalDTO(unittest.TestCase):
    """QueryTimeIntervalDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryTimeIntervalDTO:
        """Test QueryTimeIntervalDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryTimeIntervalDTO`
        """
        model = QueryTimeIntervalDTO()
        if include_optional:
            return QueryTimeIntervalDTO(
                direction = 'BACKWARD',
                dynamic_date_from = '',
                from_date_time = '',
                from_instant = '',
                interval_period_count = 56,
                interval_period_type = 'MONTH',
                shift = visier_api_data_out.models.time_shift_dto.TimeShiftDTO(
                    direction = 'BACKWARD', 
                    period_count = 56, 
                    period_type = 'MONTH', )
            )
        else:
            return QueryTimeIntervalDTO(
        )
        """

    def testQueryTimeIntervalDTO(self):
        """Test QueryTimeIntervalDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
