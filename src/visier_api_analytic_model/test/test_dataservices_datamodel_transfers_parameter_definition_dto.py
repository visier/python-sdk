# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.dataservices_datamodel_transfers_parameter_definition_dto import DataservicesDatamodelTransfersParameterDefinitionDTO

class TestDataservicesDatamodelTransfersParameterDefinitionDTO(unittest.TestCase):
    """DataservicesDatamodelTransfersParameterDefinitionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesDatamodelTransfersParameterDefinitionDTO:
        """Test DataservicesDatamodelTransfersParameterDefinitionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesDatamodelTransfersParameterDefinitionDTO(
                aggregation_type_parameter = visier_api_analytic_model.models.dataservices/datamodel/transfers/aggregation_type_parameter_dto.dataservices.datamodel.transfers.AggregationTypeParameterDTO(
                    description = '', 
                    display_name = '', 
                    id = '', 
                    parameter_options = [
                        visier_api_analytic_model.models.dataservices/datamodel/transfers/aggregation_type_option_dto.dataservices.datamodel.transfers.AggregationTypeOptionDTO(
                            aggregation_function = '', 
                            display_name = '', 
                            id = '', 
                            is_default = True, 
                            property_name = '', )
                        ], ),
                member_parameter = visier_api_analytic_model.models.dataservices/datamodel/transfers/member_parameter_definition_dto.dataservices.datamodel.transfers.MemberParameterDefinitionDTO(
                    default = None, 
                    description = '', 
                    dimension_id = '', 
                    display_name = '', 
                    id = '', 
                    reference_path = [
                        ''
                        ], ),
                numeric_parameter = visier_api_analytic_model.models.dataservices/datamodel/transfers/numeric_parameter_definition_dto.dataservices.datamodel.transfers.NumericParameterDefinitionDTO(
                    default = 1.337, 
                    description = '', 
                    display_name = '', 
                    id = '', 
                    lower_bound = 1.337, 
                    upper_bound = 1.337, ),
                plan_parameter = visier_api_analytic_model.models.dataservices/datamodel/transfers/plan_parameter_definition_dto.dataservices.datamodel.transfers.PlanParameterDefinitionDTO(
                    description = '', 
                    display_name = '', 
                    id = '', 
                    model_name = '', )
            )
        else:
            return DataservicesDatamodelTransfersParameterDefinitionDTO(
        )

    def testDataservicesDatamodelTransfersParameterDefinitionDTO(self):
        """Test DataservicesDatamodelTransfersParameterDefinitionDTO"""
        def validate_instance(instance):
            DataservicesDatamodelTransfersParameterDefinitionDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesDatamodelTransfersParameterDefinitionDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
