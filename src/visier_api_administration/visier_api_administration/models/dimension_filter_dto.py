# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1456
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_administration.models.dynamic_dimension_filter_dto import DynamicDimensionFilterDTO
from visier_api_administration.models.static_dimension_filter_dto import StaticDimensionFilterDTO
from typing import Optional, Set
from typing_extensions import Self

class DimensionFilterDTO(BaseModel):
    """
    DimensionFilterDTO
    """ # noqa: E501
    dynamic_dimension_filter: Optional[DynamicDimensionFilterDTO] = Field(default=None, alias="dynamicDimensionFilter")
    static_dimension_filter: Optional[StaticDimensionFilterDTO] = Field(default=None, alias="staticDimensionFilter")
    __properties: ClassVar[List[str]] = ["dynamicDimensionFilter", "staticDimensionFilter"]

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
        """Create an instance of DimensionFilterDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dynamic_dimension_filter
        if self.dynamic_dimension_filter:
            _dict['dynamicDimensionFilter'] = self.dynamic_dimension_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of static_dimension_filter
        if self.static_dimension_filter:
            _dict['staticDimensionFilter'] = self.static_dimension_filter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DimensionFilterDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dynamicDimensionFilter": DynamicDimensionFilterDTO.from_dict(obj["dynamicDimensionFilter"]) if obj.get("dynamicDimensionFilter") is not None else None,
            "staticDimensionFilter": StaticDimensionFilterDTO.from_dict(obj["staticDimensionFilter"]) if obj.get("staticDimensionFilter") is not None else None
        })
        return _obj

