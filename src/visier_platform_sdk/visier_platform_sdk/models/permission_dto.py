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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_platform_sdk.models.admin_capability_config_dto import AdminCapabilityConfigDTO
from visier_platform_sdk.models.data_security_profile_dto import DataSecurityProfileDTO
from visier_platform_sdk.models.role_modules_config_dto import RoleModulesConfigDTO
from typing import Optional, Set
from typing_extensions import Self

class PermissionDTO(BaseModel):
    """
    PermissionDTO
    """ # noqa: E501
    permission_id: Optional[StrictStr] = Field(default=None, description="The unique identifier associated with the permission.", alias="permissionId")
    display_name: Optional[StrictStr] = Field(default=None, description="An identifiable permission name to display in Visier, such as \"Diversity Access\".", alias="displayName")
    description: Optional[StrictStr] = Field(default=None, description="A user-defined description of the permission.")
    data_security_profiles: Optional[List[DataSecurityProfileDTO]] = Field(default=None, description="A list of objects representing the data security for each item in a permission.", alias="dataSecurityProfiles")
    admin_capability_config: Optional[AdminCapabilityConfigDTO] = Field(default=None, description="The capabilities assigned in the permission.", alias="adminCapabilityConfig")
    role_modules_config: Optional[RoleModulesConfigDTO] = Field(default=None, description="A list of content packages assigned to the permission.", alias="roleModulesConfig")
    __properties: ClassVar[List[str]] = ["permissionId", "displayName", "description", "dataSecurityProfiles", "adminCapabilityConfig", "roleModulesConfig"]

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
        # override the default output from pydantic by calling `to_dict()` of each item in data_security_profiles (list)
        _items = []
        if self.data_security_profiles:
            for _item_data_security_profiles in self.data_security_profiles:
                if _item_data_security_profiles:
                    _items.append(_item_data_security_profiles.to_dict())
            _dict['dataSecurityProfiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of admin_capability_config
        if self.admin_capability_config:
            _dict['adminCapabilityConfig'] = self.admin_capability_config.to_dict()
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
            "permissionId": obj.get("permissionId"),
            "displayName": obj.get("displayName"),
            "description": obj.get("description"),
            "dataSecurityProfiles": [DataSecurityProfileDTO.from_dict(_item) for _item in obj["dataSecurityProfiles"]] if obj.get("dataSecurityProfiles") is not None else None,
            "adminCapabilityConfig": AdminCapabilityConfigDTO.from_dict(obj["adminCapabilityConfig"]) if obj.get("adminCapabilityConfig") is not None else None,
            "roleModulesConfig": RoleModulesConfigDTO.from_dict(obj["roleModulesConfig"]) if obj.get("roleModulesConfig") is not None else None
        })
        return _obj


