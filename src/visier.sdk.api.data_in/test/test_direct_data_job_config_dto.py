# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.models.direct_data_job_config_dto import DirectDataJobConfigDTO

class TestDirectDataJobConfigDTO(unittest.TestCase):
    """DirectDataJobConfigDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DirectDataJobConfigDTO:
        """Test DirectDataJobConfigDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DirectDataJobConfigDTO`
        """
        model = DirectDataJobConfigDTO()
        if include_optional:
            return DirectDataJobConfigDTO(
                extend_objects = [
                    ''
                    ],
                supplemental_mode = 'UNCHANGED'
            )
        else:
            return DirectDataJobConfigDTO(
        )
        """

    def testDirectDataJobConfigDTO(self):
        """Test DirectDataJobConfigDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
