# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1481
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.multiple_tenant_data_versions_details_dto import MultipleTenantDataVersionsDetailsDTO

class TestMultipleTenantDataVersionsDetailsDTO(unittest.TestCase):
    """MultipleTenantDataVersionsDetailsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MultipleTenantDataVersionsDetailsDTO:
        """Test MultipleTenantDataVersionsDetailsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MultipleTenantDataVersionsDetailsDTO`
        """
        model = MultipleTenantDataVersionsDetailsDTO()
        if include_optional:
            return MultipleTenantDataVersionsDetailsDTO(
                data_versions = [
                    visier_api_data_in.models.data_version_and_date_dto.DataVersionAndDateDTO(
                        data_version = '', 
                        data_version_date = '', )
                    ],
                tenant_code = ''
            )
        else:
            return MultipleTenantDataVersionsDetailsDTO(
        )
        """

    def testMultipleTenantDataVersionsDetailsDTO(self):
        """Test MultipleTenantDataVersionsDetailsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
