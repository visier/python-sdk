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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_data_out.models.cell_set_axis_position_dto import CellSetAxisPositionDTO
from visier_api_data_out.models.dimension_reference_dto import DimensionReferenceDTO
from typing import Optional, Set
from typing_extensions import Self

class CellSetAxisDTO(BaseModel):
    """
    The axis of a cell set associated with a dimension.
    """ # noqa: E501
    dimension: Optional[DimensionReferenceDTO] = Field(default=None, description="The dimension associated with the axis.")
    positions: Optional[List[CellSetAxisPositionDTO]] = Field(default=None, description="A list of paths that represent the data's positions along the axis.")
    __properties: ClassVar[List[str]] = ["dimension", "positions"]

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
        """Create an instance of CellSetAxisDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in positions (list)
        _items = []
        if self.positions:
            for _item_positions in self.positions:
                if _item_positions:
                    _items.append(_item_positions.to_dict())
            _dict['positions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CellSetAxisDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dimension": DimensionReferenceDTO.from_dict(obj["dimension"]) if obj.get("dimension") is not None else None,
            "positions": [CellSetAxisPositionDTO.from_dict(_item) for _item in obj["positions"]] if obj.get("positions") is not None else None
        })
        return _obj


