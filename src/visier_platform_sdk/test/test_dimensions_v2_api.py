# coding: utf-8

"""
    API Reference

    Detailed API reference documentation for Visier APIs. Includes all endpoints, headers, path parameters, query parameters, request body schema, response schema, JSON request samples, and JSON response samples.

    The version of the OpenAPI document: 22222222.99201.2050
    Contact: alpine@visier.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier_platform_sdk.api.dimensions_v2_api import DimensionsV2Api


class TestDimensionsV2Api(unittest.TestCase):
    """DimensionsV2Api unit test stubs"""

    def setUp(self) -> None:
        self.api = DimensionsV2Api()

    def tearDown(self) -> None:
        pass

    def test_create_dimensions(self) -> None:
        """Test case for create_dimensions

        Create dimensions
        """
        pass

    def test_delete_dimensions(self) -> None:
        """Test case for delete_dimensions

        Delete dimensions
        """
        pass

    def test_get_all_dimensions(self) -> None:
        """Test case for get_all_dimensions

        Retrieve a list of dimensions
        """
        pass

    def test_get_analytic_object_dimensions(self) -> None:
        """Test case for get_analytic_object_dimensions

        Retrieve a list of dimensions by analytic object
        """
        pass

    def test_get_one_dimension(self) -> None:
        """Test case for get_one_dimension

        Retrieve a dimension's details
        """
        pass

    def test_patch_dimensions(self) -> None:
        """Test case for patch_dimensions

        Partially update dimensions
        """
        pass

    def test_put_dimensions(self) -> None:
        """Test case for put_dimensions

        Update dimensions
        """
        pass


if __name__ == '__main__':
    unittest.main()
