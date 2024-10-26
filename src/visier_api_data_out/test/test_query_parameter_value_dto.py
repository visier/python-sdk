# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1547
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.query_parameter_value_dto import QueryParameterValueDTO

class TestQueryParameterValueDTO(unittest.TestCase):
    """QueryParameterValueDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryParameterValueDTO:
        """Test QueryParameterValueDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return QueryParameterValueDTO(
                aggregation_type_value = visier_api_data_out.models.aggregation_type_parameter_value_dto.AggregationTypeParameterValueDTO(
                    aggregation_option_id = '', 
                    parameter_id = '', ),
                member_value = visier_api_data_out.models.member_parameter_value_dto.MemberParameterValueDTO(
                    dimension_id = '', 
                    parameter_id = '', 
                    reference_path = [
                        ''
                        ], 
                    values = None, ),
                numeric_value = visier_api_data_out.models.numeric_parameter_value_dto.NumericParameterValueDTO(
                    parameter_id = '', 
                    value = 1.337, ),
                plan_value = visier_api_data_out.models.plan_parameter_value_dto.PlanParameterValueDTO(
                    parameter_id = '', 
                    plan_id = '', 
                    scenario_id = '', 
                    snapshot_id = '', )
            )
        else:
            return QueryParameterValueDTO(
        )

    def testQueryParameterValueDTO(self):
        """Test QueryParameterValueDTO"""
        def validate_instance(instance):
            QueryParameterValueDTO.model_validate(inst_req_only)
            instance_deserialized = QueryParameterValueDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
