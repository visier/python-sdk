# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1547
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_data_in.api.data_and_job_handling_api import DataAndJobHandlingApi


class TestDataAndJobHandlingApi(unittest.TestCase):
    """DataAndJobHandlingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataAndJobHandlingApi()

    def tearDown(self) -> None:
        pass

    def test_adhoc_consolidated_analytics_job(self) -> None:
        """Test case for adhoc_consolidated_analytics_job

        Run a consolidated analytics job
        """
        pass

    def test_adhoc_extraction_job(self) -> None:
        """Test case for adhoc_extraction_job

        Run a data connector extraction job
        """
        pass

    def test_adhoc_processing_jobs(self) -> None:
        """Test case for adhoc_processing_jobs

        Run a processing job
        """
        pass

    def test_assign_connector_credential(self) -> None:
        """Test case for assign_connector_credential

        Assign connector credentials to data connectors
        """
        pass

    def test_cancel_jobs(self) -> None:
        """Test case for cancel_jobs

        Cancel a list of jobs
        """
        pass

    def test_create_connector_credential(self) -> None:
        """Test case for create_connector_credential

        Create a connector credential
        """
        pass

    def test_data_connector_credentials(self) -> None:
        """Test case for data_connector_credentials

        Retrieve a list of all data connector credentials
        """
        pass

    def test_data_connectors(self) -> None:
        """Test case for data_connectors

        Retrieve a list of all data connectors
        """
        pass

    def test_delete_connector_credential(self) -> None:
        """Test case for delete_connector_credential

        Delete a connector credential
        """
        pass

    def test_disable_dv(self) -> None:
        """Test case for disable_dv

        Disable data versions for a list of analytic tenants
        """
        pass

    def test_dispatching_job_status(self) -> None:
        """Test case for dispatching_job_status

        Retrieve a dispatching job's status
        """
        pass

    def test_exclude_data_uplaods(self) -> None:
        """Test case for exclude_data_uplaods

        Exclude data uploads
        """
        pass

    def test_extraction_job_and_status(self) -> None:
        """Test case for extraction_job_and_status

        Retrieve a dispatching job's extraction jobs with their statuses
        """
        pass

    def test_include_data_uploads(self) -> None:
        """Test case for include_data_uploads

        Include data uploads
        """
        pass

    def test_job_id_status(self) -> None:
        """Test case for job_id_status

        Retrieve a specific job's status
        """
        pass

    def test_job_status_0(self) -> None:
        """Test case for job_status_0

        Retrieve the statuses of all jobs
        """
        pass

    def test_latest_enabled_dv(self) -> None:
        """Test case for latest_enabled_dv

        Retrieve the latest enabled data versions for all analytic tenants
        """
        pass

    def test_list_connector_settings(self) -> None:
        """Test case for list_connector_settings

        Retrieve data connector settings
        """
        pass

    def test_processing_job_and_status(self) -> None:
        """Test case for processing_job_and_status

        Retrieve a dispatching job's processing jobs with their statuses
        """
        pass

    def test_processing_job_status(self) -> None:
        """Test case for processing_job_status

        Retrieve processing job statuses by receiving job ID
        """
        pass

    def test_receiving_job_and_status(self) -> None:
        """Test case for receiving_job_and_status

        Retrieve a dispatching job's receiving jobs with their statuses
        """
        pass

    def test_receiving_job_status(self) -> None:
        """Test case for receiving_job_status

        Retrieve a receiving job's status
        """
        pass

    def test_retrieve_data_categories(self) -> None:
        """Test case for retrieve_data_categories

        Retrieve a list of all data categories
        """
        pass

    def test_retrieve_data_uploads(self) -> None:
        """Test case for retrieve_data_uploads

        Retrieve data uploads
        """
        pass

    def test_set_connector_setting(self) -> None:
        """Test case for set_connector_setting

        Update data connector settings
        """
        pass

    def test_start_extraction(self) -> None:
        """Test case for start_extraction

        Trigger data connector extraction jobs
        """
        pass

    def test_start_load(self) -> None:
        """Test case for start_load

        Start the data load for analytic tenants
        """
        pass


if __name__ == '__main__':
    unittest.main()
