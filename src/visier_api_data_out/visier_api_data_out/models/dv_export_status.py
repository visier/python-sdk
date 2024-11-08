# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1559
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
from typing import Optional, Set
from typing_extensions import Self

class DvExportStatus(BaseModel):
    """
    The response structure for errors.
    """ # noqa: E501
    error_code: Optional[StrictStr] = Field(default=None, description="Error classification.", alias="errorCode")
    localized_message: Optional[StrictStr] = Field(default=None, description="Localized error message describing the root cause of the error.", alias="localizedMessage")
    message: Optional[StrictStr] = Field(default=None, description="Not used.")
    rci: Optional[StrictStr] = Field(default=None, description="Optional root cause identifier.")
    user_error: Optional[StrictBool] = Field(default=None, description="Indicates whether the error is a user error.", alias="userError")
    __properties: ClassVar[List[str]] = ["errorCode", "localizedMessage", "message", "rci", "userError"]

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
        """Create an instance of DvExportStatus from a JSON string"""
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
        """Create an instance of DvExportStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "errorCode": obj.get("errorCode"),
            "localizedMessage": obj.get("localizedMessage"),
            "message": obj.get("message"),
            "rci": obj.get("rci"),
            "userError": obj.get("userError")
        })
        return _obj


