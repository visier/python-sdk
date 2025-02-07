# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1725
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
from visier_api_data_out.models.member_filter_dto import MemberFilterDTO
from visier_api_data_out.models.selection_concept_reference_dto import SelectionConceptReferenceDTO
from typing import Optional, Set
from typing_extensions import Self

class KeyGroupFilterItemDTO(BaseModel):
    """
    An individual filter in a key group.
    """ # noqa: E501
    formula: Optional[StrictStr] = Field(default=None, description="A filter expressed as a formula.")
    member_set: Optional[MemberFilterDTO] = Field(default=None, description="A filter that includes or excludes dimension members.", alias="memberSet")
    selection_concept: Optional[SelectionConceptReferenceDTO] = Field(default=None, description="A filter that uses an existing selection concept in Visier.", alias="selectionConcept")
    __properties: ClassVar[List[str]] = ["formula", "memberSet", "selectionConcept"]

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
        """Create an instance of KeyGroupFilterItemDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of member_set
        if self.member_set:
            _dict['memberSet'] = self.member_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of selection_concept
        if self.selection_concept:
            _dict['selectionConcept'] = self.selection_concept.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeyGroupFilterItemDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "formula": obj.get("formula"),
            "memberSet": MemberFilterDTO.from_dict(obj["memberSet"]) if obj.get("memberSet") is not None else None,
            "selectionConcept": SelectionConceptReferenceDTO.from_dict(obj["selectionConcept"]) if obj.get("selectionConcept") is not None else None
        })
        return _obj


