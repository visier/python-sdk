# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.vee_visual_options_dto import VeeVisualOptionsDTO

class TestVeeVisualOptionsDTO(unittest.TestCase):
    """VeeVisualOptionsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VeeVisualOptionsDTO:
        """Test VeeVisualOptionsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VeeVisualOptionsDTO`
        """
        model = VeeVisualOptionsDTO()
        if include_optional:
            return VeeVisualOptionsDTO(
                width = 56,
                height = 56
            )
        else:
            return VeeVisualOptionsDTO(
        )
        """

    def testVeeVisualOptionsDTO(self):
        """Test VeeVisualOptionsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
