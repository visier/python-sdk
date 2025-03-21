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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DataservicesQueryTransfersTimeShiftDTO(BaseModel):
    """
    The amount of time to shift the time interval by, such as backward by one year.
    """ # noqa: E501
    direction: Optional[StrictStr] = Field(default=None, description="The direction to extend. Default is BACKWARD.")
    period_count: Optional[StrictInt] = Field(default=None, description="The number of intervals. Default is 1.", alias="periodCount")
    period_type: Optional[StrictStr] = Field(default=None, description="The time period type for the shift.", alias="periodType")
    __properties: ClassVar[List[str]] = ["direction", "periodCount", "periodType"]

    @field_validator('direction')
    def direction_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['BACKWARD', 'FORWARD']):
            raise ValueError("must be one of enum values ('BACKWARD', 'FORWARD')")
        return value

    @field_validator('period_type')
    def period_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MONTH', 'DAY', 'WEEK', 'QUARTER', 'YEAR']):
            raise ValueError("must be one of enum values ('MONTH', 'DAY', 'WEEK', 'QUARTER', 'YEAR')")
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
        """Create an instance of DataservicesQueryTransfersTimeShiftDTO from a JSON string"""
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
        """Create an instance of DataservicesQueryTransfersTimeShiftDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "direction": obj.get("direction"),
            "periodCount": obj.get("periodCount"),
            "periodType": obj.get("periodType")
        })
        return _obj


