# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.designer_transfers_data_version_export_schedule_job_request_dto import DesignerTransfersDataVersionExportScheduleJobRequestDTO

class TestDesignerTransfersDataVersionExportScheduleJobRequestDTO(unittest.TestCase):
    """DesignerTransfersDataVersionExportScheduleJobRequestDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DesignerTransfersDataVersionExportScheduleJobRequestDTO:
        """Test DesignerTransfersDataVersionExportScheduleJobRequestDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DesignerTransfersDataVersionExportScheduleJobRequestDTO(
                base_data_version_number = '',
                data_version_number = ''
            )
        else:
            return DesignerTransfersDataVersionExportScheduleJobRequestDTO(
        )

    def testDesignerTransfersDataVersionExportScheduleJobRequestDTO(self):
        """Test DesignerTransfersDataVersionExportScheduleJobRequestDTO"""
        def validate_instance(instance):
            DesignerTransfersDataVersionExportScheduleJobRequestDTO.model_validate(inst_req_only)
            instance_deserialized = DesignerTransfersDataVersionExportScheduleJobRequestDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
