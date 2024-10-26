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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class VeeClarificationDTO(BaseModel):
    """
    VeeClarificationDTO
    """ # noqa: E501
    attributes: Optional[List[StrictStr]] = Field(default=None, description="Suggested attributes to look at, that are similar or related to your question.")
    dimensions: Optional[List[StrictStr]] = Field(default=None, description="Suggested dimensions to look at, that are similar or related to your question.")
    filters: Optional[List[StrictStr]] = Field(default=None, description="Suggested filters that could be a better fit for the data.")
    message: Optional[StrictStr] = Field(default=None, description="Returned if Vee needs more context to answer your question.")
    metrics: Optional[List[StrictStr]] = Field(default=None, description="Suggested metrics to look at, that are similar or related to your question.")
    questions: Optional[List[StrictStr]] = Field(default=None, description="Some related questions that could be helpful.")
    __properties: ClassVar[List[str]] = ["attributes", "dimensions", "filters", "message", "metrics", "questions"]

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
        """Create an instance of VeeClarificationDTO from a JSON string"""
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
        """Create an instance of VeeClarificationDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attributes": obj.get("attributes"),
            "dimensions": obj.get("dimensions"),
            "filters": obj.get("filters"),
            "message": obj.get("message"),
            "metrics": obj.get("metrics"),
            "questions": obj.get("questions")
        })
        return _obj


