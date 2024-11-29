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


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_analytic_model.models.validity_range_dto import ValidityRangeDTO
from typing import Optional, Set
from typing_extensions import Self

class MemberDTO(BaseModel):
    """
    A member is an element of a dimension. Dimension members are organized hierarchically. For example, Argentina is  a member of the Location dimension at the Country level of the hierarchy Region > Country > Province > City.
    """ # noqa: E501
    display_name: Optional[StrictStr] = Field(default=None, description="The localized display name of the member.", alias="displayName")
    display_name_path: Optional[List[StrictStr]] = Field(default=None, description="The display names for each level in the member's ancestral path.", alias="displayNamePath")
    full_name: Optional[StrictStr] = Field(default=None, description="The fully qualified name of the member. This is the dimension's object name and the member's display name, separated by a period.", alias="fullName")
    level: Optional[StrictInt] = Field(default=None, description="The numeric level of the hierarchy the member belongs to.")
    path: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated list of identifiers that reference members on the query axis as part of dimensionMemberSelection.")
    validity_ranges: Optional[List[ValidityRangeDTO]] = Field(default=None, description="The validity ranges that exist for this member.", alias="validityRanges")
    __properties: ClassVar[List[str]] = ["displayName", "displayNamePath", "fullName", "level", "path", "validityRanges"]

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
        """Create an instance of MemberDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in validity_ranges (list)
        _items = []
        if self.validity_ranges:
            for _item_validity_ranges in self.validity_ranges:
                if _item_validity_ranges:
                    _items.append(_item_validity_ranges.to_dict())
            _dict['validityRanges'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MemberDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "displayName": obj.get("displayName"),
            "displayNamePath": obj.get("displayNamePath"),
            "fullName": obj.get("fullName"),
            "level": obj.get("level"),
            "path": obj.get("path"),
            "validityRanges": [ValidityRangeDTO.from_dict(_item) for _item in obj["validityRanges"]] if obj.get("validityRanges") is not None else None
        })
        return _obj


