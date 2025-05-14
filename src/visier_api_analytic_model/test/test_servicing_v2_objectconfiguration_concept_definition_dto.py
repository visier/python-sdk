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
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_concept_definition_dto import ServicingV2ObjectconfigurationConceptDefinitionDTO

class TestServicingV2ObjectconfigurationConceptDefinitionDTO(unittest.TestCase):
    """ServicingV2ObjectconfigurationConceptDefinitionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingV2ObjectconfigurationConceptDefinitionDTO:
        """Test ServicingV2ObjectconfigurationConceptDefinitionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingV2ObjectconfigurationConceptDefinitionDTO(
                uuid = '',
                object_name = '',
                basic_information = visier_api_analytic_model.models.servicing/v2/objectconfiguration/basic_information_dto.servicing.v2.objectconfiguration.BasicInformationDTO(
                    display_name = '', 
                    short_display_name = '', 
                    description = '', 
                    explanation = '', 
                    designer_notes = '', 
                    synonym_list = None, ),
                details = visier_api_analytic_model.models.servicing/v2/objectconfiguration/concept_type_details_dto.servicing.v2.objectconfiguration.ConceptTypeDetailsDTO(
                    process = None, )
            )
        else:
            return ServicingV2ObjectconfigurationConceptDefinitionDTO(
        )

    def testServicingV2ObjectconfigurationConceptDefinitionDTO(self):
        """Test ServicingV2ObjectconfigurationConceptDefinitionDTO"""
        def validate_instance(instance):
            ServicingV2ObjectconfigurationConceptDefinitionDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingV2ObjectconfigurationConceptDefinitionDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
