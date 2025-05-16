import unittest

from test_utils import create_api
from visier_platform_sdk import ProductionVersionsApi, ServicingProductionVersionAPIOperationRequestDTO


class TestProductionVersionsApi(unittest.TestCase):
    """ProductionVersionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api: ProductionVersionsApi = create_api(ProductionVersionsApi)

    def tearDown(self) -> None:
        pass

    def test_post_production_versions(self) -> None:
        """Test case for post_production_versions

        Perform an operation on production versions

        User should have internal debugging capabilities
        """

        versions_response_dto = self.api.get_production_versions()
        self.assertIsNotNone(versions_response_dto)
        self.assertIsNotNone(versions_response_dto.published_versions)
        self.assertGreater(len(versions_response_dto.published_versions), 1)

        operation_request_dto = ServicingProductionVersionAPIOperationRequestDTO(
            operation='rollBackTo'
        )
        operation_response_dto = self.api.post_production_version(versions_response_dto.published_versions[1].id,
                                                                  operation_request_dto)
        self.assertIsNotNone(operation_response_dto)
        self.assertIsNotNone(operation_response_dto.roll_back_to)


if __name__ == '__main__':
    unittest.main()
