# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 0.0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.administration.models.property_access_config_dto import PropertyAccessConfigDTO

class TestPropertyAccessConfigDTO(unittest.TestCase):
    """PropertyAccessConfigDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PropertyAccessConfigDTO:
        """Test PropertyAccessConfigDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PropertyAccessConfigDTO`
        """
        model = PropertyAccessConfigDTO()
        if include_optional:
            return PropertyAccessConfigDTO(
                access_level = 'None',
                analytic_object_id = '',
                analytic_object_reference_paths = [
                    ''
                    ],
                property_id = '',
                property_status = 'Unset'
            )
        else:
            return PropertyAccessConfigDTO(
        )
        """

    def testPropertyAccessConfigDTO(self):
        """Test PropertyAccessConfigDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
