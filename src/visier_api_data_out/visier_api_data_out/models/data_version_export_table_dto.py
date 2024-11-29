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
from visier_api_data_out.models.data_version_export_file_dto import DataVersionExportFileDTO
from typing import Optional, Set
from typing_extensions import Self

class DataVersionExportTableDTO(BaseModel):
    """
    DataVersionExportTableDTO
    """ # noqa: E501
    common_columns: Optional[DataVersionExportFileDTO] = Field(default=None, description="Information about the columns and files that are in both `dataVersionNumber` and `baseDataVersionNumber`. Always empty for full exports where `baseDataVersionNumber` is not specified.", alias="commonColumns")
    deleted_columns: Optional[List[StrictStr]] = Field(default=None, description="Information about columns that do not exist in `dataVersionNumber` but did exist in `baseDataVersionNumber`.", alias="deletedColumns")
    name: Optional[StrictStr] = Field(default=None, description="The name of a table in the data version export; for example, Employee or Applicant.")
    new_columns: Optional[DataVersionExportFileDTO] = Field(default=None, description="Information about new columns and files in the data version.  If full export, lists all columns. If delta export, lists columns that exist in `dataVersionNumber` but not in `baseDataVersionNumber`.", alias="newColumns")
    __properties: ClassVar[List[str]] = ["commonColumns", "deletedColumns", "name", "newColumns"]

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
        """Create an instance of DataVersionExportTableDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of common_columns
        if self.common_columns:
            _dict['commonColumns'] = self.common_columns.to_dict()
        # override the default output from pydantic by calling `to_dict()` of new_columns
        if self.new_columns:
            _dict['newColumns'] = self.new_columns.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataVersionExportTableDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "commonColumns": DataVersionExportFileDTO.from_dict(obj["commonColumns"]) if obj.get("commonColumns") is not None else None,
            "deletedColumns": obj.get("deletedColumns"),
            "name": obj.get("name"),
            "newColumns": DataVersionExportFileDTO.from_dict(obj["newColumns"]) if obj.get("newColumns") is not None else None
        })
        return _obj


