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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from visier_platform_sdk.models.plan_data_load_error_dto import PlanDataLoadErrorDTO
from visier_platform_sdk.models.plan_segment_level_member_dto import PlanSegmentLevelMemberDTO
from typing import Optional, Set
from typing_extensions import Self

class PlanRowDataLoadResponseDTO(BaseModel):
    """
    PlanRowDataLoadResponseDTO
    """ # noqa: E501
    added_rows_count: Optional[StrictInt] = Field(default=None, description="The number of rows added to the plan.", alias="addedRowsCount")
    removed_rows_count: Optional[StrictInt] = Field(default=None, description="The number of rows removed from the plan.", alias="removedRowsCount")
    potential_added_rows_count: Optional[StrictInt] = Field(default=None, description="The number of rows that could have been added to the plan.", alias="potentialAddedRowsCount")
    potential_removed_rows_count: Optional[StrictInt] = Field(default=None, description="The number of rows that could have been removed from the plan.", alias="potentialRemovedRowsCount")
    errors: Optional[List[PlanDataLoadErrorDTO]] = Field(default=None, description="The errors that occurred while loading the data.")
    custom_members: Optional[List[PlanSegmentLevelMemberDTO]] = Field(default=None, description="The custom members and their corresponding IDs in the plan.", alias="customMembers")
    __properties: ClassVar[List[str]] = ["addedRowsCount", "removedRowsCount", "potentialAddedRowsCount", "potentialRemovedRowsCount", "errors", "customMembers"]

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
        """Create an instance of PlanRowDataLoadResponseDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item_errors in self.errors:
                if _item_errors:
                    _items.append(_item_errors.to_dict())
            _dict['errors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_members (list)
        _items = []
        if self.custom_members:
            for _item_custom_members in self.custom_members:
                if _item_custom_members:
                    _items.append(_item_custom_members.to_dict())
            _dict['customMembers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PlanRowDataLoadResponseDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addedRowsCount": obj.get("addedRowsCount"),
            "removedRowsCount": obj.get("removedRowsCount"),
            "potentialAddedRowsCount": obj.get("potentialAddedRowsCount"),
            "potentialRemovedRowsCount": obj.get("potentialRemovedRowsCount"),
            "errors": [PlanDataLoadErrorDTO.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "customMembers": [PlanSegmentLevelMemberDTO.from_dict(_item) for _item in obj["customMembers"]] if obj.get("customMembers") is not None else None
        })
        return _obj


