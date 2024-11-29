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
from typing import Optional, Set
from typing_extensions import Self

class LineageDTO(BaseModel):
    """
    Lineage information for a given cell set. This describes how a cell set is created from other cell sets.
    """ # noqa: E501
    cell_sets: Optional[List[CellSetDTO]] = Field(default=None, description="The cell sets that constitute this lineage.", alias="cellSets")
    op: Optional[StrictStr] = Field(default=None, description="The operation used to combine the cell sets of this lineage.")
    __properties: ClassVar[List[str]] = ["cellSets", "op"]

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
        """Create an instance of LineageDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in cell_sets (list)
        _items = []
        if self.cell_sets:
            for _item_cell_sets in self.cell_sets:
                if _item_cell_sets:
                    _items.append(_item_cell_sets.to_dict())
            _dict['cellSets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LineageDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cellSets": [CellSetDTO.from_dict(_item) for _item in obj["cellSets"]] if obj.get("cellSets") is not None else None,
            "op": obj.get("op")
        })
        return _obj

from visier_api_data_out.models.cell_set_dto import CellSetDTO
# TODO: Rewrite to not use raise_errors
LineageDTO.model_rebuild(raise_errors=False)

