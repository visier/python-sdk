# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1603
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
from visier_api_data_out.models.vee_conversation_state_dto import VeeConversationStateDTO
from visier_api_data_out.models.vee_corrections_dto import VeeCorrectionsDTO
from visier_api_data_out.models.vee_data_dto import VeeDataDTO
from visier_api_data_out.models.vee_response_schema_dto import VeeResponseSchemaDTO
from visier_api_data_out.models.vee_status_code_dto import VeeStatusCodeDTO
from visier_api_data_out.models.vee_visual_dto import VeeVisualDTO
from typing import Optional, Set
from typing_extensions import Self

class VeeResponseDTO(BaseModel):
    """
    The response after asking Vee a question.
    """ # noqa: E501
    chart_url: Optional[StrictStr] = Field(default=None, description="A URL to view the visualization in Visier.", alias="chartUrl")
    conversation_state: Optional[VeeConversationStateDTO] = Field(default=None, description="The current conversation's details. To ask a follow-up question or continue the conversation with Vee, include the `conversationState` from the response in your next `/question` call. To submit feedback about Vee's answer, copy the entire response into your `/feedback` call.", alias="conversationState")
    corrections: Optional[List[VeeCorrectionsDTO]] = Field(default=None, description="A list of corrections and clarifications if the question was ambiguous or Vee was unsure in the answer.")
    data: Optional[VeeDataDTO] = Field(default=None, description="Returned if `includeData` is `true`. Provides additional data relevant to the question, such as the visualization data and any filters applied to the visualization.")
    narrative: Optional[StrictStr] = Field(default=None, description="Vee's answer to the question.")
    reworded_question: Optional[StrictStr] = Field(default=None, description="Vee's plain language interpretation of the original question. For example, if you asked \"what is the headcount by gender in each org?\", Vee might reword the question as \"What is the gender breakdown of our workforce by organization this month?\".", alias="rewordedQuestion")
    var_schema: Optional[VeeResponseSchemaDTO] = Field(default=None, description="The metrics, dimensions, and concepts that contribute to Vee's answer.", alias="schema")
    status_code: Optional[VeeStatusCodeDTO] = Field(default=None, description="A status code indicating whether or not Vee successfully answered the question.", alias="statusCode")
    visual: Optional[VeeVisualDTO] = Field(default=None, description="A base64 string-encoded PNG of a visualization generated by Vee to answer a question. For example, Vee can return a Breakdown visualization if asked about the headcount in each organization.")
    __properties: ClassVar[List[str]] = ["chartUrl", "conversationState", "corrections", "data", "narrative", "rewordedQuestion", "schema", "statusCode", "visual"]

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
        """Create an instance of VeeResponseDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in corrections (list)
        _items = []
        if self.corrections:
            for _item_corrections in self.corrections:
                if _item_corrections:
                    _items.append(_item_corrections.to_dict())
            _dict['corrections'] = _items
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status_code
        if self.status_code:
            _dict['statusCode'] = self.status_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of visual
        if self.visual:
            _dict['visual'] = self.visual.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VeeResponseDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chartUrl": obj.get("chartUrl"),
            "conversationState": VeeConversationStateDTO.from_dict(obj["conversationState"]) if obj.get("conversationState") is not None else None,
            "corrections": [VeeCorrectionsDTO.from_dict(_item) for _item in obj["corrections"]] if obj.get("corrections") is not None else None,
            "data": VeeDataDTO.from_dict(obj["data"]) if obj.get("data") is not None else None,
            "narrative": obj.get("narrative"),
            "rewordedQuestion": obj.get("rewordedQuestion"),
            "schema": VeeResponseSchemaDTO.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "statusCode": VeeStatusCodeDTO.from_dict(obj["statusCode"]) if obj.get("statusCode") is not None else None,
            "visual": VeeVisualDTO.from_dict(obj["visual"]) if obj.get("visual") is not None else None
        })
        return _obj


