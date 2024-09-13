# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1481
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.currencies_dto import CurrenciesDTO

class TestCurrenciesDTO(unittest.TestCase):
    """CurrenciesDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CurrenciesDTO:
        """Test CurrenciesDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CurrenciesDTO`
        """
        model = CurrenciesDTO()
        if include_optional:
            return CurrenciesDTO(
                currencies = [
                    visier_api_analytic_model.models.currency_dto.CurrencyDTO(
                        currency_code = '', 
                        display_name = '', 
                        short_symbol = '', 
                        symbol = '', )
                    ]
            )
        else:
            return CurrenciesDTO(
        )
        """

    def testCurrenciesDTO(self):
        """Test CurrenciesDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
