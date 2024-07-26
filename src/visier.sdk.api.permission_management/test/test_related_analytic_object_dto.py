# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.permission_management.models.related_analytic_object_dto import RelatedAnalyticObjectDTO

class TestRelatedAnalyticObjectDTO(unittest.TestCase):
    """RelatedAnalyticObjectDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RelatedAnalyticObjectDTO:
        """Test RelatedAnalyticObjectDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelatedAnalyticObjectDTO`
        """
        model = RelatedAnalyticObjectDTO()
        if include_optional:
            return RelatedAnalyticObjectDTO(
                analytic_object_id = '',
                display_name = ''
            )
        else:
            return RelatedAnalyticObjectDTO(
        )
        """

    def testRelatedAnalyticObjectDTO(self):
        """Test RelatedAnalyticObjectDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
