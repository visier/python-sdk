# coding: utf-8

"""
    Visier Object Configuration APIs

    Visier APIs for managing objects in studio experience

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.object_configuration.api.object_configuration_api import ObjectConfigurationApi


class TestObjectConfigurationApi(unittest.TestCase):
    """ObjectConfigurationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectConfigurationApi()

    def tearDown(self) -> None:
        pass

    def test_get_calculation_concept(self) -> None:
        """Test case for get_calculation_concept

        Retrieve the configuration of a calculation concept
        """
        pass

    def test_get_calculation_concepts(self) -> None:
        """Test case for get_calculation_concepts

        Retrieve all calculation concepts
        """
        pass

    def test_get_selection_concept(self) -> None:
        """Test case for get_selection_concept

        Retrieve the configuration of a selection concept
        """
        pass

    def test_get_selection_concepts(self) -> None:
        """Test case for get_selection_concepts

        Retrieve all selection concepts
        """
        pass

    def test_map_calculation_concept(self) -> None:
        """Test case for map_calculation_concept

        Map dimension members to nodes in a calculation concept
        """
        pass

    def test_map_selection_concept(self) -> None:
        """Test case for map_selection_concept

        Map dimension members to a selection concept
        """
        pass


if __name__ == '__main__':
    unittest.main()
