# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1772
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_in.models
from visier_api_data_in.models.success_factors_auth_params_dto import SuccessFactorsAuthParamsDTO

class TestSuccessFactorsAuthParamsDTO(unittest.TestCase):
    """SuccessFactorsAuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SuccessFactorsAuthParamsDTO:
        """Test SuccessFactorsAuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return SuccessFactorsAuthParamsDTO(
                company_id = '',
                host_domain_name = '',
                o_auth = visier_api_data_in.models.success_factors_o_auth_params_dto.SuccessFactorsOAuthParamsDTO(
                    api_key = '', 
                    private_x509_key = '', 
                    public_x509_cert = '', ),
                password = '',
                username = ''
            )
        else:
            return SuccessFactorsAuthParamsDTO(
        )

    def testSuccessFactorsAuthParamsDTO(self):
        """Test SuccessFactorsAuthParamsDTO"""
        def validate_instance(instance):
            SuccessFactorsAuthParamsDTO.model_validate(inst_req_only)
            instance_deserialized = SuccessFactorsAuthParamsDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
