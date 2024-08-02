# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1429
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.data_version_export_schedule_job_request_dto import DataVersionExportScheduleJobRequestDTO

class TestDataVersionExportScheduleJobRequestDTO(unittest.TestCase):
    """DataVersionExportScheduleJobRequestDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataVersionExportScheduleJobRequestDTO:
        """Test DataVersionExportScheduleJobRequestDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataVersionExportScheduleJobRequestDTO`
        """
        model = DataVersionExportScheduleJobRequestDTO()
        if include_optional:
            return DataVersionExportScheduleJobRequestDTO(
                base_data_version_number = '',
                data_version_number = ''
            )
        else:
            return DataVersionExportScheduleJobRequestDTO(
        )
        """

    def testDataVersionExportScheduleJobRequestDTO(self):
        """Test DataVersionExportScheduleJobRequestDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
