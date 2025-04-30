# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1876
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.dataservices_query_query_parameter_value_dto import DataservicesQueryQueryParameterValueDTO

class TestDataservicesQueryQueryParameterValueDTO(unittest.TestCase):
    """DataservicesQueryQueryParameterValueDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesQueryQueryParameterValueDTO:
        """Test DataservicesQueryQueryParameterValueDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesQueryQueryParameterValueDTO(
                member_value = visier_api_data_out.models.dataservices/query/member_parameter_value_dto.dataservices.query.MemberParameterValueDTO(
                    parameter_id = '', 
                    dimension_id = '', 
                    reference_path = [
                        ''
                        ], 
                    values = None, ),
                numeric_value = visier_api_data_out.models.dataservices/query/numeric_parameter_value_dto.dataservices.query.NumericParameterValueDTO(
                    parameter_id = '', 
                    value = 1.337, ),
                plan_value = visier_api_data_out.models.dataservices/query/plan_parameter_value_dto.dataservices.query.PlanParameterValueDTO(
                    parameter_id = '', 
                    plan_id = '', 
                    scenario_id = '', 
                    snapshot_id = '', ),
                aggregation_type_value = visier_api_data_out.models.dataservices/query/aggregation_type_parameter_value_dto.dataservices.query.AggregationTypeParameterValueDTO(
                    parameter_id = '', 
                    aggregation_option_id = '', )
            )
        else:
            return DataservicesQueryQueryParameterValueDTO(
        )

    def testDataservicesQueryQueryParameterValueDTO(self):
        """Test DataservicesQueryQueryParameterValueDTO"""
        def validate_instance(instance):
            DataservicesQueryQueryParameterValueDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesQueryQueryParameterValueDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
