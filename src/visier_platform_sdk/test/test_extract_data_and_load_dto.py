# coding: utf-8

"""
    API Reference

    Detailed API reference documentation for Visier APIs. Includes all endpoints, headers, path parameters, query parameters, request body schema, response schema, JSON request samples, and JSON response samples.

    The version of the OpenAPI document: 22222222.99201.2050
    Contact: alpine@visier.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import visier_platform_sdk.models
from visier_platform_sdk.models.extract_data_and_load_dto import ExtractDataAndLoadDTO

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
                force_update_existing_artifacts = True,
                excluded_tenants = [
                    ''
                    ],
                spill_debug_info_partitions_dto = 'spillNone',
                spill_debug_info_detail_level_dto = 'fileAndLine',
                last_extraction_time_offset_months = 56,
                last_extraction_time_offset_mode = '',
                offset_week_option = '',
                offset_month_option = '',
                credential_id = ''
            )
        else:
            return ExtractDataAndLoadDTO(
        )

    def testExtractDataAndLoadDTO(self):
        """Test ExtractDataAndLoadDTO"""
        def validate_instance(instance):
            ExtractDataAndLoadDTO.model_validate(inst_req_only)
            instance_deserialized = ExtractDataAndLoadDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
