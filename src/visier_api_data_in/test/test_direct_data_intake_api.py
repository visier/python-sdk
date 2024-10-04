# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1508
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_data_in.api.direct_data_intake_api import DirectDataIntakeApi


class TestDirectDataIntakeApi(unittest.TestCase):
    """DirectDataIntakeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DirectDataIntakeApi()

    def tearDown(self) -> None:
        pass

    def test_commit_transaction(self) -> None:
        """Test case for commit_transaction

        Commit a transaction
        """
        pass

    def test_get_config(self) -> None:
        """Test case for get_config

        Get the direct data intake configuration
        """
        pass

    def test_job_status(self) -> None:
        """Test case for job_status

        Check transaction status
        """
        pass

    def test_object_schema(self) -> None:
        """Test case for object_schema

        Retrieve an object's data load schema
        """
        pass

    def test_put_config(self) -> None:
        """Test case for put_config

        Update the direct data intake configuration
        """
        pass

    def test_rollback_transaction(self) -> None:
        """Test case for rollback_transaction

        Roll back a transaction
        """
        pass

    def test_start_transaction(self) -> None:
        """Test case for start_transaction

        Start a direct data intake transaction
        """
        pass

    def test_upload_file(self) -> None:
        """Test case for upload_file

        Upload files
        """
        pass


if __name__ == '__main__':
    unittest.main()
