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
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_concept_type_details_dto import ServicingV2ObjectconfigurationConceptTypeDetailsDTO

class TestServicingV2ObjectconfigurationConceptTypeDetailsDTO(unittest.TestCase):
    """ServicingV2ObjectconfigurationConceptTypeDetailsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingV2ObjectconfigurationConceptTypeDetailsDTO:
        """Test ServicingV2ObjectconfigurationConceptTypeDetailsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingV2ObjectconfigurationConceptTypeDetailsDTO(
                process = visier_api_analytic_model.models.servicing/v2/objectconfiguration/process_concept_definition_dto.servicing.v2.objectconfiguration.ProcessConceptDefinitionDTO(
                    analytic_object_name = '', 
                    status_dimension_object_name = '', 
                    participation_concept_uuid = '', 
                    on_hold_concept_uuid = '', 
                    stage_list = None, 
                    outcome_list = None, 
                    metric_list = None, 
                    property_list = None, 
                    tag_list = None, 
                    visible_in_analytics = True, 
                    include_with_vee = True, )
            )
        else:
            return ServicingV2ObjectconfigurationConceptTypeDetailsDTO(
        )

    def testServicingV2ObjectconfigurationConceptTypeDetailsDTO(self):
        """Test ServicingV2ObjectconfigurationConceptTypeDetailsDTO"""
        def validate_instance(instance):
            ServicingV2ObjectconfigurationConceptTypeDetailsDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingV2ObjectconfigurationConceptTypeDetailsDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
