# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1701
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ReportDTO(BaseModel):
    """
    The information of a single report.
    """ # noqa: E501
    allowed_actions: Optional[List[StrictStr]] = Field(default=None, description="The actions that you can perform on the report.   Valid values are:  - `duplicate`: The user can make their own copy of this report.  - `delete`: The user can delete this report.  - `edit`: The user can edit this report directly.  - `download`: The user can download this report as a CSV.  - `share`: The user can share this report with other users or user groups.", alias="allowedActions")
    description: Optional[StrictStr] = Field(default=None, description="The localized description of the report.")
    id: Optional[StrictStr] = Field(default=None, description="The unique ID of the report.")
    is_owned_by_user: Optional[StrictBool] = Field(default=None, description="If `true`, you are the owner of the report.", alias="isOwnedByUser")
    is_published_report: Optional[StrictBool] = Field(default=None, description="If `true`, the report is published through a project.", alias="isPublishedReport")
    link: Optional[StrictStr] = Field(default=None, description="The link to the report.")
    owner: Optional[StrictStr] = Field(default=None, description="The owner of the report.")
    title: Optional[StrictStr] = Field(default=None, description="The localized title of the report.")
    updated_time: Optional[StrictStr] = Field(default=None, description="The time in epoch milliseconds when the report was last updated.", alias="updatedTime")
    __properties: ClassVar[List[str]] = ["allowedActions", "description", "id", "isOwnedByUser", "isPublishedReport", "link", "owner", "title", "updatedTime"]

    @field_validator('allowed_actions')
    def allowed_actions_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['duplicate', 'delete', 'edit', 'download', 'share']):
                raise ValueError("each list item must be one of ('duplicate', 'delete', 'edit', 'download', 'share')")
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
        """Create an instance of ReportDTO from a JSON string"""
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
        """Create an instance of ReportDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowedActions": obj.get("allowedActions"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "isOwnedByUser": obj.get("isOwnedByUser"),
            "isPublishedReport": obj.get("isPublishedReport"),
            "link": obj.get("link"),
            "owner": obj.get("owner"),
            "title": obj.get("title"),
            "updatedTime": obj.get("updatedTime")
        })
        return _obj


