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
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_process_concept_stage_list_dto import ServicingV2ObjectconfigurationProcessConceptStageListDTO

class TestServicingV2ObjectconfigurationProcessConceptStageListDTO(unittest.TestCase):
    """ServicingV2ObjectconfigurationProcessConceptStageListDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingV2ObjectconfigurationProcessConceptStageListDTO:
        """Test ServicingV2ObjectconfigurationProcessConceptStageListDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingV2ObjectconfigurationProcessConceptStageListDTO(
                stages = [
                    visier_api_analytic_model.models.servicing/v2/objectconfiguration/process_concept_stage_dto.servicing.v2.objectconfiguration.ProcessConceptStageDTO(
                        uuid = '', 
                        object_name = '', 
                        basic_information = None, 
                        mapped_member_list = None, )
                    ]
            )
        else:
            return ServicingV2ObjectconfigurationProcessConceptStageListDTO(
        )

    def testServicingV2ObjectconfigurationProcessConceptStageListDTO(self):
        """Test ServicingV2ObjectconfigurationProcessConceptStageListDTO"""
        def validate_instance(instance):
            ServicingV2ObjectconfigurationProcessConceptStageListDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingV2ObjectconfigurationProcessConceptStageListDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
