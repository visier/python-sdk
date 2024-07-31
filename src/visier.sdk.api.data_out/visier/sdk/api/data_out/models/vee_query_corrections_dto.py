# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from visier.sdk.api.data_out.models.query_clarification_dto import QueryClarificationDTO
from typing import Optional, Set
from typing_extensions import Self

class VeeQueryCorrectionsDTO(BaseModel):
    """
    VeeQueryCorrectionsDTO
    """ # noqa: E501
    clarifications: Optional[List[QueryClarificationDTO]] = None
    warning: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["clarifications", "warning"]

    @field_validator('warning')
    def warning_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['VEE_NO_WARNING', 'VEE_WARNING_RESPONSE_NOT_FOUND', 'VEE_WARNING_RESPONSE_LOW_CONFIDENCE', 'VEE_WARNING_RESPONSE_FOUND_CLOSE_MATCH', 'VEE_WARNING_NO_ACCESS', 'VEE_WARNING_TIME_SELECTION_ADJUSTED', 'VEE_WARNING_FILTER_DROPPED']):
                raise ValueError("each list item must be one of ('VEE_NO_WARNING', 'VEE_WARNING_RESPONSE_NOT_FOUND', 'VEE_WARNING_RESPONSE_LOW_CONFIDENCE', 'VEE_WARNING_RESPONSE_FOUND_CLOSE_MATCH', 'VEE_WARNING_NO_ACCESS', 'VEE_WARNING_TIME_SELECTION_ADJUSTED', 'VEE_WARNING_FILTER_DROPPED')")
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
        """Create an instance of VeeQueryCorrectionsDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in clarifications (list)
        _items = []
        if self.clarifications:
            for _item in self.clarifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['clarifications'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VeeQueryCorrectionsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clarifications": [QueryClarificationDTO.from_dict(_item) for _item in obj["clarifications"]] if obj.get("clarifications") is not None else None,
            "warning": obj.get("warning")
        })
        return _obj


