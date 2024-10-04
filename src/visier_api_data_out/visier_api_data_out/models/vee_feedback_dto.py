# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1508
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
from visier_api_data_out.models.vee_response_dto import VeeResponseDTO
from typing import Optional, Set
from typing_extensions import Self

class VeeFeedbackDTO(BaseModel):
    """
    The request body fields to submit Vee feedback.
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="A description of how Vee should have answered the question or how Vee can improve the answer; for example, \"Expected Headcount metric, but Vee returned Average Headcount\".")
    is_approved: Optional[StrictBool] = Field(default=None, description="If `true`, Vee answered the question correctly. If `false`, Vee's answer was incorrect or lacked details.", alias="isApproved")
    response: Optional[VeeResponseDTO] = Field(default=None, description="Your feedback about Vee's answer. Include the response object from the `/question` call that you want to provide feedback about.")
    __properties: ClassVar[List[str]] = ["description", "isApproved", "response"]

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
        """Create an instance of VeeFeedbackDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of response
        if self.response:
            _dict['response'] = self.response.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VeeFeedbackDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "isApproved": obj.get("isApproved"),
            "response": VeeResponseDTO.from_dict(obj["response"]) if obj.get("response") is not None else None
        })
        return _obj


