# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1905
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.dataservices_datamodel_metrics_dto import DataservicesDatamodelMetricsDTO

class TestDataservicesDatamodelMetricsDTO(unittest.TestCase):
    """DataservicesDatamodelMetricsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesDatamodelMetricsDTO:
        """Test DataservicesDatamodelMetricsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesDatamodelMetricsDTO(
                metrics = [
                    visier_api_analytic_model.models.dataservices/datamodel/metric_dto.dataservices.datamodel.MetricDTO(
                        id = '', 
                        display_name = '', 
                        description = '', 
                        data_start_date = '', 
                        data_end_date = '', 
                        analytic_object_id = '', 
                        parameters = [
                            visier_api_analytic_model.models.dataservices/datamodel/parameter_definition_dto.dataservices.datamodel.ParameterDefinitionDTO(
                                member_parameter = None, 
                                numeric_parameter = None, 
                                plan_parameter = None, 
                                aggregation_type_parameter = None, )
                            ], 
                        category = 'REGULAR', 
                        visible_in_app = True, )
                    ]
            )
        else:
            return DataservicesDatamodelMetricsDTO(
        )

    def testDataservicesDatamodelMetricsDTO(self):
        """Test DataservicesDatamodelMetricsDTO"""
        def validate_instance(instance):
            DataservicesDatamodelMetricsDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesDatamodelMetricsDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
