# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1687
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
from visier_api_data_in.models.data_transfer_result_detail import DataTransferResultDetail
from typing import Optional, Set
from typing_extensions import Self

class PushDataCompleteResponse(BaseModel):
    """
    PushDataCompleteResponse
    """ # noqa: E501
    data_receiving_job_id: Optional[StrictStr] = Field(default=None, description="The unique identifier associated with the receiving job.", alias="dataReceivingJobId")
    data_transfer_result_details: Optional[List[DataTransferResultDetail]] = Field(default=None, description="A list of objects representing the results of the transfer session.", alias="dataTransferResultDetails")
    message: Optional[StrictStr] = Field(default=None, description="A meaningful message about the transfer session.")
    status: Optional[StrictStr] = Field(default=None, description="The status of the transfer session. A completed session returns the status SUCCEED.")
    transfer_session_id: Optional[StrictStr] = Field(default=None, description="The unique identifier associated with the transfer session.", alias="transferSessionId")
    __properties: ClassVar[List[str]] = ["dataReceivingJobId", "dataTransferResultDetails", "message", "status", "transferSessionId"]

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
        """Create an instance of PushDataCompleteResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data_transfer_result_details (list)
        _items = []
        if self.data_transfer_result_details:
            for _item_data_transfer_result_details in self.data_transfer_result_details:
                if _item_data_transfer_result_details:
                    _items.append(_item_data_transfer_result_details.to_dict())
            _dict['dataTransferResultDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PushDataCompleteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataReceivingJobId": obj.get("dataReceivingJobId"),
            "dataTransferResultDetails": [DataTransferResultDetail.from_dict(_item) for _item in obj["dataTransferResultDetails"]] if obj.get("dataTransferResultDetails") is not None else None,
            "message": obj.get("message"),
            "status": obj.get("status"),
            "transferSessionId": obj.get("transferSessionId")
        })
        return _obj


