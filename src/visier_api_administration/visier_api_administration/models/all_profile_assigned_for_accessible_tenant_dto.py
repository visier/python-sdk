# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1542
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
from visier_api_administration.models.profile_assigned_for_accessible_tenant_dto import ProfileAssignedForAccessibleTenantDTO
from typing import Optional, Set
from typing_extensions import Self

class AllProfileAssignedForAccessibleTenantDTO(BaseModel):
    """
    AllProfileAssignedForAccessibleTenantDTO
    """ # noqa: E501
    assigned_profiles_for_accessible_tenant: Optional[List[ProfileAssignedForAccessibleTenantDTO]] = Field(default=None, description="A list of objects representing the user profiles assigned to the user and their validity range.", alias="assignedProfilesForAccessibleTenant")
    __properties: ClassVar[List[str]] = ["assignedProfilesForAccessibleTenant"]

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
        """Create an instance of AllProfileAssignedForAccessibleTenantDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in assigned_profiles_for_accessible_tenant (list)
        _items = []
        if self.assigned_profiles_for_accessible_tenant:
            for _item_assigned_profiles_for_accessible_tenant in self.assigned_profiles_for_accessible_tenant:
                if _item_assigned_profiles_for_accessible_tenant:
                    _items.append(_item_assigned_profiles_for_accessible_tenant.to_dict())
            _dict['assignedProfilesForAccessibleTenant'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AllProfileAssignedForAccessibleTenantDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assignedProfilesForAccessibleTenant": [ProfileAssignedForAccessibleTenantDTO.from_dict(_item) for _item in obj["assignedProfilesForAccessibleTenant"]] if obj.get("assignedProfilesForAccessibleTenant") is not None else None
        })
        return _obj


