# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.permission_management.models.data_access_set_failure_dto import DataAccessSetFailureDTO

class TestDataAccessSetFailureDTO(unittest.TestCase):
    """DataAccessSetFailureDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataAccessSetFailureDTO:
        """Test DataAccessSetFailureDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataAccessSetFailureDTO`
        """
        model = DataAccessSetFailureDTO()
        if include_optional:
            return DataAccessSetFailureDTO(
                data_access_set_id = '',
                display_name = '',
                error = visier.sdk.api.permission_management.models.data_access_set_error_dto.DataAccessSetErrorDTO(
                    message = '', 
                    rci = '', )
            )
        else:
            return DataAccessSetFailureDTO(
        )
        """

    def testDataAccessSetFailureDTO(self):
        """Test DataAccessSetFailureDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
