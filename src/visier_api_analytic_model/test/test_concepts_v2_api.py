# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1905
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.api.concepts_v2_api import ConceptsV2Api


class TestConceptsV2Api(unittest.TestCase):
    """ConceptsV2Api unit test stubs"""

    def setUp(self) -> None:
        self.api = ConceptsV2Api()

    def tearDown(self) -> None:
        pass

    def test_create_concepts(self) -> None:
        """Test case for create_concepts

        Create concepts
        """
        pass

    def test_delete_concepts(self) -> None:
        """Test case for delete_concepts

        Delete concepts
        """
        pass

    def test_get_all_concepts(self) -> None:
        """Test case for get_all_concepts

        Retrieve a list of concepts
        """
        pass

    def test_get_analytic_object_concepts(self) -> None:
        """Test case for get_analytic_object_concepts

        Retrieve a list of concepts by analytic object
        """
        pass

    def test_get_one_concept(self) -> None:
        """Test case for get_one_concept

        Retrieve a concept's details
        """
        pass

    def test_patch_concepts(self) -> None:
        """Test case for patch_concepts

        Partially update concepts
        """
        pass

    def test_put_concepts(self) -> None:
        """Test case for put_concepts

        Update concepts
        """
        pass


if __name__ == '__main__':
    unittest.main()
