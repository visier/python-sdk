# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1842
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_process_concept_definition_dto import ServicingV2ObjectconfigurationProcessConceptDefinitionDTO

class TestServicingV2ObjectconfigurationProcessConceptDefinitionDTO(unittest.TestCase):
    """ServicingV2ObjectconfigurationProcessConceptDefinitionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingV2ObjectconfigurationProcessConceptDefinitionDTO:
        """Test ServicingV2ObjectconfigurationProcessConceptDefinitionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingV2ObjectconfigurationProcessConceptDefinitionDTO(
                analytic_object_name = '',
                include_with_vee = True,
                metric_list = visier_api_analytic_model.models.servicing/v2/objectconfiguration/process_concept_metric_list_dto.servicing.v2.objectconfiguration.ProcessConceptMetricListDTO(
                    metrics = [
                        visier_api_analytic_model.models.servicing/v2/objectconfiguration/metric_definition_dto.servicing.v2.objectconfiguration.MetricDefinitionDTO(
                            additive_type = 'fullyAdditive', 
                            basic_information = None, 
                            details = None, 
                            object_name = '', 
                            uuid = '', )
                        ], ),
                on_hold_concept_uuid = '',
                outcome_list = visier_api_analytic_model.models.servicing/v2/objectconfiguration/process_concept_outcome_list_dto.servicing.v2.objectconfiguration.ProcessConceptOutcomeListDTO(
                    outcomes = [
                        visier_api_analytic_model.models.servicing/v2/objectconfiguration/process_concept_outcome_dto.servicing.v2.objectconfiguration.ProcessConceptOutcomeDTO(
                            basic_information = None, 
                            mapped_member_list = None, 
                            object_name = '', 
                            outcome_semantic = 'Success', 
                            uuid = '', )
                        ], ),
                participation_concept_uuid = '',
                property_list = visier_api_analytic_model.models.servicing/v2/objectconfiguration/process_concept_property_list_dto.servicing.v2.objectconfiguration.ProcessConceptPropertyListDTO(
                    properties = [
                        visier_api_analytic_model.models.servicing/v2/objectconfiguration/property_definition_dto.servicing.v2.objectconfiguration.PropertyDefinitionDTO(
                            basic_information = None, 
                            details = None, 
                            object_name = '', 
                            uuid = '', )
                        ], ),
                stage_list = visier_api_analytic_model.models.servicing/v2/objectconfiguration/process_concept_stage_list_dto.servicing.v2.objectconfiguration.ProcessConceptStageListDTO(
                    stages = [
                        visier_api_analytic_model.models.servicing/v2/objectconfiguration/process_concept_stage_dto.servicing.v2.objectconfiguration.ProcessConceptStageDTO(
                            basic_information = None, 
                            mapped_member_list = None, 
                            object_name = '', 
                            uuid = '', )
                        ], ),
                status_dimension_object_name = '',
                tag_list = visier_api_analytic_model.models.servicing/v2/objectconfiguration/tag_reference_list_dto.servicing.v2.objectconfiguration.TagReferenceListDTO(
                    tags = [
                        visier_api_analytic_model.models.servicing/v2/objectconfiguration/tag_reference_dto.servicing.v2.objectconfiguration.TagReferenceDTO(
                            object_name = '', )
                        ], ),
                visible_in_analytics = True
            )
        else:
            return ServicingV2ObjectconfigurationProcessConceptDefinitionDTO(
        )

    def testServicingV2ObjectconfigurationProcessConceptDefinitionDTO(self):
        """Test ServicingV2ObjectconfigurationProcessConceptDefinitionDTO"""
        def validate_instance(instance):
            ServicingV2ObjectconfigurationProcessConceptDefinitionDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingV2ObjectconfigurationProcessConceptDefinitionDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
