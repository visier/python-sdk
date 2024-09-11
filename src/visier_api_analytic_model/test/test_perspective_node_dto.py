# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.99201.1476
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.perspective_node_dto import PerspectiveNodeDTO

class TestPerspectiveNodeDTO(unittest.TestCase):
    """PerspectiveNodeDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PerspectiveNodeDTO:
        """Test PerspectiveNodeDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PerspectiveNodeDTO`
        """
        model = PerspectiveNodeDTO()
        if include_optional:
            return PerspectiveNodeDTO(
                analytic_object_filters = [
                    visier_api_analytic_model.models.analytic_object_filter_dto.AnalyticObjectFilterDTO(
                        analytic_object_uuid = '', 
                        dimensions = [
                            visier_api_analytic_model.models.dimension_filter_dto.DimensionFilterDTO(
                                dimension_id = '', 
                                dimension_members = [
                                    visier_api_analytic_model.models.dimension_member_dto.DimensionMemberDTO(
                                        dimension_member = [
                                            ''
                                            ], )
                                    ], 
                                symbol_name = '', )
                            ], 
                        symbol_name = '', )
                    ],
                selection_concept_uuid = '',
                symbol_name = ''
            )
        else:
            return PerspectiveNodeDTO(
        )
        """

    def testPerspectiveNodeDTO(self):
        """Test PerspectiveNodeDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
