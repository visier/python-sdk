# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1905
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_out.models
from visier_api_data_out.models.dataservices_query_query_execution_errors_dto import DataservicesQueryQueryExecutionErrorsDTO

class TestDataservicesQueryQueryExecutionErrorsDTO(unittest.TestCase):
    """DataservicesQueryQueryExecutionErrorsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataservicesQueryQueryExecutionErrorsDTO:
        """Test DataservicesQueryQueryExecutionErrorsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataservicesQueryQueryExecutionErrorsDTO(
                error_code = '',
                message = '',
                all_error_details = [
                    visier_api_data_out.models.dataservices/query/query_execution_error_details_dto.dataservices.query.QueryExecutionErrorDetailsDTO(
                        object_type = '', 
                        query_index = 56, 
                        column_index = 56, 
                        error = '', )
                    ]
            )
        else:
            return DataservicesQueryQueryExecutionErrorsDTO(
        )

    def testDataservicesQueryQueryExecutionErrorsDTO(self):
        """Test DataservicesQueryQueryExecutionErrorsDTO"""
        def validate_instance(instance):
            DataservicesQueryQueryExecutionErrorsDTO.model_validate(inst_req_only)
            instance_deserialized = DataservicesQueryQueryExecutionErrorsDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
