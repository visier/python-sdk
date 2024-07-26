# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.permission_management.models.member_filter_config_dto import MemberFilterConfigDTO

class TestMemberFilterConfigDTO(unittest.TestCase):
    """MemberFilterConfigDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemberFilterConfigDTO:
        """Test MemberFilterConfigDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemberFilterConfigDTO`
        """
        model = MemberFilterConfigDTO()
        if include_optional:
            return MemberFilterConfigDTO(
                dimension_filters = [
                    visier.sdk.api.permission_management.models.dimension_filter_dto.DimensionFilterDTO(
                        dynamic_dimension_filter = visier.sdk.api.permission_management.models.dynamic_dimension_filter_dto.DynamicDimensionFilterDTO(
                            dimension_id = '', 
                            dimension_status = 'Unset', 
                            dynamic_property_mappings = [
                                visier.sdk.api.permission_management.models.dynamic_property_mapping_dto.DynamicPropertyMappingDTO(
                                    hierarchy_property_id = '', 
                                    hierarchy_property_status = 'Unset', 
                                    user_property = null, )
                                ], 
                            subject_reference_path = [
                                ''
                                ], ), 
                        static_dimension_filter = visier.sdk.api.permission_management.models.static_dimension_filter_dto.StaticDimensionFilterDTO(
                            dimension_id = '', 
                            dimension_status = 'Unset', 
                            member_selections = [
                                visier.sdk.api.permission_management.models.member_selection_dto.MemberSelectionDTO(
                                    dimension_member_status = 'Unset', 
                                    excluded = True, 
                                    name_path = [
                                        ''
                                        ], )
                                ], ), )
                    ]
            )
        else:
            return MemberFilterConfigDTO(
        )
        """

    def testMemberFilterConfigDTO(self):
        """Test MemberFilterConfigDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
