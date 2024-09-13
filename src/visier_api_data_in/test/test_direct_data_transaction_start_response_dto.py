# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1481
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.direct_data_transaction_start_response_dto import DirectDataTransactionStartResponseDTO

class TestDirectDataTransactionStartResponseDTO(unittest.TestCase):
    """DirectDataTransactionStartResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DirectDataTransactionStartResponseDTO:
        """Test DirectDataTransactionStartResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DirectDataTransactionStartResponseDTO`
        """
        model = DirectDataTransactionStartResponseDTO()
        if include_optional:
            return DirectDataTransactionStartResponseDTO(
                transaction_id = ''
            )
        else:
            return DirectDataTransactionStartResponseDTO(
        )
        """

    def testDirectDataTransactionStartResponseDTO(self):
        """Test DirectDataTransactionStartResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
