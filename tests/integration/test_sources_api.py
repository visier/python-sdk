import io
import unittest
import zipfile

from test_utils import create_api
from visier_platform_sdk import SourcesApi, ServicingSourcesAPIOperationRequestDTO, SourcesAPIPutResponseDTO


class TestSourcesApi(unittest.TestCase):
    """SourcesApi unit test stubs"""

    def setUp(self) -> None:
        self.api: SourcesApi = create_api(SourcesApi)

    def tearDown(self) -> None:
        pass

    def test_get_sources(self) -> None:
        operation_request_dto = ServicingSourcesAPIOperationRequestDTO(
            operation='exportSources'
        )

        rest_response = self.api.run_sources_operation_without_preload_content(operation_request_dto,
                                                                               _headers={'Accept': 'application/zip'})
        self.assertEqual(200, rest_response.status)
        zip_data = io.BytesIO(rest_response.data)

        with zipfile.ZipFile(zip_data, 'r') as zip_ref:
            zip_contents = zip_ref.namelist()
            self.assertGreater(len(zip_contents), 0, "Downloaded source zip archive is empty")

    def test_put_sources(self) -> None:
        """Test case for put_sources

        Import a list of sources
        """

        sources_zip_file = 'data/sources.zip'
        with open(sources_zip_file, 'rb') as f:
            data = f.read()

        sources_put_response: SourcesAPIPutResponseDTO = self.api.put_sources(replace_all_existing_sources=False,
                                                                              body=data)
        self.assertIsNotNone(sources_put_response)
        self.assertGreater(sources_put_response.summary.updated, 0)
        pass


if __name__ == '__main__':
    unittest.main()
