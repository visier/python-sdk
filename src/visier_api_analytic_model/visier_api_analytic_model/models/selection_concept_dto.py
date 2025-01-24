# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1687
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
from visier_api_analytic_model.models.tag_map_element_dto import TagMapElementDTO
from typing import Optional, Set
from typing_extensions import Self

class SelectionConceptDTO(BaseModel):
    """
    Selection concepts select a population of subject members of a given subject or event.
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="The localized description of the selection concept.")
    display_name: Optional[StrictStr] = Field(default=None, description="The localized display name of the selection concept.", alias="displayName")
    explanation: Optional[StrictStr] = Field(default=None, description="The localized explanation of the selection concept.")
    id: Optional[StrictStr] = Field(default=None, description="The unique ID of the selection concept  Note: See `SelectionConcepts` to get the ID.")
    tags: Optional[List[TagMapElementDTO]] = Field(default=None, description="The optional collection of tags defined for this element.")
    visible_in_app: Optional[StrictBool] = Field(default=None, description="`true` if this selection concept is set to be visible in your solution.", alias="visibleInApp")
    __properties: ClassVar[List[str]] = ["description", "displayName", "explanation", "id", "tags", "visibleInApp"]

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
        """Create an instance of SelectionConceptDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SelectionConceptDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "displayName": obj.get("displayName"),
            "explanation": obj.get("explanation"),
            "id": obj.get("id"),
            "tags": [TagMapElementDTO.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "visibleInApp": obj.get("visibleInApp")
        })
        return _obj


