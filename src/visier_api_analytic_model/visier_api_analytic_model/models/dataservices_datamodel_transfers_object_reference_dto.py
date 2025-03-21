# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DataservicesDatamodelTransfersObjectReferenceDTO(BaseModel):
    """
    A link between one analytic object and another. An ObjectReference allows you to discover the relationships between  analytic objects. In some queries, you may need to provide a qualifyingPath, which is built from ObjectReference information.
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="The localized description of the object reference.")
    display_name: Optional[StrictStr] = Field(default=None, description="The localized display name of the object reference.", alias="displayName")
    from_object: Optional[StrictStr] = Field(default=None, description="The ID of the referencing analytic object.", alias="fromObject")
    id: Optional[StrictStr] = Field(default=None, description="The unique ID of the object reference.")
    is_strong_reference: Optional[StrictBool] = Field(default=None, description="True if this is a strong reference.", alias="isStrongReference")
    to_object: Optional[StrictStr] = Field(default=None, description="The ID of the referenced analytic object.", alias="toObject")
    type: Optional[StrictStr] = Field(default=None, description="The type of object reference.")
    __properties: ClassVar[List[str]] = ["description", "displayName", "fromObject", "id", "isStrongReference", "toObject", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SUBJECT_REFERENCE', 'MULTI_VALUE_REFERENCE']):
            raise ValueError("must be one of enum values ('SUBJECT_REFERENCE', 'MULTI_VALUE_REFERENCE')")
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
        """Create an instance of DataservicesDatamodelTransfersObjectReferenceDTO from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataservicesDatamodelTransfersObjectReferenceDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "displayName": obj.get("displayName"),
            "fromObject": obj.get("fromObject"),
            "id": obj.get("id"),
            "isStrongReference": obj.get("isStrongReference"),
            "toObject": obj.get("toObject"),
            "type": obj.get("type")
        })
        return _obj


