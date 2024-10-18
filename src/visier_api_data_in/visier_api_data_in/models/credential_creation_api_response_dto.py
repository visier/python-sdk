# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1531
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
from visier_api_data_in.models.subject_missing_access_dto import SubjectMissingAccessDTO
from typing import Optional, Set
from typing_extensions import Self

class CredentialCreationAPIResponseDTO(BaseModel):
    """
    CredentialCreationAPIResponseDTO
    """ # noqa: E501
    missing_connection_properties: Optional[List[SubjectMissingAccessDTO]] = Field(default=None, description="The properties that the credential cannot access despite successful authentication.  This is only returned for authentications that do not grant access to all data.", alias="missingConnectionProperties")
    object_name: Optional[StrictStr] = Field(default=None, description="The object name of the newly created credential.", alias="objectName")
    symbol_name: Optional[StrictStr] = Field(default=None, description="The symbol name of the newly created credential.", alias="symbolName")
    uuid: Optional[StrictStr] = Field(default=None, description="The unique ID of the newly created credential.")
    __properties: ClassVar[List[str]] = ["missingConnectionProperties", "objectName", "symbolName", "uuid"]

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
        """Create an instance of CredentialCreationAPIResponseDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in missing_connection_properties (list)
        _items = []
        if self.missing_connection_properties:
            for _item_missing_connection_properties in self.missing_connection_properties:
                if _item_missing_connection_properties:
                    _items.append(_item_missing_connection_properties.to_dict())
            _dict['missingConnectionProperties'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CredentialCreationAPIResponseDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "missingConnectionProperties": [SubjectMissingAccessDTO.from_dict(_item) for _item in obj["missingConnectionProperties"]] if obj.get("missingConnectionProperties") is not None else None,
            "objectName": obj.get("objectName"),
            "symbolName": obj.get("symbolName"),
            "uuid": obj.get("uuid")
        })
        return _obj


