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
from visier_api_data_out.models.dataservices_query_transfers_key_group_filter_item_dto import DataservicesQueryTransfersKeyGroupFilterItemDTO

class TestDataservicesQueryTransfersKeyGroupFilterItemDTO(unittest.TestCase):
    """DataservicesQueryTransfersKeyGroupFilterItemDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesQueryTransfersKeyGroupFilterItemDTO:
        """Test DataservicesQueryTransfersKeyGroupFilterItemDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesQueryTransfersKeyGroupFilterItemDTO(
                formula = '',
                member_set = visier_api_data_out.models.dataservices/query/transfers/member_filter_dto.dataservices.query.transfers.MemberFilterDTO(
                    dimension = None, 
                    values = None, ),
                selection_concept = visier_api_data_out.models.dataservices/datamodel/transfers/selection_concept_reference_dto.dataservices.datamodel.transfers.SelectionConceptReferenceDTO(
                    name = '', 
                    qualifying_path = '', )
            )
        else:
            return DataservicesQueryTransfersKeyGroupFilterItemDTO(
        )

    def testDataservicesQueryTransfersKeyGroupFilterItemDTO(self):
        """Test DataservicesQueryTransfersKeyGroupFilterItemDTO"""
        def validate_instance(instance):
            DataservicesQueryTransfersKeyGroupFilterItemDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesQueryTransfersKeyGroupFilterItemDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
