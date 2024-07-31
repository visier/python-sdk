# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 0.1.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier.sdk.api.administration.models.hierarchy_property_dto import HierarchyPropertyDTO
from typing import Optional, Set
from typing_extensions import Self

class SecurableDimensionDTO(BaseModel):
    """
    SecurableDimensionDTO
    """ # noqa: E501
    analytic_object_ids: Optional[List[StrictStr]] = Field(default=None, description="A list of analytic object IDs.", alias="analyticObjectIds")
    dimension_id: Optional[StrictStr] = Field(default=None, description="The dimension ID.", alias="dimensionId")
    display_name: Optional[StrictStr] = Field(default=None, description="An identifiable dimension name to display in Visier, such as \"Contract Type\".", alias="displayName")
    hierarchy_properties: Optional[List[HierarchyPropertyDTO]] = Field(default=None, description="The list of hierarchies you can map to a user in a permission's dynamic filter.", alias="hierarchyProperties")
    __properties: ClassVar[List[str]] = ["analyticObjectIds", "dimensionId", "displayName", "hierarchyProperties"]

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
        """Create an instance of SecurableDimensionDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in hierarchy_properties (list)
        _items = []
        if self.hierarchy_properties:
            for _item in self.hierarchy_properties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hierarchyProperties'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SecurableDimensionDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "analyticObjectIds": obj.get("analyticObjectIds"),
            "dimensionId": obj.get("dimensionId"),
            "displayName": obj.get("displayName"),
            "hierarchyProperties": [HierarchyPropertyDTO.from_dict(_item) for _item in obj["hierarchyProperties"]] if obj.get("hierarchyProperties") is not None else None
        })
        return _obj


