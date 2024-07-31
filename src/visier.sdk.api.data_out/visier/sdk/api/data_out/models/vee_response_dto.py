# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 0.0.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier.sdk.api.data_out.models.vee_data_dto import VeeDataDTO
from visier.sdk.api.data_out.models.vee_query_corrections_dto import VeeQueryCorrectionsDTO
from visier.sdk.api.data_out.models.vee_response_schema_dto import VeeResponseSchemaDTO
from visier.sdk.api.data_out.models.vee_status_code_dto import VeeStatusCodeDTO
from visier.sdk.api.data_out.models.vee_thread_state_dto import VeeThreadStateDTO
from visier.sdk.api.data_out.models.vee_visual_dto import VeeVisualDTO
from typing import Optional, Set
from typing_extensions import Self

class VeeResponseDTO(BaseModel):
    """
    Server Response DTOs
    """ # noqa: E501
    chart_url: Optional[StrictStr] = Field(default=None, alias="chartUrl")
    corrections: Optional[VeeQueryCorrectionsDTO] = None
    data: Optional[VeeDataDTO] = None
    narrative: Optional[StrictStr] = None
    reworded_question: Optional[StrictStr] = Field(default=None, alias="rewordedQuestion")
    var_schema: Optional[VeeResponseSchemaDTO] = Field(default=None, alias="schema")
    status_code: Optional[VeeStatusCodeDTO] = Field(default=None, alias="statusCode")
    thread_state: Optional[VeeThreadStateDTO] = Field(default=None, alias="threadState")
    visual: Optional[VeeVisualDTO] = None
    __properties: ClassVar[List[str]] = ["chartUrl", "corrections", "data", "narrative", "rewordedQuestion", "schema", "statusCode", "threadState", "visual"]

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
        # override the default output from pydantic by calling `to_dict()` of corrections
        if self.corrections:
            _dict['corrections'] = self.corrections.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status_code
        if self.status_code:
            _dict['statusCode'] = self.status_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of thread_state
        if self.thread_state:
            _dict['threadState'] = self.thread_state.to_dict()
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
            "corrections": VeeQueryCorrectionsDTO.from_dict(obj["corrections"]) if obj.get("corrections") is not None else None,
            "data": VeeDataDTO.from_dict(obj["data"]) if obj.get("data") is not None else None,
            "narrative": obj.get("narrative"),
            "rewordedQuestion": obj.get("rewordedQuestion"),
            "schema": VeeResponseSchemaDTO.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "statusCode": VeeStatusCodeDTO.from_dict(obj["statusCode"]) if obj.get("statusCode") is not None else None,
            "threadState": VeeThreadStateDTO.from_dict(obj["threadState"]) if obj.get("threadState") is not None else None,
            "visual": VeeVisualDTO.from_dict(obj["visual"]) if obj.get("visual") is not None else None
        })
        return _obj


