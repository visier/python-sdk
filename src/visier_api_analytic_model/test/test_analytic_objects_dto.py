# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1482
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.models.analytic_objects_dto import AnalyticObjectsDTO

class TestAnalyticObjectsDTO(unittest.TestCase):
    """AnalyticObjectsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnalyticObjectsDTO:
        """Test AnalyticObjectsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnalyticObjectsDTO`
        """
        model = AnalyticObjectsDTO()
        if include_optional:
            return AnalyticObjectsDTO(
                analytic_objects = [
                    visier_api_analytic_model.models.analytic_object_dto.AnalyticObjectDTO(
                        data_end_date = '', 
                        data_start_date = '', 
                        description = '', 
                        dimension_ids = [
                            ''
                            ], 
                        display_name = '', 
                        id = '', 
                        object_references = [
                            visier_api_analytic_model.models.object_reference_dto.ObjectReferenceDTO(
                                description = '', 
                                display_name = '', 
                                from_object = '', 
                                id = '', 
                                is_strong_reference = True, 
                                to_object = '', 
                                type = 'SUBJECT_REFERENCE', )
                            ], 
                        population_configuration = null, 
                        property_ids = [
                            ''
                            ], 
                        selection_concept_ids = [
                            ''
                            ], 
                        type = 'SUBJECT', )
                    ]
            )
        else:
            return AnalyticObjectsDTO(
        )
        """

    def testAnalyticObjectsDTO(self):
        """Test AnalyticObjectsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
