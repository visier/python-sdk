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
from visier_api_analytic_model.models.dataservices_datamodel_analytic_object_dto import DataservicesDatamodelAnalyticObjectDTO

class TestDataservicesDatamodelAnalyticObjectDTO(unittest.TestCase):
    """DataservicesDatamodelAnalyticObjectDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesDatamodelAnalyticObjectDTO:
        """Test DataservicesDatamodelAnalyticObjectDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesDatamodelAnalyticObjectDTO(
                id = '',
                display_name = '',
                description = '',
                type = 'SUBJECT',
                data_start_date = '',
                data_end_date = '',
                property_ids = [
                    ''
                    ],
                dimension_ids = [
                    ''
                    ],
                selection_concept_ids = [
                    ''
                    ],
                object_references = [
                    visier_api_analytic_model.models.dataservices/datamodel/object_reference_dto.dataservices.datamodel.ObjectReferenceDTO(
                        id = '', 
                        display_name = '', 
                        description = '', 
                        from_object = '', 
                        to_object = '', 
                        type = 'SUBJECT_REFERENCE', 
                        is_strong_reference = True, )
                    ],
                population_configuration = visier_api_analytic_model.models.dataservices/datamodel/population_configuration_dto.dataservices.datamodel.PopulationConfigurationDTO(
                    distinguishing_properties = [
                        visier_api_analytic_model.models.dataservices/datamodel/property_reference_dto.dataservices.datamodel.PropertyReferenceDTO(
                            name = '', 
                            qualifying_path = '', )
                        ], 
                    change_history_properties = [
                        visier_api_analytic_model.models.dataservices/datamodel/property_reference_dto.dataservices.datamodel.PropertyReferenceDTO(
                            name = '', 
                            qualifying_path = '', )
                        ], 
                    grouping_dimensions = [
                        visier_api_analytic_model.models.dataservices/datamodel/dimension_reference_dto.dataservices.datamodel.DimensionReferenceDTO(
                            name = '', 
                            qualifying_path = '', )
                        ], )
            )
        else:
            return DataservicesDatamodelAnalyticObjectDTO(
        )

    def testDataservicesDatamodelAnalyticObjectDTO(self):
        """Test DataservicesDatamodelAnalyticObjectDTO"""
        def validate_instance(instance):
            DataservicesDatamodelAnalyticObjectDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesDatamodelAnalyticObjectDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
