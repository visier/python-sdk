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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PlanParameterValueDTO(BaseModel):
    """
    The value for a parameter on a planning metric, including the parameter ID and the plan the parameter is based on.
    """ # noqa: E501
    parameter_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the plan parameter qualified by the object.", alias="parameterId")
    plan_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the plan the parameter is based on.", alias="planId")
    scenario_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the scenario the parameter is based on.", alias="scenarioId")
    snapshot_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the snapshot the parameter is based on.", alias="snapshotId")
    __properties: ClassVar[List[str]] = ["parameterId", "planId", "scenarioId", "snapshotId"]

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
        """Create an instance of PlanParameterValueDTO from a JSON string"""
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
        """Create an instance of PlanParameterValueDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "parameterId": obj.get("parameterId"),
            "planId": obj.get("planId"),
            "scenarioId": obj.get("scenarioId"),
            "snapshotId": obj.get("snapshotId")
        })
        return _obj


