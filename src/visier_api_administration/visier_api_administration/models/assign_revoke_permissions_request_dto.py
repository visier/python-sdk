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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_administration.models.assign_revoke_permission_request_dto import AssignRevokePermissionRequestDTO
from visier_api_administration.models.target_project_for_tenants_list_dto import TargetProjectForTenantsListDTO
from typing import Optional, Set
from typing_extensions import Self

class AssignRevokePermissionsRequestDTO(BaseModel):
    """
    Set permissions request  List of permissionId with assign to user Ids
    """ # noqa: E501
    permissions: Optional[List[AssignRevokePermissionRequestDTO]] = Field(default=None, description="A list of objects representing the permissions to assign to or remove from users.")
    target_project_for_tenants_list: Optional[TargetProjectForTenantsListDTO] = Field(default=None, description="Administrating tenants can specify the tenants and projects in which to assign permissions to users or remove permissions from users. Specify one `projectId` per `tenantCode`.  If omitted, the request is immediately published to production or applied to the `ProjectID` in the request header, if available, for the administrating tenant or TargetTenantID, if available.", alias="targetProjectForTenantsList")
    __properties: ClassVar[List[str]] = ["permissions", "targetProjectForTenantsList"]

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
        """Create an instance of AssignRevokePermissionsRequestDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item_permissions in self.permissions:
                if _item_permissions:
                    _items.append(_item_permissions.to_dict())
            _dict['permissions'] = _items
        # override the default output from pydantic by calling `to_dict()` of target_project_for_tenants_list
        if self.target_project_for_tenants_list:
            _dict['targetProjectForTenantsList'] = self.target_project_for_tenants_list.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssignRevokePermissionsRequestDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "permissions": [AssignRevokePermissionRequestDTO.from_dict(_item) for _item in obj["permissions"]] if obj.get("permissions") is not None else None,
            "targetProjectForTenantsList": TargetProjectForTenantsListDTO.from_dict(obj["targetProjectForTenantsList"]) if obj.get("targetProjectForTenantsList") is not None else None
        })
        return _obj


