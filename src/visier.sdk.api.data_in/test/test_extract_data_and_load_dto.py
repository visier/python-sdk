# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.extract_data_and_load_dto import ExtractDataAndLoadDTO

class TestExtractDataAndLoadDTO(unittest.TestCase):
    """ExtractDataAndLoadDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExtractDataAndLoadDTO:
        """Test ExtractDataAndLoadDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtractDataAndLoadDTO`
        """
        model = ExtractDataAndLoadDTO()
        if include_optional:
            return ExtractDataAndLoadDTO(
                tenants = [
                    ''
                    ],
                all_tenants = True,
                override_last_extraction_timestamp = '',
                publish_data_load_artifacts = True,
                run_processing_job = True,
                data_category_id = '',
                disable_artifact_generation = True,
                connector_ids = [
                    ''
                    ],
                last_extraction_time_offset_weeks = 56,
                months_to_extract = 56,
                extract_to_time_override = '',
                batch_size_override = 56,
                sql_batch_size = 56,
                force_update_existing_artifacts = True
            )
        else:
            return ExtractDataAndLoadDTO(
        )
        """

    def testExtractDataAndLoadDTO(self):
        """Test ExtractDataAndLoadDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
