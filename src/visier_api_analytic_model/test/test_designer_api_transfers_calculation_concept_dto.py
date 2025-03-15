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
from visier_api_analytic_model.models.designer_api_transfers_calculation_concept_dto import DesignerApiTransfersCalculationConceptDTO

class TestDesignerApiTransfersCalculationConceptDTO(unittest.TestCase):
    """DesignerApiTransfersCalculationConceptDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DesignerApiTransfersCalculationConceptDTO:
        """Test DesignerApiTransfersCalculationConceptDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DesignerApiTransfersCalculationConceptDTO(
                configuration = visier_api_analytic_model.models.designer/api/transfers/calculation_concept_configuration_dto.designer.api.transfers.CalculationConceptConfigurationDTO(
                    perspectives = [
                        visier_api_analytic_model.models.designer/api/transfers/perspective_configuration_dto.designer.api.transfers.PerspectiveConfigurationDTO(
                            perspective_id = '', 
                            perspective_name = '', 
                            perspective_nodes = [
                                visier_api_analytic_model.models.designer/api/transfers/perspective_node_dto.designer.api.transfers.PerspectiveNodeDTO(
                                    analytic_object_filters = [
                                        visier_api_analytic_model.models.designer/api/transfers/analytic_object_filter_dto.designer.api.transfers.AnalyticObjectFilterDTO(
                                            analytic_object_uuid = '', 
                                            dimensions = [
                                                visier_api_analytic_model.models.designer/api/transfers/dimension_filter_dto.designer.api.transfers.DimensionFilterDTO(
                                                    dimension_id = '', 
                                                    dimension_members = [
                                                        visier_api_analytic_model.models.designer/api/transfers/dimension_member_dto.designer.api.transfers.DimensionMemberDTO(
                                                            dimension_member = [
                                                                ''
                                                                ], )
                                                        ], 
                                                    symbol_name = '', )
                                                ], 
                                            symbol_name = '', )
                                        ], 
                                    selection_concept_uuid = '', 
                                    symbol_name = '', )
                                ], )
                        ], ),
                name = '',
                uuid = ''
            )
        else:
            return DesignerApiTransfersCalculationConceptDTO(
        )

    def testDesignerApiTransfersCalculationConceptDTO(self):
        """Test DesignerApiTransfersCalculationConceptDTO"""
        def validate_instance(instance):
            DesignerApiTransfersCalculationConceptDTO.model_validate(inst_req_only)
            instance_deserialized = DesignerApiTransfersCalculationConceptDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
