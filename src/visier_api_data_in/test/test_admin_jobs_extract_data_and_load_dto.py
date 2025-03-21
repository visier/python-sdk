# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_in.models
from visier_api_data_in.models.admin_jobs_extract_data_and_load_dto import AdminJobsExtractDataAndLoadDTO

class TestAdminJobsExtractDataAndLoadDTO(unittest.TestCase):
    """AdminJobsExtractDataAndLoadDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdminJobsExtractDataAndLoadDTO:
        """Test AdminJobsExtractDataAndLoadDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return AdminJobsExtractDataAndLoadDTO(
                all_tenants = True,
                batch_size_override = 56,
                connector_ids = [
                    ''
                    ],
                data_category_id = '',
                disable_artifact_generation = True,
                excluded_tenants = [
                    ''
                    ],
                extract_to_time_override = '',
                force_update_existing_artifacts = True,
                last_extraction_time_offset_mode = '',
                last_extraction_time_offset_months = 56,
                last_extraction_time_offset_weeks = 56,
                months_to_extract = 56,
                offset_month_option = '',
                offset_week_option = '',
                override_last_extraction_timestamp = '',
                publish_data_load_artifacts = True,
                run_processing_job = True,
                spill_debug_info_detail_level_dto = 'fileAndLine',
                spill_debug_info_partitions_dto = 'spillNone',
                sql_batch_size = 56,
                tenants = [
                    ''
                    ]
            )
        else:
            return AdminJobsExtractDataAndLoadDTO(
        )

    def testAdminJobsExtractDataAndLoadDTO(self):
        """Test AdminJobsExtractDataAndLoadDTO"""
        def validate_instance(instance):
            AdminJobsExtractDataAndLoadDTO.model_validate(inst_req_only)
            instance_deserialized = AdminJobsExtractDataAndLoadDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
