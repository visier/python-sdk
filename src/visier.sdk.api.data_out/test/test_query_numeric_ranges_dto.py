# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1429
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.query_numeric_ranges_dto import QueryNumericRangesDTO

class TestQueryNumericRangesDTO(unittest.TestCase):
    """QueryNumericRangesDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryNumericRangesDTO:
        """Test QueryNumericRangesDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryNumericRangesDTO`
        """
        model = QueryNumericRangesDTO()
        if include_optional:
            return QueryNumericRangesDTO(
                include_all_member = True,
                include_independent_zero_range = True,
                include_negative = True,
                var_property = visier.sdk.api.data_out.models.query_property_dto.QueryPropertyDTO(
                    dimension = null, 
                    effective_date_property = null, 
                    formula = '', 
                    member_map_property = null, 
                    property = null, 
                    selection_concept = null, ),
                ranges = ''
            )
        else:
            return QueryNumericRangesDTO(
        )
        """

    def testQueryNumericRangesDTO(self):
        """Test QueryNumericRangesDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
