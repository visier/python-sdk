# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1598
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_data_in.models.plan_data_load_change_list_dto import PlanDataLoadChangeListDTO
from visier_api_data_in.models.plan_data_load_error_dto import PlanDataLoadErrorDTO
from typing import Optional, Set
from typing_extensions import Self

class PlanDataUploadResponseDTO(BaseModel):
    """
    PlanDataUploadResponseDTO
    """ # noqa: E501
    changelists: Optional[List[PlanDataLoadChangeListDTO]] = Field(default=None, description="The collection of changes grouped by plan item made during the data load process. This list only contains the changes specified by the load. If you indicated in the request that the changes are to be rolled up or distributed, the values modified as a result of the calculations are not listed here.")
    errors: Optional[List[PlanDataLoadErrorDTO]] = Field(default=None, description="The collection of errors encountered during the data load process.")
    potential_updated_cells_count: Optional[StrictInt] = Field(default=None, description="The number of cells that would have been updated if all changes were saved.", alias="potentialUpdatedCellsCount")
    updated_cells_count: Optional[StrictInt] = Field(default=None, description="The number of cells that were updated from the data load process.", alias="updatedCellsCount")
    __properties: ClassVar[List[str]] = ["changelists", "errors", "potentialUpdatedCellsCount", "updatedCellsCount"]

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
        """Create an instance of PlanDataUploadResponseDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in changelists (list)
        _items = []
        if self.changelists:
            for _item_changelists in self.changelists:
                if _item_changelists:
                    _items.append(_item_changelists.to_dict())
            _dict['changelists'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item_errors in self.errors:
                if _item_errors:
                    _items.append(_item_errors.to_dict())
            _dict['errors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PlanDataUploadResponseDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "changelists": [PlanDataLoadChangeListDTO.from_dict(_item) for _item in obj["changelists"]] if obj.get("changelists") is not None else None,
            "errors": [PlanDataLoadErrorDTO.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "potentialUpdatedCellsCount": obj.get("potentialUpdatedCellsCount"),
            "updatedCellsCount": obj.get("updatedCellsCount")
        })
        return _obj


