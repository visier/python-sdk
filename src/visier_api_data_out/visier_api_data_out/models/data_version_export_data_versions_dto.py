# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1508
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
from visier_api_data_out.models.data_version_export_data_version_summary_dto import DataVersionExportDataVersionSummaryDTO
from typing import Optional, Set
from typing_extensions import Self

class DataVersionExportDataVersionsDTO(BaseModel):
    """
    DataVersionExportDataVersionsDTO
    """ # noqa: E501
    data_versions: Optional[List[DataVersionExportDataVersionSummaryDTO]] = Field(default=None, description="All the available data versions for the tenant's primary data category.", alias="dataVersions")
    __properties: ClassVar[List[str]] = ["dataVersions"]

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
        """Create an instance of DataVersionExportDataVersionsDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data_versions (list)
        _items = []
        if self.data_versions:
            for _item_data_versions in self.data_versions:
                if _item_data_versions:
                    _items.append(_item_data_versions.to_dict())
            _dict['dataVersions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataVersionExportDataVersionsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataVersions": [DataVersionExportDataVersionSummaryDTO.from_dict(_item) for _item in obj["dataVersions"]] if obj.get("dataVersions") is not None else None
        })
        return _obj


