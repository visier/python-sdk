# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1429
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.query_filter_dto import QueryFilterDTO

class TestQueryFilterDTO(unittest.TestCase):
    """QueryFilterDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryFilterDTO:
        """Test QueryFilterDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryFilterDTO`
        """
        model = QueryFilterDTO()
        if include_optional:
            return QueryFilterDTO(
                cohort = visier.sdk.api.data_out.models.cohort_filter_dto.CohortFilterDTO(
                    exclude = True, 
                    key_group = null, 
                    time_interval = null, ),
                formula = '',
                member_set = visier.sdk.api.data_out.models.member_filter_dto.MemberFilterDTO(
                    dimension = null, 
                    values = null, ),
                selection_concept = visier.sdk.api.data_out.models.selection_concept_reference_dto.SelectionConceptReferenceDTO(
                    name = '', 
                    qualifying_path = '', )
            )
        else:
            return QueryFilterDTO(
        )
        """

    def testQueryFilterDTO(self):
        """Test QueryFilterDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
