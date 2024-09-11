# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.99201.1476
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.start_extraction_model import StartExtractionModel

class TestStartExtractionModel(unittest.TestCase):
    """StartExtractionModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StartExtractionModel:
        """Test StartExtractionModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StartExtractionModel`
        """
        model = StartExtractionModel()
        if include_optional:
            return StartExtractionModel(
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
                    ]
            )
        else:
            return StartExtractionModel(
        )
        """

    def testStartExtractionModel(self):
        """Test StartExtractionModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
