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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_data_in.models.data_in_tenant import DataInTenant
from typing import Optional, Set
from typing_extensions import Self

class DataInPushDataResponse(BaseModel):
    """
    DataInPushDataResponse
    """ # noqa: E501
    message: Optional[StrictStr] = Field(default=None, description="Any additional information about the data transfer.")
    sequence: Optional[StrictInt] = Field(default=None, description="The unique sequence number associated with a batch of records.")
    status: Optional[StrictStr] = Field(default=None, description="The status of the data transfer.")
    tenants: Optional[List[DataInTenant]] = Field(default=None, description="A list of strings representing the tenants that data was pushed to and their data transfer results.")
    transfer_session_id: Optional[StrictStr] = Field(default=None, description="The unique identifier associated with the transfer session.", alias="transferSessionId")
    __properties: ClassVar[List[str]] = ["message", "sequence", "status", "tenants", "transferSessionId"]

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
        """Create an instance of DataInPushDataResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tenants (list)
        _items = []
        if self.tenants:
            for _item_tenants in self.tenants:
                if _item_tenants:
                    _items.append(_item_tenants.to_dict())
            _dict['tenants'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataInPushDataResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message": obj.get("message"),
            "sequence": obj.get("sequence"),
            "status": obj.get("status"),
            "tenants": [DataInTenant.from_dict(_item) for _item in obj["tenants"]] if obj.get("tenants") is not None else None,
            "transferSessionId": obj.get("transferSessionId")
        })
        return _obj


