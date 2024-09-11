# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 0.99201.1475
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_api_administration.models.commit_and_publish_operation_response_dto import CommitAndPublishOperationResponseDTO

class TestCommitAndPublishOperationResponseDTO(unittest.TestCase):
    """CommitAndPublishOperationResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommitAndPublishOperationResponseDTO:
        """Test CommitAndPublishOperationResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommitAndPublishOperationResponseDTO`
        """
        model = CommitAndPublishOperationResponseDTO()
        if include_optional:
            return CommitAndPublishOperationResponseDTO(
                published_version = visier_api_administration.models.project_dto.ProjectDTO(
                    capabilities = [
                        'canRead'
                        ], 
                    description = '', 
                    id = '', 
                    name = '', 
                    release_version = '', 
                    ticket_number = '', 
                    version_number = 56, )
            )
        else:
            return CommitAndPublishOperationResponseDTO(
        )
        """

    def testCommitAndPublishOperationResponseDTO(self):
        """Test CommitAndPublishOperationResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
