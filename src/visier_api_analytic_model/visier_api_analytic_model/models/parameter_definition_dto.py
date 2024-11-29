# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

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
from visier_api_analytic_model.models.aggregation_type_parameter_dto import AggregationTypeParameterDTO
from visier_api_analytic_model.models.member_parameter_definition_dto import MemberParameterDefinitionDTO
from visier_api_analytic_model.models.numeric_parameter_definition_dto import NumericParameterDefinitionDTO
from visier_api_analytic_model.models.plan_parameter_definition_dto import PlanParameterDefinitionDTO
from typing import Optional, Set
from typing_extensions import Self

class ParameterDefinitionDTO(BaseModel):
    """
    Parameters generalize object definitions so that end users can provide values at query run time.
    """ # noqa: E501
    aggregation_type_parameter: Optional[AggregationTypeParameterDTO] = Field(default=None, description="An aggregation parameter. Such parameters enable control over how applicable metrics aggregate their results.", alias="aggregationTypeParameter")
    member_parameter: Optional[MemberParameterDefinitionDTO] = Field(default=None, description="A filter parameter that can be set with dimension members for the end user to select.", alias="memberParameter")
    numeric_parameter: Optional[NumericParameterDefinitionDTO] = Field(default=None, description="A parameter with a numeric data type. A numeric parameter can be set with an optional default value and value range.", alias="numericParameter")
    plan_parameter: Optional[PlanParameterDefinitionDTO] = Field(default=None, description="A parameter on a planning metric. Plan parameters resolve planning model metrics to a specific plan and scenario or snapshot.", alias="planParameter")
    __properties: ClassVar[List[str]] = ["aggregationTypeParameter", "memberParameter", "numericParameter", "planParameter"]

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
        """Create an instance of ParameterDefinitionDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aggregation_type_parameter
        if self.aggregation_type_parameter:
            _dict['aggregationTypeParameter'] = self.aggregation_type_parameter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of member_parameter
        if self.member_parameter:
            _dict['memberParameter'] = self.member_parameter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of numeric_parameter
        if self.numeric_parameter:
            _dict['numericParameter'] = self.numeric_parameter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plan_parameter
        if self.plan_parameter:
            _dict['planParameter'] = self.plan_parameter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ParameterDefinitionDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aggregationTypeParameter": AggregationTypeParameterDTO.from_dict(obj["aggregationTypeParameter"]) if obj.get("aggregationTypeParameter") is not None else None,
            "memberParameter": MemberParameterDefinitionDTO.from_dict(obj["memberParameter"]) if obj.get("memberParameter") is not None else None,
            "numericParameter": NumericParameterDefinitionDTO.from_dict(obj["numericParameter"]) if obj.get("numericParameter") is not None else None,
            "planParameter": PlanParameterDefinitionDTO.from_dict(obj["planParameter"]) if obj.get("planParameter") is not None else None
        })
        return _obj


