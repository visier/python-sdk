# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.analytic_model.models.validity_range_dto import ValidityRangeDTO

class TestValidityRangeDTO(unittest.TestCase):
    """ValidityRangeDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidityRangeDTO:
        """Test ValidityRangeDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidityRangeDTO`
        """
        model = ValidityRangeDTO()
        if include_optional:
            return ValidityRangeDTO(
                end = '',
                start = ''
            )
        else:
            return ValidityRangeDTO(
        )
        """

    def testValidityRangeDTO(self):
        """Test ValidityRangeDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
