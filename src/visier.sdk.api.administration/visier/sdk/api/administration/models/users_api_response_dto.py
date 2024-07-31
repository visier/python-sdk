# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 0.1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier.sdk.api.administration.models.users_api_failure_dto import UsersAPIFailureDTO
from visier.sdk.api.administration.models.users_api_success_dto import UsersAPISuccessDTO
from typing import Optional, Set
from typing_extensions import Self

class UsersAPIResponseDTO(BaseModel):
    """
    UsersAPIResponseDTO
    """ # noqa: E501
    failures: Optional[List[UsersAPIFailureDTO]] = Field(default=None, description="The users for which the request failed.")
    successes: Optional[List[UsersAPISuccessDTO]] = Field(default=None, description="The users for which the request succeeded.")
    __properties: ClassVar[List[str]] = ["failures", "successes"]

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
        """Create an instance of UsersAPIResponseDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in failures (list)
        _items = []
        if self.failures:
            for _item in self.failures:
                if _item:
                    _items.append(_item.to_dict())
            _dict['failures'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in successes (list)
        _items = []
        if self.successes:
            for _item in self.successes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['successes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsersAPIResponseDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "failures": [UsersAPIFailureDTO.from_dict(_item) for _item in obj["failures"]] if obj.get("failures") is not None else None,
            "successes": [UsersAPISuccessDTO.from_dict(_item) for _item in obj["successes"]] if obj.get("successes") is not None else None
        })
        return _obj


