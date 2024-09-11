# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.99201.1475
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.direct_data_schema_field_dto import DirectDataSchemaFieldDTO

class TestDirectDataSchemaFieldDTO(unittest.TestCase):
    """DirectDataSchemaFieldDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DirectDataSchemaFieldDTO:
        """Test DirectDataSchemaFieldDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DirectDataSchemaFieldDTO`
        """
        model = DirectDataSchemaFieldDTO()
        if include_optional:
            return DirectDataSchemaFieldDTO(
                data_type = '',
                empty_values_allowed = True,
                formats = [
                    ''
                    ],
                is_mandatory = True,
                name = ''
            )
        else:
            return DirectDataSchemaFieldDTO(
        )
        """

    def testDirectDataSchemaFieldDTO(self):
        """Test DirectDataSchemaFieldDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
