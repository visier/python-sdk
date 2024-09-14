# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1482
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.dimension_member_reference_dto import DimensionMemberReferenceDTO

class TestDimensionMemberReferenceDTO(unittest.TestCase):
    """DimensionMemberReferenceDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DimensionMemberReferenceDTO:
        """Test DimensionMemberReferenceDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DimensionMemberReferenceDTO`
        """
        model = DimensionMemberReferenceDTO()
        if include_optional:
            return DimensionMemberReferenceDTO(
                path = [
                    ''
                    ]
            )
        else:
            return DimensionMemberReferenceDTO(
        )
        """

    def testDimensionMemberReferenceDTO(self):
        """Test DimensionMemberReferenceDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
