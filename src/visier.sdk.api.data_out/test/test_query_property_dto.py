# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.query_property_dto import QueryPropertyDTO

class TestQueryPropertyDTO(unittest.TestCase):
    """QueryPropertyDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryPropertyDTO:
        """Test QueryPropertyDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryPropertyDTO`
        """
        model = QueryPropertyDTO()
        if include_optional:
            return QueryPropertyDTO(
                formula = '',
                var_property = visier.sdk.api.data_out.models.property_reference_dto.PropertyReferenceDTO(
                    name = '', 
                    qualifying_path = '', ),
                selection_concept = visier.sdk.api.data_out.models.selection_concept_reference_dto.SelectionConceptReferenceDTO(
                    name = '', 
                    qualifying_path = '', ),
                dimension = visier.sdk.api.data_out.models.dimension_reference_dto.DimensionReferenceDTO(
                    name = '', 
                    qualifying_path = '', ),
                member_map_property = visier.sdk.api.data_out.models.query_member_map_property_dto.QueryMemberMapPropertyDTO(
                    member_map = null, 
                    target_dimension_name = '', ),
                effective_date_property = None
            )
        else:
            return QueryPropertyDTO(
        )
        """

    def testQueryPropertyDTO(self):
        """Test QueryPropertyDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
