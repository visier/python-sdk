# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1547
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
from visier_api_data_out.models.vee_visual_options_dto import VeeVisualOptionsDTO
from typing import Optional, Set
from typing_extensions import Self

class VeeOptionsDTO(BaseModel):
    """
    VeeOptionsDTO
    """ # noqa: E501
    data_format: Optional[StrictStr] = Field(default=None, description="The format to return visualization data in. Valid values: `json`.", alias="dataFormat")
    include_data: Optional[StrictBool] = Field(default=None, description="If `true`, returns additional data relevant to the question, including `dataJson` (visualization data) and `context` (filters applied to the visualization). Default is `false`.", alias="includeData")
    include_reworded_question: Optional[StrictBool] = Field(default=None, description="If `true`, returns Vee's plain language interpretation of the original question. For example, if you asked \"what is the headcount by gender in each org?\", Vee might reword the question as \"What is the gender breakdown of our workforce by organization this month?\". Default is `false`.", alias="includeRewordedQuestion")
    include_visual: Optional[StrictBool] = Field(default=None, description="If `true`, returns a base64 string-encoded PNG of a rendered visualization with Vee's answer. Default is `false`.", alias="includeVisual")
    visual_options: Optional[VeeVisualOptionsDTO] = Field(default=None, description="Specify how to render the visualization.", alias="visualOptions")
    __properties: ClassVar[List[str]] = ["dataFormat", "includeData", "includeRewordedQuestion", "includeVisual", "visualOptions"]

    @field_validator('data_format')
    def data_format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['json']):
            raise ValueError("must be one of enum values ('json')")
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
        """Create an instance of VeeOptionsDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of visual_options
        if self.visual_options:
            _dict['visualOptions'] = self.visual_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VeeOptionsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataFormat": obj.get("dataFormat"),
            "includeData": obj.get("includeData"),
            "includeRewordedQuestion": obj.get("includeRewordedQuestion"),
            "includeVisual": obj.get("includeVisual"),
            "visualOptions": VeeVisualOptionsDTO.from_dict(obj["visualOptions"]) if obj.get("visualOptions") is not None else None
        })
        return _obj


