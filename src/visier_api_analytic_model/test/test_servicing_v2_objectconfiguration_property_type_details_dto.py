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
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_property_type_details_dto import ServicingV2ObjectconfigurationPropertyTypeDetailsDTO

class TestServicingV2ObjectconfigurationPropertyTypeDetailsDTO(unittest.TestCase):
    """ServicingV2ObjectconfigurationPropertyTypeDetailsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingV2ObjectconfigurationPropertyTypeDetailsDTO:
        """Test ServicingV2ObjectconfigurationPropertyTypeDetailsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingV2ObjectconfigurationPropertyTypeDetailsDTO(
                simple = visier_api_analytic_model.models.servicing/v2/objectconfiguration/simple_property_type_dto.servicing.v2.objectconfiguration.SimplePropertyTypeDTO(
                    data_type = '', 
                    primitive_type = '', ),
                calculated = visier_api_analytic_model.models.servicing/v2/objectconfiguration/calculated_property_type_dto.servicing.v2.objectconfiguration.CalculatedPropertyTypeDTO(
                    data_type = '', 
                    primitive_type = '', 
                    formula = '', ),
                process_concept = visier_api_analytic_model.models.servicing/v2/objectconfiguration/process_concept_property_type_dto.servicing.v2.objectconfiguration.ProcessConceptPropertyTypeDTO(
                    data_type = '', 
                    primitive_type = '', 
                    formula = '', )
            )
        else:
            return ServicingV2ObjectconfigurationPropertyTypeDetailsDTO(
        )

    def testServicingV2ObjectconfigurationPropertyTypeDetailsDTO(self):
        """Test ServicingV2ObjectconfigurationPropertyTypeDetailsDTO"""
        def validate_instance(instance):
            ServicingV2ObjectconfigurationPropertyTypeDetailsDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingV2ObjectconfigurationPropertyTypeDetailsDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
