# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1494
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
from visier_api_administration.models.project_dto import ProjectDTO
from typing import Optional, Set
from typing_extensions import Self

class GetProjectsAPIResponseDTO(BaseModel):
    """
    GetProjectsAPIResponseDTO
    """ # noqa: E501
    approval_projects: Optional[List[ProjectDTO]] = Field(default=None, description="A list of objects representing the accessible approval projects for the user.", alias="approvalProjects")
    archived_projects: Optional[List[ProjectDTO]] = Field(default=None, description="A list of objects representing the accessible archived projects for the user.", alias="archivedProjects")
    open_projects: Optional[List[ProjectDTO]] = Field(default=None, description="A list of objects representing the accessible open projects for the user.", alias="openProjects")
    rejected_projects: Optional[List[ProjectDTO]] = Field(default=None, description="A list of objects representing the accessible rejected projects for the user.", alias="rejectedProjects")
    __properties: ClassVar[List[str]] = ["approvalProjects", "archivedProjects", "openProjects", "rejectedProjects"]

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
        """Create an instance of GetProjectsAPIResponseDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in approval_projects (list)
        _items = []
        if self.approval_projects:
            for _item_approval_projects in self.approval_projects:
                if _item_approval_projects:
                    _items.append(_item_approval_projects.to_dict())
            _dict['approvalProjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in archived_projects (list)
        _items = []
        if self.archived_projects:
            for _item_archived_projects in self.archived_projects:
                if _item_archived_projects:
                    _items.append(_item_archived_projects.to_dict())
            _dict['archivedProjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in open_projects (list)
        _items = []
        if self.open_projects:
            for _item_open_projects in self.open_projects:
                if _item_open_projects:
                    _items.append(_item_open_projects.to_dict())
            _dict['openProjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rejected_projects (list)
        _items = []
        if self.rejected_projects:
            for _item_rejected_projects in self.rejected_projects:
                if _item_rejected_projects:
                    _items.append(_item_rejected_projects.to_dict())
            _dict['rejectedProjects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetProjectsAPIResponseDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "approvalProjects": [ProjectDTO.from_dict(_item) for _item in obj["approvalProjects"]] if obj.get("approvalProjects") is not None else None,
            "archivedProjects": [ProjectDTO.from_dict(_item) for _item in obj["archivedProjects"]] if obj.get("archivedProjects") is not None else None,
            "openProjects": [ProjectDTO.from_dict(_item) for _item in obj["openProjects"]] if obj.get("openProjects") is not None else None,
            "rejectedProjects": [ProjectDTO.from_dict(_item) for _item in obj["rejectedProjects"]] if obj.get("rejectedProjects") is not None else None
        })
        return _obj


