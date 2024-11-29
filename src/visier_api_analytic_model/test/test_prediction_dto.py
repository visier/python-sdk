# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1614
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.prediction_dto import PredictionDTO

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

        if include_optional:
            return PredictionDTO(
                data_end_date = '',
                data_start_date = '',
                description = '',
                display_name = '',
                event = '',
                event_filter = '',
                factor_concepts = [
                    ''
                    ],
                factor_dimensions = [
                    ''
                    ],
                factor_properties = [
                    ''
                    ],
                factors_name = '',
                id = '',
                is_multi_tenant = True,
                label_property = '',
                minimum_training_months = '',
                score_name = '',
                subject = '',
                subject_filter = '',
                subject_key = '',
                subject_parent_key = ''
            )
        else:
            return PredictionDTO(
        )

    def testPredictionDTO(self):
        """Test PredictionDTO"""
        def validate_instance(instance):
            PredictionDTO.model_validate(inst_req_only)
            instance_deserialized = PredictionDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
