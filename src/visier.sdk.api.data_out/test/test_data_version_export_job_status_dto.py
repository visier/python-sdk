# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1418
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.data_version_export_job_status_dto import DataVersionExportJobStatusDTO

class TestDataVersionExportJobStatusDTO(unittest.TestCase):
    """DataVersionExportJobStatusDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataVersionExportJobStatusDTO:
        """Test DataVersionExportJobStatusDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataVersionExportJobStatusDTO`
        """
        model = DataVersionExportJobStatusDTO()
        if include_optional:
            return DataVersionExportJobStatusDTO(
                completed = True,
                export_uuid = '',
                failed = True,
                job_uuid = ''
            )
        else:
            return DataVersionExportJobStatusDTO(
        )
        """

    def testDataVersionExportJobStatusDTO(self):
        """Test DataVersionExportJobStatusDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
