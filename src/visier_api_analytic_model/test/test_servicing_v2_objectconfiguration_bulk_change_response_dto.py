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
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_bulk_change_response_dto import ServicingV2ObjectconfigurationBulkChangeResponseDTO

class TestServicingV2ObjectconfigurationBulkChangeResponseDTO(unittest.TestCase):
    """ServicingV2ObjectconfigurationBulkChangeResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingV2ObjectconfigurationBulkChangeResponseDTO:
        """Test ServicingV2ObjectconfigurationBulkChangeResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingV2ObjectconfigurationBulkChangeResponseDTO(
                successes = [
                    visier_api_analytic_model.models.servicing/v2/objectconfiguration/successful_change_dto.servicing.v2.objectconfiguration.SuccessfulChangeDTO(
                        execution_context = None, 
                        object_name = '', 
                        uuid = '', 
                        display_name = '', )
                    ],
                failures = [
                    visier_api_analytic_model.models.servicing/v2/objectconfiguration/failed_change_dto.servicing.v2.objectconfiguration.FailedChangeDTO(
                        execution_context = None, 
                        object_name = '', 
                        uuid = '', 
                        display_name = '', 
                        messages = [
                            ''
                            ], )
                    ]
            )
        else:
            return ServicingV2ObjectconfigurationBulkChangeResponseDTO(
        )

    def testServicingV2ObjectconfigurationBulkChangeResponseDTO(self):
        """Test ServicingV2ObjectconfigurationBulkChangeResponseDTO"""
        def validate_instance(instance):
            ServicingV2ObjectconfigurationBulkChangeResponseDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingV2ObjectconfigurationBulkChangeResponseDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
