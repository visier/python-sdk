# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1627
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_analytic_model.models.property_type_dto import PropertyTypeDTO
from visier_api_analytic_model.models.tags_dto import TagsDTO
from typing import Optional, Set
from typing_extensions import Self

class PropertyChangeDefinitionDTO(BaseModel):
    """
    PropertyChangeDefinitionDTO
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="A short description of the property. Descriptions provide in-context help for your users while working in Visier.")
    designer_notes: Optional[StrictStr] = Field(default=None, description="Notes for the designer. This field is used to provide additional information about the property.", alias="designerNotes")
    display_name: Optional[StrictStr] = Field(default=None, description="The user-friendly name for the property.", alias="displayName")
    explanation: Optional[StrictStr] = Field(default=None, description="Explanation of the property. This field is used to provide additional information about the property.")
    id: Optional[StrictStr] = Field(default=None, description="The symbol name of the property; for example, Employee.Birth_Date")
    include_with_vee: Optional[StrictBool] = Field(default=None, description="If 'true', the property is included with Vee.", alias="includeWithVee")
    short_display_name: Optional[StrictStr] = Field(default=None, description="A shortened version of the display name. If the property is visible in the solution experience, this name is displayed in visualization titles.", alias="shortDisplayName")
    tags: Optional[TagsDTO] = Field(default=None, description="The tags associated with the property.")
    type: Optional[PropertyTypeDTO] = Field(default=None, description="The type of the property.")
    __properties: ClassVar[List[str]] = ["description", "designerNotes", "displayName", "explanation", "id", "includeWithVee", "shortDisplayName", "tags", "type"]

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
        """Create an instance of PropertyChangeDefinitionDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PropertyChangeDefinitionDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "designerNotes": obj.get("designerNotes"),
            "displayName": obj.get("displayName"),
            "explanation": obj.get("explanation"),
            "id": obj.get("id"),
            "includeWithVee": obj.get("includeWithVee"),
            "shortDisplayName": obj.get("shortDisplayName"),
            "tags": TagsDTO.from_dict(obj["tags"]) if obj.get("tags") is not None else None,
            "type": PropertyTypeDTO.from_dict(obj["type"]) if obj.get("type") is not None else None
        })
        return _obj


