# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1614
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_analytic_model.api.data_model_api import DataModelApi


class TestDataModelApi(unittest.TestCase):
    """DataModelApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataModelApi()

    def tearDown(self) -> None:
        pass

    def test_analytic_metrics(self) -> None:
        """Test case for analytic_metrics

        Retrieve a list of metrics for an analytic object by ID
        """
        pass

    def test_analytic_object(self) -> None:
        """Test case for analytic_object

        Retrieve an analytic object by ID
        """
        pass

    def test_analytic_objects(self) -> None:
        """Test case for analytic_objects

        Retrieve a list of analytic objects
        """
        pass

    def test_call_property(self) -> None:
        """Test case for call_property

        Retrieve a property by ID
        """
        pass

    def test_currencies(self) -> None:
        """Test case for currencies

        Retrieve all currencies
        """
        pass

    def test_currency(self) -> None:
        """Test case for currency

        Retrieve a currency
        """
        pass

    def test_currency_rates(self) -> None:
        """Test case for currency_rates

        Retrieve all exchange rates for a currency
        """
        pass

    def test_currency_rates_with_to_currency(self) -> None:
        """Test case for currency_rates_with_to_currency

        Retrieve exchange rates from one currency to another currency
        """
        pass

    def test_dimension(self) -> None:
        """Test case for dimension

        Retrieve a dimension by ID
        """
        pass

    def test_dimension_member_map_validation(self) -> None:
        """Test case for dimension_member_map_validation

        Validate a member map's unmapped dimension members by ID
        """
        pass

    def test_dimensions(self) -> None:
        """Test case for dimensions

        Retrieve a list of dimensions
        """
        pass

    def test_member(self) -> None:
        """Test case for member

        Retrieve a dimension member
        """
        pass

    def test_members(self) -> None:
        """Test case for members

        Retrieve a list of dimension members
        """
        pass

    def test_metric(self) -> None:
        """Test case for metric

        Retrieve a metric by ID
        """
        pass

    def test_metric_dimensions(self) -> None:
        """Test case for metric_dimensions

        Retrieve a metric's dimensions
        """
        pass

    def test_metric_selection_concepts(self) -> None:
        """Test case for metric_selection_concepts

        Retrieve a metric's selection concepts
        """
        pass

    def test_metrics(self) -> None:
        """Test case for metrics

        Retrieve a list of metrics
        """
        pass

    def test_plan_data_loadl_list(self) -> None:
        """Test case for plan_data_loadl_list

        Retrieve a list of plans
        """
        pass

    def test_plan_info_with_schema(self) -> None:
        """Test case for plan_info_with_schema

        Retrieve a plan's details
        """
        pass

    def test_planning_metrics(self) -> None:
        """Test case for planning_metrics

        Retrieve metrics by planning model ID
        """
        pass

    def test_planning_model(self) -> None:
        """Test case for planning_model

        Retrieve a planning model by ID
        """
        pass

    def test_planning_models(self) -> None:
        """Test case for planning_models

        Retrieve a list of planning models
        """
        pass

    def test_planning_plan(self) -> None:
        """Test case for planning_plan

        Retrieve a plan by planning model ID and plan ID
        """
        pass

    def test_planning_plans(self) -> None:
        """Test case for planning_plans

        Retrieve a list of plans by planning model ID
        """
        pass

    def test_prediction(self) -> None:
        """Test case for prediction

        Retrieve a prediction by ID
        """
        pass

    def test_predictions(self) -> None:
        """Test case for predictions

        Retrieve a list of predictions
        """
        pass

    def test_properties(self) -> None:
        """Test case for properties

        Retrieve a list of properties
        """
        pass

    def test_selection_concept(self) -> None:
        """Test case for selection_concept

        Retrieve an analytic object's selection concept by ID
        """
        pass

    def test_selection_concepts(self) -> None:
        """Test case for selection_concepts

        Retrieve an analytic object's selection concepts
        """
        pass

    def test_update_dimensions(self) -> None:
        """Test case for update_dimensions

        Update dimensions
        """
        pass

    def test_update_properties(self) -> None:
        """Test case for update_properties

        Update properties
        """
        pass


if __name__ == '__main__':
    unittest.main()
