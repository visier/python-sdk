# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1531
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
from visier_api_administration.models.failed_local_tenant_profile_assignment_dto import FailedLocalTenantProfileAssignmentDTO
from visier_api_administration.models.successful_local_tenant_profile_assignment_dto import SuccessfulLocalTenantProfileAssignmentDTO
from visier_api_administration.models.user_id_error_dto import UserIdErrorDTO
from typing import Optional, Set
from typing_extensions import Self

class LocalTenantProfileAssignmentResponseDTO(BaseModel):
    """
    LocalTenantProfileAssignmentResponseDTO
    """ # noqa: E501
    bad_user_ids: Optional[List[UserIdErrorDTO]] = Field(default=None, description="A list of objects representing the user IDs that may not be valid.", alias="badUserIds")
    errors: Optional[StrictBool] = Field(default=None, description="If true, an error was generated by the request.")
    failed_assignments: Optional[List[FailedLocalTenantProfileAssignmentDTO]] = Field(default=None, description="A list of objects representing any errors that occurred during the assignment operation.", alias="failedAssignments")
    successful_assignments: Optional[List[SuccessfulLocalTenantProfileAssignmentDTO]] = Field(default=None, description="A list of the user IDs that were successfully assigned the profile.", alias="successfulAssignments")
    __properties: ClassVar[List[str]] = ["badUserIds", "errors", "failedAssignments", "successfulAssignments"]

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
        """Create an instance of LocalTenantProfileAssignmentResponseDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in bad_user_ids (list)
        _items = []
        if self.bad_user_ids:
            for _item_bad_user_ids in self.bad_user_ids:
                if _item_bad_user_ids:
                    _items.append(_item_bad_user_ids.to_dict())
            _dict['badUserIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in failed_assignments (list)
        _items = []
        if self.failed_assignments:
            for _item_failed_assignments in self.failed_assignments:
                if _item_failed_assignments:
                    _items.append(_item_failed_assignments.to_dict())
            _dict['failedAssignments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in successful_assignments (list)
        _items = []
        if self.successful_assignments:
            for _item_successful_assignments in self.successful_assignments:
                if _item_successful_assignments:
                    _items.append(_item_successful_assignments.to_dict())
            _dict['successfulAssignments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LocalTenantProfileAssignmentResponseDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "badUserIds": [UserIdErrorDTO.from_dict(_item) for _item in obj["badUserIds"]] if obj.get("badUserIds") is not None else None,
            "errors": obj.get("errors"),
            "failedAssignments": [FailedLocalTenantProfileAssignmentDTO.from_dict(_item) for _item in obj["failedAssignments"]] if obj.get("failedAssignments") is not None else None,
            "successfulAssignments": [SuccessfulLocalTenantProfileAssignmentDTO.from_dict(_item) for _item in obj["successfulAssignments"]] if obj.get("successfulAssignments") is not None else None
        })
        return _obj


