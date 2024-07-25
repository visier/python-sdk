# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.permission_management.models.data_access_set_dto import DataAccessSetDTO

class TestDataAccessSetDTO(unittest.TestCase):
    """DataAccessSetDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataAccessSetDTO:
        """Test DataAccessSetDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataAccessSetDTO`
        """
        model = DataAccessSetDTO()
        if include_optional:
            return DataAccessSetDTO(
                analytic_object_id = '',
                description = '',
                display_name = '',
                id = '',
                property_access_configs = [
                    visier.sdk.api.permission_management.models.property_access_config_dto.PropertyAccessConfigDTO(
                        access_level = 'None', 
                        analytic_object_id = '', 
                        analytic_object_reference_paths = [
                            ''
                            ], 
                        property_id = '', 
                        property_status = 'Unset', )
                    ]
            )
        else:
            return DataAccessSetDTO(
        )
        """

    def testDataAccessSetDTO(self):
        """Test DataAccessSetDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
