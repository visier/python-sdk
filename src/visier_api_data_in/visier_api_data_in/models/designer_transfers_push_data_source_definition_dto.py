# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

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
from visier_api_data_in.models.designer_transfers_push_data_column_definition_dto import DesignerTransfersPushDataColumnDefinitionDTO
from typing import Optional, Set
from typing_extensions import Self

class DesignerTransfersPushDataSourceDefinitionDTO(BaseModel):
    """
    Details of each existing source.
    """ # noqa: E501
    columns: Optional[List[DesignerTransfersPushDataColumnDefinitionDTO]] = Field(default=None, description="A list of objects representing the source columns.")
    is_inherited: Optional[StrictBool] = Field(default=None, description="If true, the source is inherited by all analytic tenants.", alias="isInherited")
    name: Optional[StrictStr] = Field(default=None, description="The object name of the source.")
    source_id: Optional[StrictStr] = Field(default=None, description="The unique identifier associated with the source.", alias="sourceId")
    __properties: ClassVar[List[str]] = ["columns", "isInherited", "name", "sourceId"]

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
        """Create an instance of DesignerTransfersPushDataSourceDefinitionDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in columns (list)
        _items = []
        if self.columns:
            for _item_columns in self.columns:
                if _item_columns:
                    _items.append(_item_columns.to_dict())
            _dict['columns'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DesignerTransfersPushDataSourceDefinitionDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "columns": [DesignerTransfersPushDataColumnDefinitionDTO.from_dict(_item) for _item in obj["columns"]] if obj.get("columns") is not None else None,
            "isInherited": obj.get("isInherited"),
            "name": obj.get("name"),
            "sourceId": obj.get("sourceId")
        })
        return _obj


