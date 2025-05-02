# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1880
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.dataservices_datamodel_predictions_dto import DataservicesDatamodelPredictionsDTO

class TestDataservicesDatamodelPredictionsDTO(unittest.TestCase):
    """DataservicesDatamodelPredictionsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesDatamodelPredictionsDTO:
        """Test DataservicesDatamodelPredictionsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesDatamodelPredictionsDTO(
                predictions = [
                    visier_api_analytic_model.models.dataservices/datamodel/prediction_dto.dataservices.datamodel.PredictionDTO(
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
                        is_multi_tenant = True, )
                    ]
            )
        else:
            return DataservicesDatamodelPredictionsDTO(
        )

    def testDataservicesDatamodelPredictionsDTO(self):
        """Test DataservicesDatamodelPredictionsDTO"""
        def validate_instance(instance):
            DataservicesDatamodelPredictionsDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesDatamodelPredictionsDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
