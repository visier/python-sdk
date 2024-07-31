# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_out.models.vee_sample_question_library_dto import VeeSampleQuestionLibraryDTO

class TestVeeSampleQuestionLibraryDTO(unittest.TestCase):
    """VeeSampleQuestionLibraryDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VeeSampleQuestionLibraryDTO:
        """Test VeeSampleQuestionLibraryDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VeeSampleQuestionLibraryDTO`
        """
        model = VeeSampleQuestionLibraryDTO()
        if include_optional:
            return VeeSampleQuestionLibraryDTO(
                questions = [
                    visier.sdk.api.data_out.models.vee_sample_question_dto.VeeSampleQuestionDTO(
                        metadata = visier.sdk.api.data_out.models.vee_sample_question_metadata_dto.VeeSampleQuestionMetadataDTO(
                            categories = [
                                ''
                                ], ), 
                        question = '', )
                    ]
            )
        else:
            return VeeSampleQuestionLibraryDTO(
        )
        """

    def testVeeSampleQuestionLibraryDTO(self):
        """Test VeeSampleQuestionLibraryDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
