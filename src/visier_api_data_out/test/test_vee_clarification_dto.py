# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.99201.1476
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_out.models.vee_clarification_dto import VeeClarificationDTO

class TestVeeClarificationDTO(unittest.TestCase):
    """VeeClarificationDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VeeClarificationDTO:
        """Test VeeClarificationDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VeeClarificationDTO`
        """
        model = VeeClarificationDTO()
        if include_optional:
            return VeeClarificationDTO(
                attributes = [
                    ''
                    ],
                dimensions = [
                    ''
                    ],
                filters = [
                    ''
                    ],
                message = '',
                metrics = [
                    ''
                    ],
                questions = [
                    ''
                    ]
            )
        else:
            return VeeClarificationDTO(
        )
        """

    def testVeeClarificationDTO(self):
        """Test VeeClarificationDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
