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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_administration.models.servicing_publicapi_transfers_failed_local_tenant_profile_revoke_dto import ServicingPublicapiTransfersFailedLocalTenantProfileRevokeDTO
from visier_api_administration.models.servicing_publicapi_transfers_successful_local_tenant_profile_assignment_dto import ServicingPublicapiTransfersSuccessfulLocalTenantProfileAssignmentDTO
from typing import Optional, Set
from typing_extensions import Self

class ServicingPublicapiTransfersLocalTenantProfileRevokeResponseDTO(BaseModel):
    """
    ServicingPublicapiTransfersLocalTenantProfileRevokeResponseDTO
    """ # noqa: E501
    failed: Optional[List[ServicingPublicapiTransfersFailedLocalTenantProfileRevokeDTO]] = Field(default=None, description="A list of objects representing any errors that occurred during the assignment operation.")
    succeeded: Optional[List[ServicingPublicapiTransfersSuccessfulLocalTenantProfileAssignmentDTO]] = Field(default=None, description="A list of the user IDs that successfully had a profile removed.")
    __properties: ClassVar[List[str]] = ["failed", "succeeded"]

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
        """Create an instance of ServicingPublicapiTransfersLocalTenantProfileRevokeResponseDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in failed (list)
        _items = []
        if self.failed:
            for _item_failed in self.failed:
                if _item_failed:
                    _items.append(_item_failed.to_dict())
            _dict['failed'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in succeeded (list)
        _items = []
        if self.succeeded:
            for _item_succeeded in self.succeeded:
                if _item_succeeded:
                    _items.append(_item_succeeded.to_dict())
            _dict['succeeded'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServicingPublicapiTransfersLocalTenantProfileRevokeResponseDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "failed": [ServicingPublicapiTransfersFailedLocalTenantProfileRevokeDTO.from_dict(_item) for _item in obj["failed"]] if obj.get("failed") is not None else None,
            "succeeded": [ServicingPublicapiTransfersSuccessfulLocalTenantProfileAssignmentDTO.from_dict(_item) for _item in obj["succeeded"]] if obj.get("succeeded") is not None else None
        })
        return _obj


