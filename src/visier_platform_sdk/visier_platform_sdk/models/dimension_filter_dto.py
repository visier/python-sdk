# coding: utf-8

"""
    API Reference

    Detailed API reference documentation for Visier APIs. Includes all endpoints, headers, path parameters, query parameters, request body schema, response schema, JSON request samples, and JSON response samples.

    The version of the OpenAPI document: 22222222.99200.21550
    Contact: alpine@visier.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_platform_sdk.models.member_selection_list_dto import MemberSelectionListDTO
from visier_platform_sdk.models.qualifying_path_dto import QualifyingPathDTO
from typing import Optional, Set
from typing_extensions import Self

class DimensionFilterDTO(BaseModel):
    """
    A dimension associated with the selection concept.
    """ # noqa: E501
    dimension_name: Optional[StrictStr] = Field(default=None, description="The display name of the dimension.", alias="dimensionName")
    qualifying_path: Optional[QualifyingPathDTO] = Field(default=None, description="The objects that qualify the path to the dimension from its parent analytic object. For example, let's say the analytic object is `Applicant` and the dimension is `Location`. To get from `Location` to `Applicant` there are multiple paths, one of which is to follow references `Requisition` and then `Hiring Manager` to `Location`. `Location` is available on `Hiring_Manager` because a hiring manager is an `Employee`. In this example, the qualifying path is `Requisition.Hiring_Manager`.", alias="qualifyingPath")
    member_selection_list: Optional[MemberSelectionListDTO] = Field(default=None, description="The dimension members in a member selection concept.", alias="memberSelectionList")
    __properties: ClassVar[List[str]] = ["dimensionName", "qualifyingPath", "memberSelectionList"]

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
        """Create an instance of DimensionFilterDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of qualifying_path
        if self.qualifying_path:
            _dict['qualifyingPath'] = self.qualifying_path.to_dict()
        # override the default output from pydantic by calling `to_dict()` of member_selection_list
        if self.member_selection_list:
            _dict['memberSelectionList'] = self.member_selection_list.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DimensionFilterDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dimensionName": obj.get("dimensionName"),
            "qualifyingPath": QualifyingPathDTO.from_dict(obj["qualifyingPath"]) if obj.get("qualifyingPath") is not None else None,
            "memberSelectionList": MemberSelectionListDTO.from_dict(obj["memberSelectionList"]) if obj.get("memberSelectionList") is not None else None
        })
        return _obj


