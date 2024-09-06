# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_in.models.consolidated_analytics_job_request_dto import ConsolidatedAnalyticsJobRequestDTO

class TestConsolidatedAnalyticsJobRequestDTO(unittest.TestCase):
    """ConsolidatedAnalyticsJobRequestDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConsolidatedAnalyticsJobRequestDTO:
        """Test ConsolidatedAnalyticsJobRequestDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConsolidatedAnalyticsJobRequestDTO`
        """
        model = ConsolidatedAnalyticsJobRequestDTO()
        if include_optional:
            return ConsolidatedAnalyticsJobRequestDTO(
                tenant_code = ''
            )
        else:
            return ConsolidatedAnalyticsJobRequestDTO(
        )
        """

    def testConsolidatedAnalyticsJobRequestDTO(self):
        """Test ConsolidatedAnalyticsJobRequestDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()