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
from visier_api_analytic_model.models.servicing_publicapi_objectconfiguration_properties_change_definitions_dto import ServicingPublicapiObjectconfigurationPropertiesChangeDefinitionsDTO

class TestServicingPublicapiObjectconfigurationPropertiesChangeDefinitionsDTO(unittest.TestCase):
    """ServicingPublicapiObjectconfigurationPropertiesChangeDefinitionsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingPublicapiObjectconfigurationPropertiesChangeDefinitionsDTO:
        """Test ServicingPublicapiObjectconfigurationPropertiesChangeDefinitionsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingPublicapiObjectconfigurationPropertiesChangeDefinitionsDTO(
                properties_by_tenant = [
                    visier_api_analytic_model.models.servicing/publicapi/objectconfiguration/property_change_definitions_by_tenant_dto.servicing.publicapi.objectconfiguration.PropertyChangeDefinitionsByTenantDTO(
                        project_id = '', 
                        properties = [
                            visier_api_analytic_model.models.servicing/publicapi/objectconfiguration/property_change_definition_dto.servicing.publicapi.objectconfiguration.PropertyChangeDefinitionDTO(
                                description = '', 
                                designer_notes = '', 
                                display_name = '', 
                                explanation = '', 
                                id = '', 
                                include_with_vee = True, 
                                short_display_name = '', 
                                tags = None, 
                                type = None, )
                            ], 
                        tenant_code = '', )
                    ]
            )
        else:
            return ServicingPublicapiObjectconfigurationPropertiesChangeDefinitionsDTO(
        )

    def testServicingPublicapiObjectconfigurationPropertiesChangeDefinitionsDTO(self):
        """Test ServicingPublicapiObjectconfigurationPropertiesChangeDefinitionsDTO"""
        def validate_instance(instance):
            ServicingPublicapiObjectconfigurationPropertiesChangeDefinitionsDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingPublicapiObjectconfigurationPropertiesChangeDefinitionsDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
