# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1614
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_administration.api.projects_api import ProjectsApi


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectsApi()

    def tearDown(self) -> None:
        pass

    def test_create_project(self) -> None:
        """Test case for create_project

        Create a new draft project
        """
        pass

    def test_delete_project(self) -> None:
        """Test case for delete_project

        Delete a draft project
        """
        pass

    def test_get_project(self) -> None:
        """Test case for get_project

        Retrieve a draft project's information
        """
        pass

    def test_get_project_commits(self) -> None:
        """Test case for get_project_commits

        Retrieve a list of all committed changes in a project
        """
        pass

    def test_get_projects(self) -> None:
        """Test case for get_projects

        Retrieve a list of draft projects accessible to the user
        """
        pass

    def test_put_project_commits(self) -> None:
        """Test case for put_project_commits

        Import committed changes into a project
        """
        pass

    def test_run_project_operation(self) -> None:
        """Test case for run_project_operation

        Perform an operation on a draft project
        """
        pass


if __name__ == '__main__':
    unittest.main()
