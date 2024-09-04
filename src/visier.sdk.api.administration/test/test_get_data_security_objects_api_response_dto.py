# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.administration.models.get_data_security_objects_api_response_dto import GetDataSecurityObjectsAPIResponseDTO

class TestGetDataSecurityObjectsAPIResponseDTO(unittest.TestCase):
    """GetDataSecurityObjectsAPIResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDataSecurityObjectsAPIResponseDTO:
        """Test GetDataSecurityObjectsAPIResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDataSecurityObjectsAPIResponseDTO`
        """
        model = GetDataSecurityObjectsAPIResponseDTO()
        if include_optional:
            return GetDataSecurityObjectsAPIResponseDTO(
                analytic_objects = [
                    visier.sdk.api.administration.models.analytic_object_dto.AnalyticObjectDTO(
                        analytic_object_id = '', 
                        display_name = '', 
                        object_type = 'Event', 
                        related_objects = [
                            visier.sdk.api.administration.models.related_analytic_object_dto.RelatedAnalyticObjectDTO(
                                analytic_object_id = '', 
                                display_name = '', )
                            ], 
                        securable_properties = [
                            visier.sdk.api.administration.models.securable_property_dto.SecurablePropertyDTO(
                                property_id = '', 
                                display_name = '', 
                                analytic_object_id = '', 
                                is_primary_key = True, 
                                reference_symbol_name = '', )
                            ], 
                        securable_dimensions = [
                            visier.sdk.api.administration.models.securable_dimension_dto.SecurableDimensionDTO(
                                dimension_id = '', 
                                display_name = '', 
                                analytic_object_ids = [
                                    ''
                                    ], 
                                hierarchy_properties = [
                                    visier.sdk.api.administration.models.hierarchy_property_dto.HierarchyPropertyDTO(
                                        hierarchy_property_id = '', 
                                        display_name = '', )
                                    ], )
                            ], )
                    ]
            )
        else:
            return GetDataSecurityObjectsAPIResponseDTO(
        )
        """

    def testGetDataSecurityObjectsAPIResponseDTO(self):
        """Test GetDataSecurityObjectsAPIResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
