# coding: utf-8

"""
    Visier Object Configuration APIs

    Visier APIs for managing objects in studio experience

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.object_configuration.models.perspective_configuration_dto import PerspectiveConfigurationDTO

class TestPerspectiveConfigurationDTO(unittest.TestCase):
    """PerspectiveConfigurationDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PerspectiveConfigurationDTO:
        """Test PerspectiveConfigurationDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PerspectiveConfigurationDTO`
        """
        model = PerspectiveConfigurationDTO()
        if include_optional:
            return PerspectiveConfigurationDTO(
                perspective_id = '',
                perspective_name = '',
                perspective_nodes = [
                    visier.sdk.api.object_configuration.models.perspective_node_dto.PerspectiveNodeDTO(
                        analytic_object_filters = [
                            visier.sdk.api.object_configuration.models.analytic_object_filter_dto.AnalyticObjectFilterDTO(
                                analytic_object_uuid = '', 
                                dimensions = [
                                    visier.sdk.api.object_configuration.models.dimension_filter_dto.DimensionFilterDTO(
                                        dimension_id = '', 
                                        dimension_members = [
                                            visier.sdk.api.object_configuration.models.dimension_member_dto.DimensionMemberDTO(
                                                dimension_member = [
                                                    ''
                                                    ], )
                                            ], 
                                        symbol_name = '', )
                                    ], 
                                symbol_name = '', )
                            ], 
                        selection_concept_uuid = '', 
                        symbol_name = '', )
                    ]
            )
        else:
            return PerspectiveConfigurationDTO(
        )
        """

    def testPerspectiveConfigurationDTO(self):
        """Test PerspectiveConfigurationDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
