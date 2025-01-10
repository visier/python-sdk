# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1656
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.query_property_dto import QueryPropertyDTO

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

        if include_optional:
            return QueryPropertyDTO(
                dimension = visier_api_data_out.models.dimension_reference_dto.DimensionReferenceDTO(
                    name = '', 
                    qualifying_path = '', ),
                dimension_level_selection = visier_api_data_out.models.query_dimension_level_property_dto.QueryDimensionLevelPropertyDTO(
                    dimension = None, 
                    level_depth = 56, 
                    level_id = '', 
                    member_value_mode = 'NAME', ),
                effective_date_property = None,
                formula = '',
                member_map_property = visier_api_data_out.models.query_member_map_property_dto.QueryMemberMapPropertyDTO(
                    member_map = None, 
                    target_dimension_name = '', ),
                var_property = visier_api_data_out.models.property_reference_dto.PropertyReferenceDTO(
                    name = '', 
                    qualifying_path = '', ),
                selection_concept = visier_api_data_out.models.selection_concept_reference_dto.SelectionConceptReferenceDTO(
                    name = '', 
                    qualifying_path = '', )
            )
        else:
            return QueryPropertyDTO(
        )

    def testQueryPropertyDTO(self):
        """Test QueryPropertyDTO"""
        def validate_instance(instance):
            QueryPropertyDTO.model_validate(inst_req_only)
            instance_deserialized = QueryPropertyDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
