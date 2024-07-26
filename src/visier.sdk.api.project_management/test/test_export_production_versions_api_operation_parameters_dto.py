# coding: utf-8

"""
    Visier Project Management APIs

    Visier APIs for managing and publishing projects

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.project_management.models.export_production_versions_api_operation_parameters_dto import ExportProductionVersionsAPIOperationParametersDTO

class TestExportProductionVersionsAPIOperationParametersDTO(unittest.TestCase):
    """ExportProductionVersionsAPIOperationParametersDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExportProductionVersionsAPIOperationParametersDTO:
        """Test ExportProductionVersionsAPIOperationParametersDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExportProductionVersionsAPIOperationParametersDTO`
        """
        model = ExportProductionVersionsAPIOperationParametersDTO()
        if include_optional:
            return ExportProductionVersionsAPIOperationParametersDTO(
                end_version = '',
                excluded_versions = [
                    ''
                    ],
                start_version = ''
            )
        else:
            return ExportProductionVersionsAPIOperationParametersDTO(
        )
        """

    def testExportProductionVersionsAPIOperationParametersDTO(self):
        """Test ExportProductionVersionsAPIOperationParametersDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
