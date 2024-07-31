# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.query_member_map_property_dto import QueryMemberMapPropertyDTO

class TestQueryMemberMapPropertyDTO(unittest.TestCase):
    """QueryMemberMapPropertyDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryMemberMapPropertyDTO:
        """Test QueryMemberMapPropertyDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryMemberMapPropertyDTO`
        """
        model = QueryMemberMapPropertyDTO()
        if include_optional:
            return QueryMemberMapPropertyDTO(
                member_map = visier.sdk.api.data_out.models.dimension_reference_dto.DimensionReferenceDTO(
                    name = '', 
                    qualifying_path = '', ),
                target_dimension_name = ''
            )
        else:
            return QueryMemberMapPropertyDTO(
        )
        """

    def testQueryMemberMapPropertyDTO(self):
        """Test QueryMemberMapPropertyDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
