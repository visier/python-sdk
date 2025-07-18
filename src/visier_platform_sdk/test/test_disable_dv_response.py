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
from visier_platform_sdk.models.disable_dv_response import DisableDVResponse

class TestDisableDVResponse(unittest.TestCase):
    """DisableDVResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DisableDVResponse:
        """Test DisableDVResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DisableDVResponse(
                total_failures = 56,
                total_success = 56,
                results = [
                    visier_platform_sdk.models.result.Result(
                        job_id = '', 
                        data_version = '', 
                        tenant_code = '', 
                        status = '', 
                        message = '', )
                    ]
            )
        else:
            return DisableDVResponse(
        )

    def testDisableDVResponse(self):
        """Test DisableDVResponse"""
        def validate_instance(instance):
            DisableDVResponse.model_validate(inst_req_only)
            instance_deserialized = DisableDVResponse.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
