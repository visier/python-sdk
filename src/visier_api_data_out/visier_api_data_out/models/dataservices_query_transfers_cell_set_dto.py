# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1793
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
from visier_api_data_out.models.dataservices_query_transfers_cell_dto import DataservicesQueryTransfersCellDTO
from visier_api_data_out.models.dataservices_query_transfers_cell_set_axis_dto import DataservicesQueryTransfersCellSetAxisDTO
from typing import Optional, Set
from typing_extensions import Self

class DataservicesQueryTransfersCellSetDTO(BaseModel):
    """
    The set of cells returned from executing an aggregation query.  A CellSet represents a structured, multidimensional array of values.
    """ # noqa: E501
    axes: Optional[List[DataservicesQueryTransfersCellSetAxisDTO]] = Field(default=None, description="The set of axes for the cell set that represent the objects the data is grouped by.")
    cells: Optional[List[DataservicesQueryTransfersCellDTO]] = Field(default=None, description="The set of cells that represent the result of your query.")
    lineage: Optional[DataservicesQueryTransfersLineageDTO] = Field(default=None, description="Lineage information for this cell set. This can be omitted if the cell has no lineage or the user did not request lineage information.")
    __properties: ClassVar[List[str]] = ["axes", "cells", "lineage"]

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
        """Create an instance of DataservicesQueryTransfersCellSetDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in axes (list)
        _items = []
        if self.axes:
            for _item_axes in self.axes:
                if _item_axes:
                    _items.append(_item_axes.to_dict())
            _dict['axes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in cells (list)
        _items = []
        if self.cells:
            for _item_cells in self.cells:
                if _item_cells:
                    _items.append(_item_cells.to_dict())
            _dict['cells'] = _items
        # override the default output from pydantic by calling `to_dict()` of lineage
        if self.lineage:
            _dict['lineage'] = self.lineage.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataservicesQueryTransfersCellSetDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "axes": [DataservicesQueryTransfersCellSetAxisDTO.from_dict(_item) for _item in obj["axes"]] if obj.get("axes") is not None else None,
            "cells": [DataservicesQueryTransfersCellDTO.from_dict(_item) for _item in obj["cells"]] if obj.get("cells") is not None else None,
            "lineage": DataservicesQueryTransfersLineageDTO.from_dict(obj["lineage"]) if obj.get("lineage") is not None else None
        })
        return _obj

from visier_api_data_out.models.dataservices_query_transfers_lineage_dto import DataservicesQueryTransfersLineageDTO
# TODO: Rewrite to not use raise_errors
DataservicesQueryTransfersCellSetDTO.model_rebuild(raise_errors=False)

