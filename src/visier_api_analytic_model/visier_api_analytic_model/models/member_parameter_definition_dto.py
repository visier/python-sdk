# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1772
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
from visier_api_analytic_model.models.member_values_dto import MemberValuesDTO
from typing import Optional, Set
from typing_extensions import Self

class MemberParameterDefinitionDTO(BaseModel):
    """
    The definition of a filter parameter. These elements are returned as part of the definition for metrics that include parameters in their definition.
    """ # noqa: E501
    default: Optional[MemberValuesDTO] = Field(default=None, description="The default value if the end user does not select a member at run time.")
    description: Optional[StrictStr] = Field(default=None, description="The localized description of the member parameter.")
    dimension_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the dimension on which the member parameter is based.", alias="dimensionId")
    display_name: Optional[StrictStr] = Field(default=None, description="The localized display name of the member parameter.", alias="displayName")
    id: Optional[StrictStr] = Field(default=None, description="The unique ID of the member parameter.")
    reference_path: Optional[List[StrictStr]] = Field(default=None, description="The analytic object reference path from the metric to the dimension.", alias="referencePath")
    __properties: ClassVar[List[str]] = ["default", "description", "dimensionId", "displayName", "id", "referencePath"]

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
        """Create an instance of MemberParameterDefinitionDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of default
        if self.default:
            _dict['default'] = self.default.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MemberParameterDefinitionDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "default": MemberValuesDTO.from_dict(obj["default"]) if obj.get("default") is not None else None,
            "description": obj.get("description"),
            "dimensionId": obj.get("dimensionId"),
            "displayName": obj.get("displayName"),
            "id": obj.get("id"),
            "referencePath": obj.get("referencePath")
        })
        return _obj


