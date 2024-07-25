# coding: utf-8

"""
    Visier Profile Management APIs

    Visier APIs for managing the profiles assigned to users

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.profile_management.models.reduced_error_dto import ReducedErrorDTO

class TestReducedErrorDTO(unittest.TestCase):
    """ReducedErrorDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReducedErrorDTO:
        """Test ReducedErrorDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReducedErrorDTO`
        """
        model = ReducedErrorDTO()
        if include_optional:
            return ReducedErrorDTO(
                error_message = ''
            )
        else:
            return ReducedErrorDTO(
        )
        """

    def testReducedErrorDTO(self):
        """Test ReducedErrorDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
