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
from visier_api_data_out.models.dataservices_query_transfers_query_time_interval_dto import DataservicesQueryTransfersQueryTimeIntervalDTO

class TestDataservicesQueryTransfersQueryTimeIntervalDTO(unittest.TestCase):
    """DataservicesQueryTransfersQueryTimeIntervalDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesQueryTransfersQueryTimeIntervalDTO:
        """Test DataservicesQueryTransfersQueryTimeIntervalDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesQueryTransfersQueryTimeIntervalDTO(
                direction = 'BACKWARD',
                dynamic_date_from = 'SOURCE',
                from_date_time = '',
                from_instant = '',
                interval_period_count = 56,
                interval_period_type = 'MONTH',
                shift = visier_api_data_out.models.dataservices/query/transfers/time_shift_dto.dataservices.query.transfers.TimeShiftDTO(
                    direction = 'BACKWARD', 
                    period_count = 56, 
                    period_type = 'MONTH', )
            )
        else:
            return DataservicesQueryTransfersQueryTimeIntervalDTO(
        )

    def testDataservicesQueryTransfersQueryTimeIntervalDTO(self):
        """Test DataservicesQueryTransfersQueryTimeIntervalDTO"""
        def validate_instance(instance):
            DataservicesQueryTransfersQueryTimeIntervalDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesQueryTransfersQueryTimeIntervalDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
