# coding: utf-8

"""
    Visier Tenant Management APIs

    Visier APIs for managing tenants

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.tenant_management.models.business_location_dto import BusinessLocationDTO

class TestBusinessLocationDTO(unittest.TestCase):
    """BusinessLocationDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BusinessLocationDTO:
        """Test BusinessLocationDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BusinessLocationDTO`
        """
        model = BusinessLocationDTO()
        if include_optional:
            return BusinessLocationDTO(
                country_code = '',
                postal_code = ''
            )
        else:
            return BusinessLocationDTO(
        )
        """

    def testBusinessLocationDTO(self):
        """Test BusinessLocationDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
