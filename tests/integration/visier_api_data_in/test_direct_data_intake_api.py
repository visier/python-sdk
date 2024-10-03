import unittest

from test_utils import create_api
from visier_api_core import ApiException
from visier_api_data_in.api.direct_data_intake_api import DirectDataIntakeApi

SUCCEEDED = 'SUCCEEDED'


class TestDirectDataIntakeApi(unittest.TestCase):
    """DirectDataIntakeApi unit test stubs"""

    def setUp(self) -> None:
        self.api: DirectDataIntakeApi = create_api(DirectDataIntakeApi)

    def tearDown(self) -> None:
        pass

    def test_upload_file(self) -> None:
        """Test case for upload_file

        Upload files
        """

        draft_id = 'prod'
        transaction_dto = self.api.start_transaction(draft_id=draft_id)
        try:
            upload_response_dto = self.api.upload_file(draft_id=draft_id,
                                                       transaction_id=transaction_dto.transaction_id,
                                                       object_name="Applicant",
                                                       file="data/applicant.csv")
            self.assertIsNotNone(upload_response_dto)
            self.assertEqual(upload_response_dto.status, SUCCEEDED)
            commit_response_dto = self.api.commit_transaction(draft_id=draft_id,
                                                              transaction_id=transaction_dto.transaction_id)
            self.assertIsNotNone(commit_response_dto)
            self.assertEqual(commit_response_dto.status, SUCCEEDED)
        except ApiException as e:
            self.api.rollback_transaction(draft_id=draft_id, transaction_id=transaction_dto.transaction_id)
            raise e


if __name__ == '__main__':
    unittest.main()
