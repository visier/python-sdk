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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_platform_sdk.models.cell_distribution_bin_dto import CellDistributionBinDTO
from typing import Optional, Set
from typing_extensions import Self

class CellDTO(BaseModel):
    """
    An individual value in a cell set.
    """ # noqa: E501
    value: Optional[StrictStr] = Field(default=None, description="The value of the cell.")
    support: Optional[StrictStr] = Field(default=None, description="The number of data points contributing to this cell.")
    coordinates: Optional[List[StrictInt]] = Field(default=None, description="A list of integers representing the coordinates of this cell, identifying its position along each axis.")
    distribution: Optional[List[CellDistributionBinDTO]] = Field(default=None, description="The optional distribution of this cell.  This will be populated if distribution calculation is requested, and supported by the query.")
    __properties: ClassVar[List[str]] = ["value", "support", "coordinates", "distribution"]

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
        """Create an instance of CellDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in distribution (list)
        _items = []
        if self.distribution:
            for _item_distribution in self.distribution:
                if _item_distribution:
                    _items.append(_item_distribution.to_dict())
            _dict['distribution'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CellDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "value": obj.get("value"),
            "support": obj.get("support"),
            "coordinates": obj.get("coordinates"),
            "distribution": [CellDistributionBinDTO.from_dict(_item) for _item in obj["distribution"]] if obj.get("distribution") is not None else None
        })
        return _obj


