# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier.sdk.api.permission_management.models.dimension_filter_dto import DimensionFilterDTO
from typing import Optional, Set
from typing_extensions import Self

class MemberFilterConfigDTO(BaseModel):
    """
    MemberFilterConfigDTO
    """ # noqa: E501
    dimension_filters: Optional[List[DimensionFilterDTO]] = Field(default=None, description="A list of objects representing the custom filters that define population access for the item.   A custom filter can be a \"member filter\" (`staticDimensionFilter`) or a \"dynamic filter\" (`dynamicDimensionFilter`).", alias="dimensionFilters")
    __properties: ClassVar[List[str]] = ["dimensionFilters"]

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
        """Create an instance of MemberFilterConfigDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in dimension_filters (list)
        _items = []
        if self.dimension_filters:
            for _item in self.dimension_filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dimensionFilters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MemberFilterConfigDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dimensionFilters": [DimensionFilterDTO.from_dict(_item) for _item in obj["dimensionFilters"]] if obj.get("dimensionFilters") is not None else None
        })
        return _obj


