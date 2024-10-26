# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_analytic_model.models.object_change_failure_dto import ObjectChangeFailureDTO
from visier_api_analytic_model.models.object_change_success_dto import ObjectChangeSuccessDTO
from typing import Optional, Set
from typing_extensions import Self

class ObjectsBulkChangeResponseDTO(BaseModel):
    """
    ObjectsBulkChangeResponseDTO
    """ # noqa: E501
    failures: Optional[List[ObjectChangeFailureDTO]] = Field(default=None, description="The objects that were not successfully changed.")
    successes: Optional[List[ObjectChangeSuccessDTO]] = Field(default=None, description="The objects that were successfully changed.")
    __properties: ClassVar[List[str]] = ["failures", "successes"]

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
        """Create an instance of ObjectsBulkChangeResponseDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in failures (list)
        _items = []
        if self.failures:
            for _item_failures in self.failures:
                if _item_failures:
                    _items.append(_item_failures.to_dict())
            _dict['failures'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in successes (list)
        _items = []
        if self.successes:
            for _item_successes in self.successes:
                if _item_successes:
                    _items.append(_item_successes.to_dict())
            _dict['successes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectsBulkChangeResponseDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "failures": [ObjectChangeFailureDTO.from_dict(_item) for _item in obj["failures"]] if obj.get("failures") is not None else None,
            "successes": [ObjectChangeSuccessDTO.from_dict(_item) for _item in obj["successes"]] if obj.get("successes") is not None else None
        })
        return _obj


