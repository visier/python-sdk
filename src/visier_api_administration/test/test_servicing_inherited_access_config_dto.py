# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1880
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_administration.models
from visier_api_administration.models.servicing_inherited_access_config_dto import ServicingInheritedAccessConfigDTO

class TestServicingInheritedAccessConfigDTO(unittest.TestCase):
    """ServicingInheritedAccessConfigDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingInheritedAccessConfigDTO:
        """Test ServicingInheritedAccessConfigDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingInheritedAccessConfigDTO(
                analytic_object_id = '',
                remove_access = True,
                member_filter_configs = [
                    visier_api_administration.models.servicing/member_filter_config_dto.servicing.MemberFilterConfigDTO(
                        dimension_filters = [
                            visier_api_administration.models.servicing/dimension_filter_dto.servicing.DimensionFilterDTO(
                                static_dimension_filter = visier_api_administration.models.servicing/static_dimension_filter_dto.servicing.StaticDimensionFilterDTO(
                                    dimension_id = '', 
                                    subject_reference_path = [
                                        ''
                                        ], 
                                    member_selections = [
                                        visier_api_administration.models.servicing/member_selection_dto.servicing.MemberSelectionDTO(
                                            name_path = [
                                                ''
                                                ], 
                                            excluded = True, 
                                            dimension_member_status = 'Unset', )
                                        ], 
                                    dimension_status = 'Unset', ), 
                                dynamic_dimension_filter = visier_api_administration.models.servicing/dynamic_dimension_filter_dto.servicing.DynamicDimensionFilterDTO(
                                    dimension_id = '', 
                                    dynamic_property_mappings = [
                                        visier_api_administration.models.servicing/dynamic_property_mapping_dto.servicing.DynamicPropertyMappingDTO(
                                            hierarchy_property_id = '', 
                                            user_property = None, 
                                            hierarchy_property_status = 'Unset', )
                                        ], 
                                    dimension_status = 'Unset', ), )
                            ], )
                    ]
            )
        else:
            return ServicingInheritedAccessConfigDTO(
        )

    def testServicingInheritedAccessConfigDTO(self):
        """Test ServicingInheritedAccessConfigDTO"""
        def validate_instance(instance):
            ServicingInheritedAccessConfigDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingInheritedAccessConfigDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
