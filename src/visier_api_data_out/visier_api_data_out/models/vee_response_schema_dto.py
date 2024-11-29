# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1614
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
from visier_api_data_out.models.vee_response_schema_reference_dto import VeeResponseSchemaReferenceDTO
from typing import Optional, Set
from typing_extensions import Self

class VeeResponseSchemaDTO(BaseModel):
    """
    VeeResponseSchemaDTO
    """ # noqa: E501
    concepts: Optional[List[VeeResponseSchemaReferenceDTO]] = Field(default=None, description="A list of the concepts that contribute to Vee's answer.")
    dimensions: Optional[List[VeeResponseSchemaReferenceDTO]] = Field(default=None, description="A list of the dimensions that contribute to Vee's answer.")
    metrics: Optional[List[StrictStr]] = Field(default=None, description="A list of the metrics that contribute to Vee's answer.")
    __properties: ClassVar[List[str]] = ["concepts", "dimensions", "metrics"]

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
        """Create an instance of VeeResponseSchemaDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in concepts (list)
        _items = []
        if self.concepts:
            for _item_concepts in self.concepts:
                if _item_concepts:
                    _items.append(_item_concepts.to_dict())
            _dict['concepts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in dimensions (list)
        _items = []
        if self.dimensions:
            for _item_dimensions in self.dimensions:
                if _item_dimensions:
                    _items.append(_item_dimensions.to_dict())
            _dict['dimensions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VeeResponseSchemaDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "concepts": [VeeResponseSchemaReferenceDTO.from_dict(_item) for _item in obj["concepts"]] if obj.get("concepts") is not None else None,
            "dimensions": [VeeResponseSchemaReferenceDTO.from_dict(_item) for _item in obj["dimensions"]] if obj.get("dimensions") is not None else None,
            "metrics": obj.get("metrics")
        })
        return _obj


