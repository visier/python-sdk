# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1793
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
from visier_api_administration.models.admin_publicapi_transfers_element_ids_dto import AdminPublicapiTransfersElementIDsDTO
from visier_api_administration.models.admin_publicapi_transfers_user_group_change_users_dto import AdminPublicapiTransfersUserGroupChangeUsersDTO
from typing import Optional, Set
from typing_extensions import Self

class AdminPublicapiTransfersUserGroupChangeDefinitionDTO(BaseModel):
    """
    AdminPublicapiTransfersUserGroupChangeDefinitionDTO
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="A detailed description of the population and purpose of the user group.")
    display_name: Optional[StrictStr] = Field(default=None, description="An identifiable user group name to display in Visier, such as \"Leadership User Group\".", alias="displayName")
    permission_ids: Optional[AdminPublicapiTransfersElementIDsDTO] = Field(default=None, description="The unique identifiers of permissions assigned to members of this user group.", alias="permissionIds")
    project_id: Optional[StrictStr] = Field(default=None, description="The project ID in which to update or create the user group.  If omitted and the ProjectID request header is not defined, the change is published to production immediately.", alias="projectId")
    tenant_code: Optional[StrictStr] = Field(default=None, description="The code of the tenant to which the user group belongs or should be created in.  Omit if creating or updating user groups in the current tenant.", alias="tenantCode")
    user_group_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the user group. Omit if creating a new user group.", alias="userGroupId")
    users: Optional[AdminPublicapiTransfersUserGroupChangeUsersDTO] = Field(default=None, description="The users assigned to the user group. You can define user group members dynamically with `dynamicFilterDefinition` or manually with `includeAllUsers` or `manuallyIncludedIds`.")
    __properties: ClassVar[List[str]] = ["description", "displayName", "permissionIds", "projectId", "tenantCode", "userGroupId", "users"]

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
        """Create an instance of AdminPublicapiTransfersUserGroupChangeDefinitionDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of permission_ids
        if self.permission_ids:
            _dict['permissionIds'] = self.permission_ids.to_dict()
        # override the default output from pydantic by calling `to_dict()` of users
        if self.users:
            _dict['users'] = self.users.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdminPublicapiTransfersUserGroupChangeDefinitionDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "displayName": obj.get("displayName"),
            "permissionIds": AdminPublicapiTransfersElementIDsDTO.from_dict(obj["permissionIds"]) if obj.get("permissionIds") is not None else None,
            "projectId": obj.get("projectId"),
            "tenantCode": obj.get("tenantCode"),
            "userGroupId": obj.get("userGroupId"),
            "users": AdminPublicapiTransfersUserGroupChangeUsersDTO.from_dict(obj["users"]) if obj.get("users") is not None else None
        })
        return _obj


