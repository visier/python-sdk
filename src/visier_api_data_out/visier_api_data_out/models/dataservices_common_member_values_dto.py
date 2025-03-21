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
from visier_api_data_out.models.dataservices_common_dimension_member_reference_dto import DataservicesCommonDimensionMemberReferenceDTO
from typing import Optional, Set
from typing_extensions import Self

class DataservicesCommonMemberValuesDTO(BaseModel):
    """
    Member filter values are discrete member references in a dimension filter. You can define  included and excluded members simultaneously. This is typically done with filtering applied on  dimensions with multiple levels. For example, a Location parameter may include “South  America” and exclude “Brazil” which results in the metric being evaluated for all South American  countries except Brazil.
    """ # noqa: E501
    excluded: Optional[List[DataservicesCommonDimensionMemberReferenceDTO]] = Field(default=None, description="The unique IDs of members to exclude when evaluating the metric.")
    included: Optional[List[DataservicesCommonDimensionMemberReferenceDTO]] = Field(default=None, description="The unique IDs of members to include when evaluating the metric.")
    __properties: ClassVar[List[str]] = ["excluded", "included"]

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
        """Create an instance of DataservicesCommonMemberValuesDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in excluded (list)
        _items = []
        if self.excluded:
            for _item_excluded in self.excluded:
                if _item_excluded:
                    _items.append(_item_excluded.to_dict())
            _dict['excluded'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in included (list)
        _items = []
        if self.included:
            for _item_included in self.included:
                if _item_included:
                    _items.append(_item_included.to_dict())
            _dict['included'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataservicesCommonMemberValuesDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "excluded": [DataservicesCommonDimensionMemberReferenceDTO.from_dict(_item) for _item in obj["excluded"]] if obj.get("excluded") is not None else None,
            "included": [DataservicesCommonDimensionMemberReferenceDTO.from_dict(_item) for _item in obj["included"]] if obj.get("included") is not None else None
        })
        return _obj


