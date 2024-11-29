# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1614
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
from visier_api_data_out.models.aggregation_type_parameter_value_dto import AggregationTypeParameterValueDTO
from visier_api_data_out.models.member_parameter_value_dto import MemberParameterValueDTO
from visier_api_data_out.models.numeric_parameter_value_dto import NumericParameterValueDTO
from visier_api_data_out.models.plan_parameter_value_dto import PlanParameterValueDTO
from typing import Optional, Set
from typing_extensions import Self

class QueryParameterValueDTO(BaseModel):
    """
    An object that contains parameter values for either member or numeric parameters.
    """ # noqa: E501
    aggregation_type_value: Optional[AggregationTypeParameterValueDTO] = Field(default=None, description="A value for an aggregation parameter.", alias="aggregationTypeValue")
    member_value: Optional[MemberParameterValueDTO] = Field(default=None, description="A value for a member parameter.", alias="memberValue")
    numeric_value: Optional[NumericParameterValueDTO] = Field(default=None, description="A value for a numeric parameter.", alias="numericValue")
    plan_value: Optional[PlanParameterValueDTO] = Field(default=None, description="A value for a plan parameter.", alias="planValue")
    __properties: ClassVar[List[str]] = ["aggregationTypeValue", "memberValue", "numericValue", "planValue"]

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
        """Create an instance of QueryParameterValueDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aggregation_type_value
        if self.aggregation_type_value:
            _dict['aggregationTypeValue'] = self.aggregation_type_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of member_value
        if self.member_value:
            _dict['memberValue'] = self.member_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of numeric_value
        if self.numeric_value:
            _dict['numericValue'] = self.numeric_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plan_value
        if self.plan_value:
            _dict['planValue'] = self.plan_value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QueryParameterValueDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aggregationTypeValue": AggregationTypeParameterValueDTO.from_dict(obj["aggregationTypeValue"]) if obj.get("aggregationTypeValue") is not None else None,
            "memberValue": MemberParameterValueDTO.from_dict(obj["memberValue"]) if obj.get("memberValue") is not None else None,
            "numericValue": NumericParameterValueDTO.from_dict(obj["numericValue"]) if obj.get("numericValue") is not None else None,
            "planValue": PlanParameterValueDTO.from_dict(obj["planValue"]) if obj.get("planValue") is not None else None
        })
        return _obj


