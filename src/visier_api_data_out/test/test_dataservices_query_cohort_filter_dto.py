# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1808
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.dataservices_query_cohort_filter_dto import DataservicesQueryCohortFilterDTO

class TestDataservicesQueryCohortFilterDTO(unittest.TestCase):
    """DataservicesQueryCohortFilterDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesQueryCohortFilterDTO:
        """Test DataservicesQueryCohortFilterDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesQueryCohortFilterDTO(
                exclude = True,
                key_group = visier_api_data_out.models.dataservices/query/key_group_filter_dto.dataservices.query.KeyGroupFilterDTO(
                    filters = [
                        visier_api_data_out.models.dataservices/query/key_group_filter_item_dto.dataservices.query.KeyGroupFilterItemDTO(
                            formula = '', 
                            member_set = None, 
                            selection_concept = None, )
                        ], ),
                time_interval = visier_api_data_out.models.dataservices/query/query_time_interval_dto.dataservices.query.QueryTimeIntervalDTO(
                    direction = 'BACKWARD', 
                    dynamic_date_from = 'SOURCE', 
                    from_date_time = '', 
                    from_instant = '', 
                    interval_period_count = 56, 
                    interval_period_type = 'MONTH', 
                    shift = None, )
            )
        else:
            return DataservicesQueryCohortFilterDTO(
        )

    def testDataservicesQueryCohortFilterDTO(self):
        """Test DataservicesQueryCohortFilterDTO"""
        def validate_instance(instance):
            DataservicesQueryCohortFilterDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesQueryCohortFilterDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
