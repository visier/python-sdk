# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1880
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
from visier_api_data_out.models.analysis_common_vee_conversation_state_dto import AnalysisCommonVeeConversationStateDTO
from visier_api_data_out.models.analysis_common_vee_options_dto import AnalysisCommonVeeOptionsDTO
from typing import Optional, Set
from typing_extensions import Self

class AnalysisCommonVeeQuestionDTO(BaseModel):
    """
    The request body fields to ask Vee a question.
    """ # noqa: E501
    question: Optional[StrictStr] = Field(default=None, description="The question to ask Vee. If asking a follow-up question or continuing a conversation with Vee, specify the `conversationState` object from the question's response.")
    conversation_state: Optional[AnalysisCommonVeeConversationStateDTO] = Field(default=None, description="The unique identifier of the conversation with Vee. If empty, starts a new conversation with Vee. If asking a follow-up question or continuing a conversation with Vee, specify the `conversationState` object from the question's response. To submit feedback about Vee's answer, copy the entire response into your `/feedback` call.", alias="conversationState")
    options: Optional[AnalysisCommonVeeOptionsDTO] = Field(default=None, description="Options to specify how Vee should respond to a question.")
    max_view_details_members: Optional[StrictInt] = Field(default=None, description="The maximum number of members to return in Detailed View.", alias="maxViewDetailsMembers")
    __properties: ClassVar[List[str]] = ["question", "conversationState", "options", "maxViewDetailsMembers"]

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
        """Create an instance of AnalysisCommonVeeQuestionDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of conversation_state
        if self.conversation_state:
            _dict['conversationState'] = self.conversation_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AnalysisCommonVeeQuestionDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "question": obj.get("question"),
            "conversationState": AnalysisCommonVeeConversationStateDTO.from_dict(obj["conversationState"]) if obj.get("conversationState") is not None else None,
            "options": AnalysisCommonVeeOptionsDTO.from_dict(obj["options"]) if obj.get("options") is not None else None,
            "maxViewDetailsMembers": obj.get("maxViewDetailsMembers")
        })
        return _obj


