# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_data_out.models.dataservices_query_transfers_aggregation_query_source_dto import DataservicesQueryTransfersAggregationQuerySourceDTO
from visier_api_data_out.models.dataservices_query_transfers_query_axis_dto import DataservicesQueryTransfersQueryAxisDTO
from visier_api_data_out.models.dataservices_query_transfers_query_filter_dto import DataservicesQueryTransfersQueryFilterDTO
from visier_api_data_out.models.dataservices_query_transfers_query_parameter_value_dto import DataservicesQueryTransfersQueryParameterValueDTO
from visier_api_data_out.models.dataservices_query_transfers_query_time_intervals_dto import DataservicesQueryTransfersQueryTimeIntervalsDTO
from typing import Optional, Set
from typing_extensions import Self

class DataservicesQueryTransfersAggregationQueryDTO(BaseModel):
    """
    An AggregationQuery defines the data to query in an aggregation query and returns a `cell set` calculated from  the selected data points.
    """ # noqa: E501
    axes: Optional[List[DataservicesQueryTransfersQueryAxisDTO]] = Field(default=None, description="The objects by which to group the query. An axis defines the groups that the data belongs to.  Omit `axes` if no grouping is required.")
    filters: Optional[List[DataservicesQueryTransfersQueryFilterDTO]] = Field(default=None, description="The objects by which to filter the query, such as dimensions or concepts.  A filter defines the population to retrieve data from. Omit `filters` if no filtering is required.")
    parameter_values: Optional[List[DataservicesQueryTransfersQueryParameterValueDTO]] = Field(default=None, description="The values associated with parameters, if defined.", alias="parameterValues")
    source: Optional[DataservicesQueryTransfersAggregationQuerySourceDTO] = Field(default=None, description="The source data, such as a metric or formula, to query.")
    time_intervals: Optional[DataservicesQueryTransfersQueryTimeIntervalsDTO] = Field(default=None, description="The time intervals to query.", alias="timeIntervals")
    __properties: ClassVar[List[str]] = ["axes", "filters", "parameterValues", "source", "timeIntervals"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DataservicesQueryTransfersAggregationQueryDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in axes (list)
        _items = []
        if self.axes:
            for _item_axes in self.axes:
                if _item_axes:
                    _items.append(_item_axes.to_dict())
            _dict['axes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item_filters in self.filters:
                if _item_filters:
                    _items.append(_item_filters.to_dict())
            _dict['filters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in parameter_values (list)
        _items = []
        if self.parameter_values:
            for _item_parameter_values in self.parameter_values:
                if _item_parameter_values:
                    _items.append(_item_parameter_values.to_dict())
            _dict['parameterValues'] = _items
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_intervals
        if self.time_intervals:
            _dict['timeIntervals'] = self.time_intervals.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataservicesQueryTransfersAggregationQueryDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "axes": [DataservicesQueryTransfersQueryAxisDTO.from_dict(_item) for _item in obj["axes"]] if obj.get("axes") is not None else None,
            "filters": [DataservicesQueryTransfersQueryFilterDTO.from_dict(_item) for _item in obj["filters"]] if obj.get("filters") is not None else None,
            "parameterValues": [DataservicesQueryTransfersQueryParameterValueDTO.from_dict(_item) for _item in obj["parameterValues"]] if obj.get("parameterValues") is not None else None,
            "source": DataservicesQueryTransfersAggregationQuerySourceDTO.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "timeIntervals": DataservicesQueryTransfersQueryTimeIntervalsDTO.from_dict(obj["timeIntervals"]) if obj.get("timeIntervals") is not None else None
        })
        return _obj


