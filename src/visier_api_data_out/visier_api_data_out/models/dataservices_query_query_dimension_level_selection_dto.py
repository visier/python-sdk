# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1892
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_data_out.models.dataservices_datamodel_dimension_reference_dto import DataservicesDatamodelDimensionReferenceDTO
from typing import Optional, Set
from typing_extensions import Self

class DataservicesQueryQueryDimensionLevelSelectionDTO(BaseModel):
    """
    A QueryDimensionLevelSelection allows you to select a dimension level and its members without  explicitly listing each member.
    """ # noqa: E501
    dimension: Optional[DataservicesDatamodelDimensionReferenceDTO] = Field(default=None, description="A dimension and its qualifying path to query.")
    level_ids: Optional[List[StrictStr]] = Field(default=None, description="A list of level IDs for the dimension levels that you want to query. For example, [\"Level_1\", \"Level_2\"]. To get a dimension's level IDs, call the Data Model API.", alias="levelIds")
    level_depths: Optional[List[StrictInt]] = Field(default=None, description="A list of level depths for the dimension levels that you want to query. For a parent-child dimension, depth must be greater than 0. For example, [1, 2]. To get a dimension's level depths, call the Data Model API.", alias="levelDepths")
    __properties: ClassVar[List[str]] = ["dimension", "levelIds", "levelDepths"]

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
        """Create an instance of DataservicesQueryQueryDimensionLevelSelectionDTO from a JSON string"""
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
        """Create an instance of DataservicesQueryQueryDimensionLevelSelectionDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dimension": DataservicesDatamodelDimensionReferenceDTO.from_dict(obj["dimension"]) if obj.get("dimension") is not None else None,
            "levelIds": obj.get("levelIds"),
            "levelDepths": obj.get("levelDepths")
        })
        return _obj


