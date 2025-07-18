# coding: utf-8

"""
    API Reference

    Detailed API reference documentation for Visier APIs. Includes all endpoints, headers, path parameters, query parameters, request body schema, response schema, JSON request samples, and JSON response samples.

    The version of the OpenAPI document: 22222222.99201.2050
    Contact: alpine@visier.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier_platform_sdk.models.calculated_selection_concept_dto import CalculatedSelectionConceptDTO
from visier_platform_sdk.models.member_selection_concept_dto import MemberSelectionConceptDTO
from visier_platform_sdk.models.process_concept_definition_dto import ProcessConceptDefinitionDTO
from typing import Optional, Set
from typing_extensions import Self

class ConceptTypeDetailsDTO(BaseModel):
    """
    ConceptTypeDetailsDTO
    """ # noqa: E501
    process: Optional[ProcessConceptDefinitionDTO] = Field(default=None, description="The process concept's associated objects, such as its analytic object and status dimension.")
    member_selection: Optional[MemberSelectionConceptDTO] = Field(default=None, description="The member selection concept's configuration, such as its dimension members.", alias="memberSelection")
    calculated_selection: Optional[CalculatedSelectionConceptDTO] = Field(default=None, description="The calculated selection concept's configuration, such as its formula.", alias="calculatedSelection")
    __properties: ClassVar[List[str]] = ["process", "memberSelection", "calculatedSelection"]

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
        """Create an instance of ConceptTypeDetailsDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of process
        if self.process:
            _dict['process'] = self.process.to_dict()
        # override the default output from pydantic by calling `to_dict()` of member_selection
        if self.member_selection:
            _dict['memberSelection'] = self.member_selection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of calculated_selection
        if self.calculated_selection:
            _dict['calculatedSelection'] = self.calculated_selection.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConceptTypeDetailsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "process": ProcessConceptDefinitionDTO.from_dict(obj["process"]) if obj.get("process") is not None else None,
            "memberSelection": MemberSelectionConceptDTO.from_dict(obj["memberSelection"]) if obj.get("memberSelection") is not None else None,
            "calculatedSelection": CalculatedSelectionConceptDTO.from_dict(obj["calculatedSelection"]) if obj.get("calculatedSelection") is not None else None
        })
        return _obj


