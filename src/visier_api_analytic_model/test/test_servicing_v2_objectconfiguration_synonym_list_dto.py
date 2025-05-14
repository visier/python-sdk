# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1905
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_analytic_model.models
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_synonym_list_dto import ServicingV2ObjectconfigurationSynonymListDTO

class TestServicingV2ObjectconfigurationSynonymListDTO(unittest.TestCase):
    """ServicingV2ObjectconfigurationSynonymListDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicingV2ObjectconfigurationSynonymListDTO:
        """Test ServicingV2ObjectconfigurationSynonymListDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return ServicingV2ObjectconfigurationSynonymListDTO(
                synonyms = [
                    ''
                    ]
            )
        else:
            return ServicingV2ObjectconfigurationSynonymListDTO(
        )

    def testServicingV2ObjectconfigurationSynonymListDTO(self):
        """Test ServicingV2ObjectconfigurationSynonymListDTO"""
        def validate_instance(instance):
            ServicingV2ObjectconfigurationSynonymListDTO.model_validate(inst_req_only)
            instance_deserialized = ServicingV2ObjectconfigurationSynonymListDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
