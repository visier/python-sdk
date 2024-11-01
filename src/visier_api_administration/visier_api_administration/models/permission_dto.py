# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1551
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_administration.models.admin_capability_config_dto import AdminCapabilityConfigDTO
from visier_api_administration.models.data_security_profile_dto import DataSecurityProfileDTO
from visier_api_administration.models.role_modules_config_dto import RoleModulesConfigDTO
from typing import Optional, Set
from typing_extensions import Self

class PermissionDTO(BaseModel):
    """
    PermissionDTO
    """ # noqa: E501
    admin_capability_config: Optional[AdminCapabilityConfigDTO] = Field(default=None, description="The capabilities assigned in the permission.", alias="adminCapabilityConfig")
    data_security_profiles: Optional[List[DataSecurityProfileDTO]] = Field(default=None, description="A list of objects representing the data security for each item in a permission.", alias="dataSecurityProfiles")
    description: Optional[StrictStr] = Field(default=None, description="A user-defined description of the permission.")
    display_name: Optional[StrictStr] = Field(default=None, description="An identifiable permission name to display in Visier, such as \"Diversity Access\".", alias="displayName")
    permission_id: Optional[StrictStr] = Field(default=None, description="The unique identifier associated with the permission.", alias="permissionId")
    role_modules_config: Optional[RoleModulesConfigDTO] = Field(default=None, description="A list of content packages assigned to the permission.", alias="roleModulesConfig")
    __properties: ClassVar[List[str]] = ["adminCapabilityConfig", "dataSecurityProfiles", "description", "displayName", "permissionId", "roleModulesConfig"]

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
        """Create an instance of PermissionDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of admin_capability_config
        if self.admin_capability_config:
            _dict['adminCapabilityConfig'] = self.admin_capability_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in data_security_profiles (list)
        _items = []
        if self.data_security_profiles:
            for _item_data_security_profiles in self.data_security_profiles:
                if _item_data_security_profiles:
                    _items.append(_item_data_security_profiles.to_dict())
            _dict['dataSecurityProfiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of role_modules_config
        if self.role_modules_config:
            _dict['roleModulesConfig'] = self.role_modules_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PermissionDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adminCapabilityConfig": AdminCapabilityConfigDTO.from_dict(obj["adminCapabilityConfig"]) if obj.get("adminCapabilityConfig") is not None else None,
            "dataSecurityProfiles": [DataSecurityProfileDTO.from_dict(_item) for _item in obj["dataSecurityProfiles"]] if obj.get("dataSecurityProfiles") is not None else None,
            "description": obj.get("description"),
            "displayName": obj.get("displayName"),
            "permissionId": obj.get("permissionId"),
            "roleModulesConfig": RoleModulesConfigDTO.from_dict(obj["roleModulesConfig"]) if obj.get("roleModulesConfig") is not None else None
        })
        return _obj


