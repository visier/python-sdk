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

from visier_api_data_in.api.pgp_key_api import PGPKeyApi


class TestPGPKeyApi(unittest.TestCase):
    """PGPKeyApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PGPKeyApi()

    def tearDown(self) -> None:
        pass

    def test_delete_pgp_key_pair(self) -> None:
        """Test case for delete_pgp_key_pair

        Delete a PGP key pair
        """
        pass

    def test_generate_pgp_key_pair(self) -> None:
        """Test case for generate_pgp_key_pair

        Download a public encryption key
        """
        pass

    def test_get_all_pgp_public_keys(self) -> None:
        """Test case for get_all_pgp_public_keys

        Retrieve all PGP public keys
        """
        pass

    def test_get_pgp_public_key(self) -> None:
        """Test case for get_pgp_public_key

        Retrieve a PGP public key using the key ID
        """
        pass


if __name__ == '__main__':
    unittest.main()
