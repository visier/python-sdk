# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1772
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
from visier_api_data_out.models.data_version_export_table_dto import DataVersionExportTableDTO
from typing import Optional, Set
from typing_extensions import Self

class DataVersionExportDTO(BaseModel):
    """
    DataVersionExportDTO
    """ # noqa: E501
    base_data_version_number: Optional[StrictStr] = Field(default=None, description="The baseline data version number for which the export was generated. If specified, the export is a delta of the differences between `dateVersionNumber` and `baseDataVersionNumber`. If empty, a full export is generated for `dataVersionNumber`.", alias="baseDataVersionNumber")
    data_version_number: Optional[StrictStr] = Field(default=None, description="The data version number for which the export was generated.", alias="dataVersionNumber")
    deleted_tables: Optional[List[StrictStr]] = Field(default=None, description="Tables that do not exist in `dataVersionNumber` but did exist in `baseDataVersionNumber`.", alias="deletedTables")
    new_tables: Optional[List[StrictStr]] = Field(default=None, description="Tables that exist in `dataVersionNumber` but did not exist in `baseDataVersionNumber`.", alias="newTables")
    tables: Optional[List[DataVersionExportTableDTO]] = Field(default=None, description="Information about the tables in the export.")
    timestamp: Optional[StrictStr] = Field(default=None, description="The date that the data version export was generated, in milliseconds since 1970-01-01T00:00:00Z.")
    uuid: Optional[StrictStr] = Field(default=None, description="The unique identifier of the data version export. Must be a valid UUID.")
    __properties: ClassVar[List[str]] = ["baseDataVersionNumber", "dataVersionNumber", "deletedTables", "newTables", "tables", "timestamp", "uuid"]

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
        """Create an instance of DataVersionExportDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tables (list)
        _items = []
        if self.tables:
            for _item_tables in self.tables:
                if _item_tables:
                    _items.append(_item_tables.to_dict())
            _dict['tables'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataVersionExportDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "baseDataVersionNumber": obj.get("baseDataVersionNumber"),
            "dataVersionNumber": obj.get("dataVersionNumber"),
            "deletedTables": obj.get("deletedTables"),
            "newTables": obj.get("newTables"),
            "tables": [DataVersionExportTableDTO.from_dict(_item) for _item in obj["tables"]] if obj.get("tables") is not None else None,
            "timestamp": obj.get("timestamp"),
            "uuid": obj.get("uuid")
        })
        return _obj


