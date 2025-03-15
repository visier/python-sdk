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
from visier_api_analytic_model.models.servicing_publicapi_objectconfiguration_property_bulk_delete_response_dto import ServicingPublicapiObjectconfigurationPropertyBulkDeleteResponseDTO

class TestServicingPublicapiObjectconfigurationPropertyBulkDeleteResponseDTO(unittest.TestCase):
    """ServicingPublicapiObjectconfigurationPropertyBulkDeleteResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingPublicapiObjectconfigurationPropertyBulkDeleteResponseDTO:
        """Test ServicingPublicapiObjectconfigurationPropertyBulkDeleteResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingPublicapiObjectconfigurationPropertyBulkDeleteResponseDTO(
                failures = [
                    visier_api_analytic_model.models.servicing/publicapi/objectconfiguration/property_delete_failure_dto.servicing.publicapi.objectconfiguration.PropertyDeleteFailureDTO(
                        derived_dependents_to_delete = [
                            visier_api_analytic_model.models.servicing/publicapi/objectconfiguration/dependent_dto.servicing.publicapi.objectconfiguration.DependentDTO(
                                display_name = '', 
                                id = '', 
                                object_type = '', )
                            ], 
                        display_name = '', 
                        id = '', 
                        message = '', 
                        project_id = '', 
                        rci = '', 
                        reference_dependents_to_ignore = [
                            visier_api_analytic_model.models.servicing/publicapi/objectconfiguration/dependent_dto.servicing.publicapi.objectconfiguration.DependentDTO(
                                display_name = '', 
                                id = '', 
                                object_type = '', )
                            ], 
                        tenant_code = '', )
                    ],
                successes = [
                    visier_api_analytic_model.models.servicing/publicapi/objectconfiguration/property_delete_success_dto.servicing.publicapi.objectconfiguration.PropertyDeleteSuccessDTO(
                        derived_dependents_deleted = [
                            visier_api_analytic_model.models.servicing/publicapi/objectconfiguration/dependent_dto.servicing.publicapi.objectconfiguration.DependentDTO(
                                display_name = '', 
                                id = '', 
                                object_type = '', )
                            ], 
                        display_name = '', 
                        id = '', 
                        project_id = '', 
                        reference_dependents_ignored = [
                            visier_api_analytic_model.models.servicing/publicapi/objectconfiguration/dependent_dto.servicing.publicapi.objectconfiguration.DependentDTO(
                                display_name = '', 
                                id = '', 
                                object_type = '', )
                            ], 
                        tenant_code = '', )
                    ]
            )
        else:
            return ServicingPublicapiObjectconfigurationPropertyBulkDeleteResponseDTO(
        )

    def testServicingPublicapiObjectconfigurationPropertyBulkDeleteResponseDTO(self):
        """Test ServicingPublicapiObjectconfigurationPropertyBulkDeleteResponseDTO"""
        def validate_instance(instance):
            ServicingPublicapiObjectconfigurationPropertyBulkDeleteResponseDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingPublicapiObjectconfigurationPropertyBulkDeleteResponseDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
