# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.99201.1474
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.member_dto import MemberDTO

class TestMemberDTO(unittest.TestCase):
    """MemberDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemberDTO:
        """Test MemberDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemberDTO`
        """
        model = MemberDTO()
        if include_optional:
            return MemberDTO(
                display_name = '',
                display_name_path = [
                    ''
                    ],
                full_name = '',
                level = 56,
                path = [
                    ''
                    ],
                validity_ranges = [
                    visier_api_analytic_model.models.validity_range_dto.ValidityRangeDTO(
                        end = '', 
                        start = '', )
                    ]
            )
        else:
            return MemberDTO(
        )
        """

    def testMemberDTO(self):
        """Test MemberDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
