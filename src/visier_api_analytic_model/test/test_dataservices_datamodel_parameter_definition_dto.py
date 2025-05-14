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
from visier_api_analytic_model.models.dataservices_datamodel_parameter_definition_dto import DataservicesDatamodelParameterDefinitionDTO

class TestDataservicesDatamodelParameterDefinitionDTO(unittest.TestCase):
    """DataservicesDatamodelParameterDefinitionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesDatamodelParameterDefinitionDTO:
        """Test DataservicesDatamodelParameterDefinitionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesDatamodelParameterDefinitionDTO(
                member_parameter = visier_api_analytic_model.models.dataservices/datamodel/member_parameter_definition_dto.dataservices.datamodel.MemberParameterDefinitionDTO(
                    id = '', 
                    display_name = '', 
                    description = '', 
                    dimension_id = '', 
                    reference_path = [
                        ''
                        ], 
                    default = None, ),
                numeric_parameter = visier_api_analytic_model.models.dataservices/datamodel/numeric_parameter_definition_dto.dataservices.datamodel.NumericParameterDefinitionDTO(
                    id = '', 
                    display_name = '', 
                    description = '', 
                    lower_bound = 1.337, 
                    upper_bound = 1.337, 
                    default = 1.337, ),
                plan_parameter = visier_api_analytic_model.models.dataservices/datamodel/plan_parameter_definition_dto.dataservices.datamodel.PlanParameterDefinitionDTO(
                    id = '', 
                    display_name = '', 
                    description = '', 
                    model_name = '', ),
                aggregation_type_parameter = visier_api_analytic_model.models.dataservices/datamodel/aggregation_type_parameter_dto.dataservices.datamodel.AggregationTypeParameterDTO(
                    id = '', 
                    display_name = '', 
                    description = '', 
                    parameter_options = [
                        visier_api_analytic_model.models.dataservices/datamodel/aggregation_type_option_dto.dataservices.datamodel.AggregationTypeOptionDTO(
                            id = '', 
                            display_name = '', 
                            property_name = '', 
                            aggregation_function = '', 
                            is_default = True, )
                        ], )
            )
        else:
            return DataservicesDatamodelParameterDefinitionDTO(
        )

    def testDataservicesDatamodelParameterDefinitionDTO(self):
        """Test DataservicesDatamodelParameterDefinitionDTO"""
        def validate_instance(instance):
            DataservicesDatamodelParameterDefinitionDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesDatamodelParameterDefinitionDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
