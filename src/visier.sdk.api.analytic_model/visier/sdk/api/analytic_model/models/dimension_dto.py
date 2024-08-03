# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1430
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier.sdk.api.analytic_model.models.level_dto import LevelDTO
from visier.sdk.api.analytic_model.models.tag_map_element_dto import TagMapElementDTO
from typing import Optional, Set
from typing_extensions import Self

class DimensionDTO(BaseModel):
    """
    A dimension organizes unique values of an attribute into a list or a hierarchical structure for use as a filter or group-by in your solution.
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="The localized description of the dimension.")
    display_name: Optional[StrictStr] = Field(default=None, description="The localized display name of the dimension.", alias="displayName")
    id: Optional[StrictStr] = Field(default=None, description="The unique ID of the dimension.  Note: See `Dimensions` to get the ID`.")
    levels: Optional[List[LevelDTO]] = Field(default=None, description="The levels defined for the dimension. Note: For parent-child dimensions, a level name is generated by Visier.")
    member_count: Optional[StrictInt] = Field(default=None, description="The total number of members for the dimension, excluding the (All) member.", alias="memberCount")
    tags: Optional[List[TagMapElementDTO]] = Field(default=None, description="The optional collection of tags defined for this element.")
    unknown_member: Optional[List[StrictStr]] = Field(default=None, description="The optional path to the unknown member, if defined.", alias="unknownMember")
    visible_in_app: Optional[StrictBool] = Field(default=None, description="`true` if this dimension is set to be visible in your solution.", alias="visibleInApp")
    __properties: ClassVar[List[str]] = ["description", "displayName", "id", "levels", "memberCount", "tags", "unknownMember", "visibleInApp"]

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
        """Create an instance of DimensionDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in levels (list)
        _items = []
        if self.levels:
            for _item in self.levels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['levels'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DimensionDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "displayName": obj.get("displayName"),
            "id": obj.get("id"),
            "levels": [LevelDTO.from_dict(_item) for _item in obj["levels"]] if obj.get("levels") is not None else None,
            "memberCount": obj.get("memberCount"),
            "tags": [TagMapElementDTO.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "unknownMember": obj.get("unknownMember"),
            "visibleInApp": obj.get("visibleInApp")
        })
        return _obj


