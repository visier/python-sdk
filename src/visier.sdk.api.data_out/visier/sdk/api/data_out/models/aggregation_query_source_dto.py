# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier.sdk.api.data_out.models.aggregation_query_source_metrics_dto import AggregationQuerySourceMetricsDTO
from typing import Optional, Set
from typing_extensions import Self

class AggregationQuerySourceDTO(BaseModel):
    """
    An AggregationQuerySource defines the source data to query in an aggregation query.
    """ # noqa: E501
    formula: Optional[StrictStr] = Field(default=None, description="An ad-hoc metric formula. The response returns the results of the aggregate.  See the formula dictionary in Visier to find functions and objects you can use in a formula.")
    metric: Optional[StrictStr] = Field(default=None, description="The ID of an existing metric in your Visier solution. See `Metrics` to get the ID.")
    metrics: Optional[AggregationQuerySourceMetricsDTO] = Field(default=None, description="The IDs of metrics to aggregate. All metrics in the query must reference the same analytic object.  For example, you cannot query Headcount and Applicant Count because one uses the Employee subject and  the other uses the Applicant subject. You can query Headcount and Employee Count for Women because both  reference the Employee subject. Only available when the Accept header is text/csv. For more information,  see `Aggregate`.")
    __properties: ClassVar[List[str]] = ["formula", "metric", "metrics"]

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
        """Create an instance of AggregationQuerySourceDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metrics
        if self.metrics:
            _dict['metrics'] = self.metrics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AggregationQuerySourceDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "formula": obj.get("formula"),
            "metric": obj.get("metric"),
            "metrics": AggregationQuerySourceMetricsDTO.from_dict(obj["metrics"]) if obj.get("metrics") is not None else None
        })
        return _obj


