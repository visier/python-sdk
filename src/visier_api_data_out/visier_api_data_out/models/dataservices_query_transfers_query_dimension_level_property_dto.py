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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_data_out.models.dataservices_datamodel_transfers_dimension_reference_dto import DataservicesDatamodelTransfersDimensionReferenceDTO
from typing import Optional, Set
from typing_extensions import Self

class DataservicesQueryTransfersQueryDimensionLevelPropertyDTO(BaseModel):
    """
    A QueryDimensionLevelPropertyDTO defines an existing dimension level and its dimension to query.
    """ # noqa: E501
    dimension: Optional[DataservicesDatamodelTransfersDimensionReferenceDTO] = Field(default=None, description="A dimension and its qualifying path to query.")
    level_depth: Optional[StrictInt] = Field(default=None, description="The level depth.", alias="levelDepth")
    level_id: Optional[StrictStr] = Field(default=None, description="The level ID.", alias="levelId")
    member_value_mode: Optional[StrictStr] = Field(default=None, description="Controls how to display member values.   Valid values are `NAME`, `PATH`.   * `NAME`: Returns the member's display name. This is the default.  * `PATH`: Returns the member's name path.", alias="memberValueMode")
    __properties: ClassVar[List[str]] = ["dimension", "levelDepth", "levelId", "memberValueMode"]

    @field_validator('member_value_mode')
    def member_value_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NAME', 'PATH']):
            raise ValueError("must be one of enum values ('NAME', 'PATH')")
        return value

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
        """Create an instance of DataservicesQueryTransfersQueryDimensionLevelPropertyDTO from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataservicesQueryTransfersQueryDimensionLevelPropertyDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dimension": DataservicesDatamodelTransfersDimensionReferenceDTO.from_dict(obj["dimension"]) if obj.get("dimension") is not None else None,
            "levelDepth": obj.get("levelDepth"),
            "levelId": obj.get("levelId"),
            "memberValueMode": obj.get("memberValueMode")
        })
        return _obj


