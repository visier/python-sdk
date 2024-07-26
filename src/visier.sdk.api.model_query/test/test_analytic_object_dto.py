# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.model_query.models.analytic_object_dto import AnalyticObjectDTO

class TestAnalyticObjectDTO(unittest.TestCase):
    """AnalyticObjectDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnalyticObjectDTO:
        """Test AnalyticObjectDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnalyticObjectDTO`
        """
        model = AnalyticObjectDTO()
        if include_optional:
            return AnalyticObjectDTO(
                data_end_date = '',
                data_start_date = '',
                description = '',
                dimension_ids = [
                    ''
                    ],
                display_name = '',
                id = '',
                object_references = [
                    visier.sdk.api.model_query.models.object_reference_dto.ObjectReferenceDTO(
                        description = '', 
                        display_name = '', 
                        from_object = '', 
                        id = '', 
                        is_strong_reference = True, 
                        to_object = '', 
                        type = 'SUBJECT_REFERENCE', )
                    ],
                population_configuration = visier.sdk.api.model_query.models.population_configuration_dto.PopulationConfigurationDTO(
                    change_history_properties = [
                        visier.sdk.api.model_query.models.property_reference_dto.PropertyReferenceDTO(
                            name = '', 
                            qualifying_path = '', )
                        ], 
                    distinguishing_properties = [
                        visier.sdk.api.model_query.models.property_reference_dto.PropertyReferenceDTO(
                            name = '', 
                            qualifying_path = '', )
                        ], 
                    grouping_dimensions = [
                        visier.sdk.api.model_query.models.dimension_reference_dto.DimensionReferenceDTO(
                            name = '', 
                            qualifying_path = '', )
                        ], ),
                property_ids = [
                    ''
                    ],
                selection_concept_ids = [
                    ''
                    ],
                type = 'SUBJECT'
            )
        else:
            return AnalyticObjectDTO(
        )
        """

    def testAnalyticObjectDTO(self):
        """Test AnalyticObjectDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
