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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_data_out.models.dataservices_query_transfers_query_property_dto import DataservicesQueryTransfersQueryPropertyDTO
from typing import Optional, Set
from typing_extensions import Self

class DataservicesQueryTransfersQueryNumericRangesDTO(BaseModel):
    """
    A QueryNumericRanges groups data into specified ranges based on a property value.
    """ # noqa: E501
    include_all_member: Optional[StrictBool] = Field(default=None, description="If `true`, a member is included that represents all members on the axis. Default is false.", alias="includeAllMember")
    include_independent_zero_range: Optional[StrictBool] = Field(default=None, description="If `true`, 0 is an independent range. Default is false.", alias="includeIndependentZeroRange")
    include_negative: Optional[StrictBool] = Field(default=None, description="If `true`, negative ranges are included. Default is false.", alias="includeNegative")
    var_property: Optional[DataservicesQueryTransfersQueryPropertyDTO] = Field(default=None, description="The name and qualifying path of a numeric property. Non-numeric properties are not accepted.", alias="property")
    ranges: Optional[StrictStr] = Field(default=None, description="The ranges to group data into, expressed as a space-separated string of range-bound values.")
    __properties: ClassVar[List[str]] = ["includeAllMember", "includeIndependentZeroRange", "includeNegative", "property", "ranges"]

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
        """Create an instance of DataservicesQueryTransfersQueryNumericRangesDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_property
        if self.var_property:
            _dict['property'] = self.var_property.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataservicesQueryTransfersQueryNumericRangesDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "includeAllMember": obj.get("includeAllMember"),
            "includeIndependentZeroRange": obj.get("includeIndependentZeroRange"),
            "includeNegative": obj.get("includeNegative"),
            "property": DataservicesQueryTransfersQueryPropertyDTO.from_dict(obj["property"]) if obj.get("property") is not None else None,
            "ranges": obj.get("ranges")
        })
        return _obj


