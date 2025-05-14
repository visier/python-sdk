# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1905
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
from visier_api_administration.models.servicing_all_permissions_assigned_for_local_tenant_dto import ServicingAllPermissionsAssignedForLocalTenantDTO
from visier_api_administration.models.servicing_all_profile_assigned_for_local_tenant_dto import ServicingAllProfileAssignedForLocalTenantDTO
from visier_api_administration.models.servicing_all_user_groups_assigned_for_local_tenant_dto import ServicingAllUserGroupsAssignedForLocalTenantDTO
from visier_api_administration.models.servicing_last_login_dto import ServicingLastLoginDTO
from typing import Optional, Set
from typing_extensions import Self

class ServicingUserGetAPIResponseDTO(BaseModel):
    """
    ServicingUserGetAPIResponseDTO
    """ # noqa: E501
    user_id: Optional[StrictStr] = Field(default=None, description="The unique identifier associated with the user.", alias="userId")
    username: Optional[StrictStr] = Field(default=None, description="The user's username. This is typically the user's email, such as john@jupiter.com.")
    display_name: Optional[StrictStr] = Field(default=None, description="An identifiable name to display within Visier. For example, \"John Smith\".", alias="displayName")
    employee_id: Optional[StrictStr] = Field(default=None, description="If applicable, and if available, the user employee ID in the data.", alias="employeeId")
    account_enabled: Optional[StrictBool] = Field(default=None, description="If false, the user account is disabled.", alias="accountEnabled")
    profiles: Optional[ServicingAllProfileAssignedForLocalTenantDTO] = Field(default=None, description="A list of objects representing the list of available profiles. Not returned if the user has no profiles.")
    permissions: Optional[ServicingAllPermissionsAssignedForLocalTenantDTO] = Field(default=None, description="A list of objects representing the user's permissions.")
    user_groups: Optional[ServicingAllUserGroupsAssignedForLocalTenantDTO] = Field(default=None, description="A list of objects representing the available user groups.", alias="userGroups")
    last_login: Optional[ServicingLastLoginDTO] = Field(default=None, description="An object that represents the time that the user last logged into Visier.", alias="lastLogin")
    email: Optional[StrictStr] = Field(default=None, description="The user's email address.")
    __properties: ClassVar[List[str]] = ["userId", "username", "displayName", "employeeId", "accountEnabled", "profiles", "permissions", "userGroups", "lastLogin", "email"]

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
        """Create an instance of ServicingUserGetAPIResponseDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of profiles
        if self.profiles:
            _dict['profiles'] = self.profiles.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_groups
        if self.user_groups:
            _dict['userGroups'] = self.user_groups.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_login
        if self.last_login:
            _dict['lastLogin'] = self.last_login.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServicingUserGetAPIResponseDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "userId": obj.get("userId"),
            "username": obj.get("username"),
            "displayName": obj.get("displayName"),
            "employeeId": obj.get("employeeId"),
            "accountEnabled": obj.get("accountEnabled"),
            "profiles": ServicingAllProfileAssignedForLocalTenantDTO.from_dict(obj["profiles"]) if obj.get("profiles") is not None else None,
            "permissions": ServicingAllPermissionsAssignedForLocalTenantDTO.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "userGroups": ServicingAllUserGroupsAssignedForLocalTenantDTO.from_dict(obj["userGroups"]) if obj.get("userGroups") is not None else None,
            "lastLogin": ServicingLastLoginDTO.from_dict(obj["lastLogin"]) if obj.get("lastLogin") is not None else None,
            "email": obj.get("email")
        })
        return _obj


