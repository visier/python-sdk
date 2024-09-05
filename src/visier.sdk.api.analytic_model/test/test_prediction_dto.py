# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.analytic_model.models.prediction_dto import PredictionDTO

class TestPredictionDTO(unittest.TestCase):
    """PredictionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PredictionDTO:
        """Test PredictionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PredictionDTO`
        """
        model = PredictionDTO()
        if include_optional:
            return PredictionDTO(
                id = '',
                display_name = '',
                description = '',
                subject = '',
                subject_key = '',
                subject_parent_key = '',
                subject_filter = '',
                event = '',
                event_filter = '',
                label_property = '',
                factor_properties = [
                    ''
                    ],
                factor_dimensions = [
                    ''
                    ],
                factor_concepts = [
                    ''
                    ],
                data_start_date = '',
                data_end_date = '',
                score_name = '',
                factors_name = '',
                minimum_training_months = '',
                is_multi_tenant = True
            )
        else:
            return PredictionDTO(
        )
        """

    def testPredictionDTO(self):
        """Test PredictionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
