# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1474
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_data_out.models.key_group_filter_item_dto import KeyGroupFilterItemDTO

class TestKeyGroupFilterItemDTO(unittest.TestCase):
    """KeyGroupFilterItemDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KeyGroupFilterItemDTO:
        """Test KeyGroupFilterItemDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KeyGroupFilterItemDTO`
        """
        model = KeyGroupFilterItemDTO()
        if include_optional:
            return KeyGroupFilterItemDTO(
                formula = '',
                member_set = visier_api_data_out.models.member_filter_dto.MemberFilterDTO(
                    dimension = null, 
                    values = null, ),
                selection_concept = visier_api_data_out.models.selection_concept_reference_dto.SelectionConceptReferenceDTO(
                    name = '', 
                    qualifying_path = '', )
            )
        else:
            return KeyGroupFilterItemDTO(
        )
        """

    def testKeyGroupFilterItemDTO(self):
        """Test KeyGroupFilterItemDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
