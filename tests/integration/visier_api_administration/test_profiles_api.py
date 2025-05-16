import unittest

from test_utils import create_api
from visier_platform_sdk import ProfilesApi


class TestProfilesApi(unittest.TestCase):
    """ProfilesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = create_api(ProfilesApi)

    def tearDown(self) -> None:
        pass

    def test_get_all_profiles(self) -> None:
        """Test case for get_all_profiles

        Retrieve a list of all profiles
        """

        profiles_response_dto = self.api.get_all_profiles()

        self.assertIsNotNone(profiles_response_dto)
        self.assertGreater(len(profiles_response_dto.profiles), 0)


if __name__ == '__main__':
    unittest.main()
