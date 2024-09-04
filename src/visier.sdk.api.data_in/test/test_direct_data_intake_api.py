# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.data_in.api.direct_data_intake_api import DirectDataIntakeApi


class TestDirectDataIntakeApi(unittest.TestCase):
    """DirectDataIntakeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DirectDataIntakeApi()

    def tearDown(self) -> None:
        pass

    def test_direct_data_intake_commit_transaction(self) -> None:
        """Test case for direct_data_intake_commit_transaction

        Commit a transaction
        """
        pass

    def test_direct_data_intake_get_config(self) -> None:
        """Test case for direct_data_intake_get_config

        Get the direct data intake configuration
        """
        pass

    def test_direct_data_intake_job_status(self) -> None:
        """Test case for direct_data_intake_job_status

        Check transaction status
        """
        pass

    def test_direct_data_intake_object_schema(self) -> None:
        """Test case for direct_data_intake_object_schema

        Retrieve an object's data load schema
        """
        pass

    def test_direct_data_intake_put_config(self) -> None:
        """Test case for direct_data_intake_put_config

        Update the direct data intake configuration
        """
        pass

    def test_direct_data_intake_rollback_transaction(self) -> None:
        """Test case for direct_data_intake_rollback_transaction

        Roll back a transaction
        """
        pass

    def test_direct_data_intake_start_transaction(self) -> None:
        """Test case for direct_data_intake_start_transaction

        Start a direct data intake transaction
        """
        pass

    def test_direct_data_intake_upload_file(self) -> None:
        """Test case for direct_data_intake_upload_file

        Upload files
        """
        pass


if __name__ == '__main__':
    unittest.main()
