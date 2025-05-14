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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_administration.models.admin_element_ids_dto import AdminElementIDsDTO
from visier_api_administration.models.admin_user_group_filters_dto import AdminUserGroupFiltersDTO
from typing import Optional, Set
from typing_extensions import Self

class AdminUserGroupChangeUsersDTO(BaseModel):
    """
    AdminUserGroupChangeUsersDTO
    """ # noqa: E501
    include_all_users: Optional[StrictBool] = Field(default=None, description="If `true`, all users are included in the user group. If `true`:  * You can manually exclude users with `manuallyExcludedIds`.  * Cannot be combined with `manuallyIncludedIds` or `dynamicFilterDefinition`.", alias="includeAllUsers")
    manually_included_ids: Optional[AdminElementIDsDTO] = Field(default=None, description="Includes specified user IDs in the user group.  * May be combined with `dynamicFilterDefinition`.  * Omit if `includeAllUsers` is `true`.", alias="manuallyIncludedIds")
    manually_excluded_ids: Optional[AdminElementIDsDTO] = Field(default=None, description="Excludes specified user IDs from the user group.  * You can manually exclude users if `includeAllUsers` is `true` or if `dynamicFilterDefinition` is defined.  * Excluded IDs must not overlap with user IDs in `manuallyIncludedIds`.", alias="manuallyExcludedIds")
    dynamic_filter_definition: Optional[AdminUserGroupFiltersDTO] = Field(default=None, description="The filters that dynamically define a population through dimensions or dimensions accessible through references from the analytic object.  * Omit if `includeAllUsers` is `true`.  * You can combine dynamic filters with manually-assigned users.", alias="dynamicFilterDefinition")
    __properties: ClassVar[List[str]] = ["includeAllUsers", "manuallyIncludedIds", "manuallyExcludedIds", "dynamicFilterDefinition"]

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
        """Create an instance of AdminUserGroupChangeUsersDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of manually_included_ids
        if self.manually_included_ids:
            _dict['manuallyIncludedIds'] = self.manually_included_ids.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manually_excluded_ids
        if self.manually_excluded_ids:
            _dict['manuallyExcludedIds'] = self.manually_excluded_ids.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dynamic_filter_definition
        if self.dynamic_filter_definition:
            _dict['dynamicFilterDefinition'] = self.dynamic_filter_definition.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdminUserGroupChangeUsersDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "includeAllUsers": obj.get("includeAllUsers"),
            "manuallyIncludedIds": AdminElementIDsDTO.from_dict(obj["manuallyIncludedIds"]) if obj.get("manuallyIncludedIds") is not None else None,
            "manuallyExcludedIds": AdminElementIDsDTO.from_dict(obj["manuallyExcludedIds"]) if obj.get("manuallyExcludedIds") is not None else None,
            "dynamicFilterDefinition": AdminUserGroupFiltersDTO.from_dict(obj["dynamicFilterDefinition"]) if obj.get("dynamicFilterDefinition") is not None else None
        })
        return _obj


