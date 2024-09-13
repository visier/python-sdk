# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1481
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.direct_data_schema_dto import DirectDataSchemaDTO

class TestDirectDataSchemaDTO(unittest.TestCase):
    """DirectDataSchemaDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DirectDataSchemaDTO:
        """Test DirectDataSchemaDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DirectDataSchemaDTO`
        """
        model = DirectDataSchemaDTO()
        if include_optional:
            return DirectDataSchemaDTO(
                var_schema = [
                    visier_api_data_in.models.direct_data_schema_field_dto.DirectDataSchemaFieldDTO(
                        data_type = '', 
                        empty_values_allowed = True, 
                        formats = [
                            ''
                            ], 
                        is_mandatory = True, 
                        name = '', )
                    ]
            )
        else:
            return DirectDataSchemaDTO(
        )
        """

    def testDirectDataSchemaDTO(self):
        """Test DirectDataSchemaDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
