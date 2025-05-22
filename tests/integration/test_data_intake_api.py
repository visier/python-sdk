import unittest
from typing import Type, TypeVar

from test_utils import create_api, TENANT_CODE
from visier_platform_sdk import DataIntakeApi, StartTransferResponse, PushDataResponse, \
    PushDataCompleteRequest, PushDataCompleteResponse

from visier_platform_sdk.rest import RESTResponseType

T = TypeVar('T')


class TestDataIntakeApi(unittest.TestCase):
    """DataIntakeApi unit test stubs"""

    def setUp(self) -> None:
        self.api: DataIntakeApi = create_api(DataIntakeApi)

    def tearDown(self) -> None:
        pass

    def get_dto_from_response(self, response: RESTResponseType, dto_class: Type[T]) -> T:
        """
        Deserialize response data into the specified DTO class.
        This method should be used until incorrect content-type headers are fixed in the API.

        :param response: The response from {method}_without_preload_content.
        :param dto_class: The DTO class to deserialize into.
        :return: An instance of the DTO class.
        """
        self.assertIsNotNone(response)
        self.assertEqual(response.status, 200)
        data = response.data.decode()
        dto = dto_class.from_json(data)
        self.assertIsNotNone(dto)
        return dto

    def test_upload_data(self) -> None:
        """Test case for upload_data

        Transfer data to sources via file upload
        """

        sources_dto = self.api.get_sources()
        self.assertIsNotNone(sources_dto)
        self.assertGreater(len(sources_dto.sources), 1)

        transfer_rest_response = self.api.start_transfer_without_preload_content()
        transfer_response_dto = self.get_dto_from_response(transfer_rest_response, StartTransferResponse)
        try:
            upload_rest_response = self.api.upload_data_without_preload_content(
                transfer_session_id=transfer_response_dto.transfer_session_id,
                source_id=sources_dto.sources[0].source_id,
                tenant_code=TENANT_CODE,
                file="data/applicant.csv")
            push_data_response_dto = self.get_dto_from_response(upload_rest_response, PushDataResponse)
            self.assertEqual('SUCCEED', push_data_response_dto.status)

            push_data_completed = PushDataCompleteRequest(
                transfer_session_id=transfer_response_dto.transfer_session_id,
            )
            push_complete_rest_response = self.api.push_data_complete_without_preload_content(push_data_completed)
            push_complete_response = self.get_dto_from_response(push_complete_rest_response,
                                                                PushDataCompleteResponse)
            self.assertIsNotNone(push_complete_response)

        except Exception as e:
            self.api.push_data_cancel_without_preload_content(transfer_response_dto.transfer_session_id)
            raise e


if __name__ == '__main__':
    unittest.main()
