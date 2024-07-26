# coding: utf-8

"""
    Visier Data Intake APIs

    Visier APIs for sending raw or untransformed source data to Visier

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_intake.models.push_data_column_definition_dto import PushDataColumnDefinitionDTO

class TestPushDataColumnDefinitionDTO(unittest.TestCase):
    """PushDataColumnDefinitionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PushDataColumnDefinitionDTO:
        """Test PushDataColumnDefinitionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PushDataColumnDefinitionDTO`
        """
        model = PushDataColumnDefinitionDTO()
        if include_optional:
            return PushDataColumnDefinitionDTO(
                allow_empty = True,
                column_name = '',
                data_formats = [
                    ''
                    ],
                data_type = '',
                default_value = '',
                is_mandatory = True
            )
        else:
            return PushDataColumnDefinitionDTO(
        )
        """

    def testPushDataColumnDefinitionDTO(self):
        """Test PushDataColumnDefinitionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
