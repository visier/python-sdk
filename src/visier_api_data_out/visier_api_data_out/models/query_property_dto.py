# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

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
from visier_api_data_out.models.dimension_reference_dto import DimensionReferenceDTO
from visier_api_data_out.models.property_reference_dto import PropertyReferenceDTO
from visier_api_data_out.models.query_dimension_level_property_dto import QueryDimensionLevelPropertyDTO
from visier_api_data_out.models.query_member_map_property_dto import QueryMemberMapPropertyDTO
from visier_api_data_out.models.selection_concept_reference_dto import SelectionConceptReferenceDTO
from typing import Optional, Set
from typing_extensions import Self

class QueryPropertyDTO(BaseModel):
    """
    A QueryProperty defines a property of a data point returned from a query.  This is not the same as a `property` in Visier's data mode.
    """ # noqa: E501
    dimension: Optional[DimensionReferenceDTO] = Field(default=None, description="A dimension-based property that returns the full name path of the dimension member that the data point is mapped to.")
    dimension_level_selection: Optional[QueryDimensionLevelPropertyDTO] = Field(default=None, description="A dimension-based property that returns the member values of the dimension level.", alias="dimensionLevelSelection")
    effective_date_property: Optional[Dict[str, Any]] = Field(default=None, description="A property that yields the effective date for the record", alias="effectiveDateProperty")
    formula: Optional[StrictStr] = Field(default=None, description="A formula-based property.")
    member_map_property: Optional[QueryMemberMapPropertyDTO] = Field(default=None, description="A member map-based property that uses an existing member map in Visier.", alias="memberMapProperty")
    var_property: Optional[PropertyReferenceDTO] = Field(default=None, description="A property reference.", alias="property")
    selection_concept: Optional[SelectionConceptReferenceDTO] = Field(default=None, description="A selection concept-based property that returns true or false.", alias="selectionConcept")
    __properties: ClassVar[List[str]] = ["dimension", "dimensionLevelSelection", "effectiveDateProperty", "formula", "memberMapProperty", "property", "selectionConcept"]

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
        """Create an instance of QueryPropertyDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dimension
        if self.dimension:
            _dict['dimension'] = self.dimension.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dimension_level_selection
        if self.dimension_level_selection:
            _dict['dimensionLevelSelection'] = self.dimension_level_selection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of member_map_property
        if self.member_map_property:
            _dict['memberMapProperty'] = self.member_map_property.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_property
        if self.var_property:
            _dict['property'] = self.var_property.to_dict()
        # override the default output from pydantic by calling `to_dict()` of selection_concept
        if self.selection_concept:
            _dict['selectionConcept'] = self.selection_concept.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QueryPropertyDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dimension": DimensionReferenceDTO.from_dict(obj["dimension"]) if obj.get("dimension") is not None else None,
            "dimensionLevelSelection": QueryDimensionLevelPropertyDTO.from_dict(obj["dimensionLevelSelection"]) if obj.get("dimensionLevelSelection") is not None else None,
            "effectiveDateProperty": obj.get("effectiveDateProperty"),
            "formula": obj.get("formula"),
            "memberMapProperty": QueryMemberMapPropertyDTO.from_dict(obj["memberMapProperty"]) if obj.get("memberMapProperty") is not None else None,
            "property": PropertyReferenceDTO.from_dict(obj["property"]) if obj.get("property") is not None else None,
            "selectionConcept": SelectionConceptReferenceDTO.from_dict(obj["selectionConcept"]) if obj.get("selectionConcept") is not None else None
        })
        return _obj


