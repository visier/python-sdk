# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.start_extraction_request import StartExtractionRequest

class TestStartExtractionRequest(unittest.TestCase):
    """StartExtractionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StartExtractionRequest:
        """Test StartExtractionRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StartExtractionRequest`
        """
        model = StartExtractionRequest()
        if include_optional:
            return StartExtractionRequest(
                model = visier_api_data_in.models.start_extraction_model.StartExtractionModel(
                    all_tenants = True, 
                    batch_size_override = 56, 
                    connector_ids = [
                        ''
                        ], 
                    data_category_id = '', 
                    disable_artifact_generation = True, 
                    extract_to_time_override = '', 
                    force_update_existing_artifacts = True, 
                    last_extraction_time_offset_weeks = 56, 
                    months_to_extract = 56, 
                    override_last_extraction_timestamp = '', 
                    publish_data_load_artifacts = True, 
                    run_processing_job = True, 
                    sql_batch_size = 56, 
                    tenants = [
                        ''
                        ], )
            )
        else:
            return StartExtractionRequest(
        )
        """

    def testStartExtractionRequest(self):
        """Test StartExtractionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()