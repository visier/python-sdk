# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1508
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.currency_rates_dto import CurrencyRatesDTO

class TestCurrencyRatesDTO(unittest.TestCase):
    """CurrencyRatesDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CurrencyRatesDTO:
        """Test CurrencyRatesDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return CurrencyRatesDTO(
                currency_rates = [
                    visier_api_analytic_model.models.currency_rate_dto.CurrencyRateDTO(
                        end_time = '', 
                        from_currency_code = '', 
                        rate = 1.337, 
                        start_time = '', 
                        to_currency_code = '', )
                    ]
            )
        else:
            return CurrencyRatesDTO(
        )

    def testCurrencyRatesDTO(self):
        """Test CurrencyRatesDTO"""
        def validate_instance(instance):
            CurrencyRatesDTO.model_validate(inst_req_only)
            instance_deserialized = CurrencyRatesDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
