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
from visier_api_analytic_model.models.servicing_objectconfiguration_property_bulk_delete_response_dto import ServicingObjectconfigurationPropertyBulkDeleteResponseDTO

class TestServicingObjectconfigurationPropertyBulkDeleteResponseDTO(unittest.TestCase):
    """ServicingObjectconfigurationPropertyBulkDeleteResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingObjectconfigurationPropertyBulkDeleteResponseDTO:
        """Test ServicingObjectconfigurationPropertyBulkDeleteResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingObjectconfigurationPropertyBulkDeleteResponseDTO(
                successes = [
                    visier_api_analytic_model.models.servicing/objectconfiguration/property_delete_success_dto.servicing.objectconfiguration.PropertyDeleteSuccessDTO(
                        id = '', 
                        display_name = '', 
                        tenant_code = '', 
                        project_id = '', 
                        derived_dependents_deleted = [
                            visier_api_analytic_model.models.servicing/objectconfiguration/dependent_dto.servicing.objectconfiguration.DependentDTO(
                                id = '', 
                                display_name = '', 
                                object_type = '', )
                            ], 
                        reference_dependents_ignored = [
                            visier_api_analytic_model.models.servicing/objectconfiguration/dependent_dto.servicing.objectconfiguration.DependentDTO(
                                id = '', 
                                display_name = '', 
                                object_type = '', )
                            ], )
                    ],
                failures = [
                    visier_api_analytic_model.models.servicing/objectconfiguration/property_delete_failure_dto.servicing.objectconfiguration.PropertyDeleteFailureDTO(
                        id = '', 
                        display_name = '', 
                        message = '', 
                        rci = '', 
                        tenant_code = '', 
                        project_id = '', 
                        derived_dependents_to_delete = [
                            visier_api_analytic_model.models.servicing/objectconfiguration/dependent_dto.servicing.objectconfiguration.DependentDTO(
                                id = '', 
                                display_name = '', 
                                object_type = '', )
                            ], 
                        reference_dependents_to_ignore = [
                            visier_api_analytic_model.models.servicing/objectconfiguration/dependent_dto.servicing.objectconfiguration.DependentDTO(
                                id = '', 
                                display_name = '', 
                                object_type = '', )
                            ], )
                    ]
            )
        else:
            return ServicingObjectconfigurationPropertyBulkDeleteResponseDTO(
        )

    def testServicingObjectconfigurationPropertyBulkDeleteResponseDTO(self):
        """Test ServicingObjectconfigurationPropertyBulkDeleteResponseDTO"""
        def validate_instance(instance):
            ServicingObjectconfigurationPropertyBulkDeleteResponseDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingObjectconfigurationPropertyBulkDeleteResponseDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
