# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1598
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
from visier_api_analytic_model.models.plan_item_dto import PlanItemDTO
from visier_api_analytic_model.models.plan_segment_level_dto import PlanSegmentLevelDTO
from visier_api_analytic_model.models.plan_segment_level_member_list_dto import PlanSegmentLevelMemberListDTO
from visier_api_analytic_model.models.plan_time_period_dto import PlanTimePeriodDTO
from typing import Optional, Set
from typing_extensions import Self

class PlanSchemaDTO(BaseModel):
    """
    Information about a plan's schema.
    """ # noqa: E501
    plan_items: Optional[List[PlanItemDTO]] = Field(default=None, description="A collection of editable plan items in a plan.", alias="planItems")
    plan_segment_level_members: Optional[List[PlanSegmentLevelMemberListDTO]] = Field(default=None, description="A collection of members grouped by their dimension and level.  The combination of these member IDs points to a specific row in the plan.", alias="planSegmentLevelMembers")
    plan_segment_levels: Optional[List[PlanSegmentLevelDTO]] = Field(default=None, description="The dimensions that the plan is segmented by.", alias="planSegmentLevels")
    time_periods: Optional[List[PlanTimePeriodDTO]] = Field(default=None, description="The editable time periods in a plan. These time periods are the columns in the planning grid.", alias="timePeriods")
    __properties: ClassVar[List[str]] = ["planItems", "planSegmentLevelMembers", "planSegmentLevels", "timePeriods"]

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
        """Create an instance of PlanSchemaDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in plan_items (list)
        _items = []
        if self.plan_items:
            for _item_plan_items in self.plan_items:
                if _item_plan_items:
                    _items.append(_item_plan_items.to_dict())
            _dict['planItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in plan_segment_level_members (list)
        _items = []
        if self.plan_segment_level_members:
            for _item_plan_segment_level_members in self.plan_segment_level_members:
                if _item_plan_segment_level_members:
                    _items.append(_item_plan_segment_level_members.to_dict())
            _dict['planSegmentLevelMembers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in plan_segment_levels (list)
        _items = []
        if self.plan_segment_levels:
            for _item_plan_segment_levels in self.plan_segment_levels:
                if _item_plan_segment_levels:
                    _items.append(_item_plan_segment_levels.to_dict())
            _dict['planSegmentLevels'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in time_periods (list)
        _items = []
        if self.time_periods:
            for _item_time_periods in self.time_periods:
                if _item_time_periods:
                    _items.append(_item_time_periods.to_dict())
            _dict['timePeriods'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PlanSchemaDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "planItems": [PlanItemDTO.from_dict(_item) for _item in obj["planItems"]] if obj.get("planItems") is not None else None,
            "planSegmentLevelMembers": [PlanSegmentLevelMemberListDTO.from_dict(_item) for _item in obj["planSegmentLevelMembers"]] if obj.get("planSegmentLevelMembers") is not None else None,
            "planSegmentLevels": [PlanSegmentLevelDTO.from_dict(_item) for _item in obj["planSegmentLevels"]] if obj.get("planSegmentLevels") is not None else None,
            "timePeriods": [PlanTimePeriodDTO.from_dict(_item) for _item in obj["timePeriods"]] if obj.get("timePeriods") is not None else None
        })
        return _obj


