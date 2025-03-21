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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DesignerTransfersDimensionsAuthParamsDTO(BaseModel):
    """
    DesignerTransfersDimensionsAuthParamsDTO
    """ # noqa: E501
    app_key: Optional[StrictStr] = Field(default=None, alias="appKey")
    client_id: Optional[StrictStr] = Field(default=None, alias="clientId")
    client_secret: Optional[StrictStr] = Field(default=None, alias="clientSecret")
    password: Optional[StrictStr] = None
    username: Optional[StrictStr] = None
    vanity_url: Optional[StrictStr] = Field(default=None, alias="vanityUrl")
    __properties: ClassVar[List[str]] = ["appKey", "clientId", "clientSecret", "password", "username", "vanityUrl"]

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
        """Create an instance of DesignerTransfersDimensionsAuthParamsDTO from a JSON string"""
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
        """Create an instance of DesignerTransfersDimensionsAuthParamsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "appKey": obj.get("appKey"),
            "clientId": obj.get("clientId"),
            "clientSecret": obj.get("clientSecret"),
            "password": obj.get("password"),
            "username": obj.get("username"),
            "vanityUrl": obj.get("vanityUrl")
        })
        return _obj


