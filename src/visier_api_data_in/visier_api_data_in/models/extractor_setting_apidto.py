# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1547
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
from visier_api_data_in.models.extractor_setting_key_value_apidto import ExtractorSettingKeyValueAPIDTO
from typing import Optional, Set
from typing_extensions import Self

class ExtractorSettingAPIDTO(BaseModel):
    """
    ExtractorSettingAPIDTO
    """ # noqa: E501
    connector_id: Optional[StrictStr] = Field(default=None, description="The unique identifier associated with the data connector.", alias="connectorId")
    connector_settings: Optional[List[ExtractorSettingKeyValueAPIDTO]] = Field(default=None, description="A list of objects representing the settings that are available for the data connector.", alias="connectorSettings")
    display_name: Optional[StrictStr] = Field(default=None, description="An identifiable data connector name that is displayed within Visier.", alias="displayName")
    __properties: ClassVar[List[str]] = ["connectorId", "connectorSettings", "displayName"]

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
        """Create an instance of ExtractorSettingAPIDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in connector_settings (list)
        _items = []
        if self.connector_settings:
            for _item_connector_settings in self.connector_settings:
                if _item_connector_settings:
                    _items.append(_item_connector_settings.to_dict())
            _dict['connectorSettings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExtractorSettingAPIDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connectorId": obj.get("connectorId"),
            "connectorSettings": [ExtractorSettingKeyValueAPIDTO.from_dict(_item) for _item in obj["connectorSettings"]] if obj.get("connectorSettings") is not None else None,
            "displayName": obj.get("displayName")
        })
        return _obj


