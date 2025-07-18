# coding: utf-8

"""
    API Reference

    Detailed API reference documentation for Visier APIs. Includes all endpoints, headers, path parameters, query parameters, request body schema, response schema, JSON request samples, and JSON response samples.

    The version of the OpenAPI document: 22222222.99201.2050
    Contact: alpine@visier.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class InternalQueryExecutionOptionsDTO(BaseModel):
    """
    Internal options - not to be documented or used by external parties
    """ # noqa: E501
    sparse_handling_mode: Optional[StrictStr] = Field(default=None, alias="sparseHandlingMode")
    align_time_axis_to_period_end: Optional[StrictBool] = Field(default=None, description="If true, shifts the time axis members back by one millisecond.  Shifting the time axis members back by one millisecond makes them valid at the end of the period instead of at the start of the next period.  This aligns the returned data timestamps with the timestamps in the Visier application.   Example: If the timestamps are originally [`2019-06-01T00:00:00.000Z`, `2019-05-01T00:00:00.000Z`],  then `alignTimeAxisPeriodEnd` turns the timestamps into [`2019-05-31T23:59:59.999Z`, `2019-04-30T23:59:59.999Z`].   Example: If the timestamps are originally [`2019-05-01T00:00:00.000Z/2019-06-01T00:00:00.000Z`, `2019-04-01T00:00:00.000Z/2019-05-01T00:00:00.000Z`],  then `alignTimeAxisPeriodEnd` turns the timestamps into [`2019-05-01T00:00:00.000Z/2019-05-31T23:59:59.999Z`, `2019-04-01T00:00:00.000Z/2019-04-30T23:59:59.999Z`].", alias="alignTimeAxisToPeriodEnd")
    __properties: ClassVar[List[str]] = ["sparseHandlingMode", "alignTimeAxisToPeriodEnd"]

    @field_validator('sparse_handling_mode')
    def sparse_handling_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ALLOW', 'DISALLOW', 'FORCE']):
            raise ValueError("must be one of enum values ('ALLOW', 'DISALLOW', 'FORCE')")
        return value

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
        """Create an instance of InternalQueryExecutionOptionsDTO from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InternalQueryExecutionOptionsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sparseHandlingMode": obj.get("sparseHandlingMode"),
            "alignTimeAxisToPeriodEnd": obj.get("alignTimeAxisToPeriodEnd")
        })
        return _obj


