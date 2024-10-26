# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1547
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ProfileAssignedForAccessibleTenantDTO(BaseModel):
    """
    ProfileAssignedForAccessibleTenantDTO
    """ # noqa: E501
    display_name: Optional[StrictStr] = Field(default=None, description="An identifiable profile name to display in Visier such as \"Partner Service Manager\".", alias="displayName")
    for_all_children: Optional[StrictBool] = Field(default=None, description="If true, the profile is assigned for all the analytic tenants of the administrating tenant.", alias="forAllChildren")
    profile_id: Optional[StrictStr] = Field(default=None, description="The unique identifier associated with the profile.", alias="profileId")
    tenant_code: Optional[StrictStr] = Field(default=None, description="The tenant code of the analytic tenant on which this profile is assigned.", alias="tenantCode")
    validity_end_time: Optional[StrictStr] = Field(default=None, description="An exclusive date-time when this profile is no longer active.   Note: Long.Max_Value means that endTime is undefined and is equivalent to permanent access.", alias="validityEndTime")
    validity_start_time: Optional[StrictStr] = Field(default=None, description="An inclusive date-time when this profile is active.   Note: Long.Min_Value means that startTime is undefined.", alias="validityStartTime")
    __properties: ClassVar[List[str]] = ["displayName", "forAllChildren", "profileId", "tenantCode", "validityEndTime", "validityStartTime"]

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
        """Create an instance of ProfileAssignedForAccessibleTenantDTO from a JSON string"""
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
        """Create an instance of ProfileAssignedForAccessibleTenantDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "displayName": obj.get("displayName"),
            "forAllChildren": obj.get("forAllChildren"),
            "profileId": obj.get("profileId"),
            "tenantCode": obj.get("tenantCode"),
            "validityEndTime": obj.get("validityEndTime"),
            "validityStartTime": obj.get("validityStartTime")
        })
        return _obj


