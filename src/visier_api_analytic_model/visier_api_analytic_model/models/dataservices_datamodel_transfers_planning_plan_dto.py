# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1793
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
from visier_api_analytic_model.models.dataservices_datamodel_transfers_planning_plan_context_dto import DataservicesDatamodelTransfersPlanningPlanContextDTO
from visier_api_analytic_model.models.dataservices_datamodel_transfers_scenario_or_snapshot_dto import DataservicesDatamodelTransfersScenarioOrSnapshotDTO
from typing import Optional, Set
from typing_extensions import Self

class DataservicesDatamodelTransfersPlanningPlanDTO(BaseModel):
    """
    The definition of a plan. Plans are defined on planning models, and each plan may define multiple scenarios or snapshots.
    """ # noqa: E501
    default_contexts: Optional[List[DataservicesDatamodelTransfersPlanningPlanContextDTO]] = Field(default=None, description="The contexts defined for the plan.", alias="defaultContexts")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the plan.  Note: See `PlanningPlans` to get the ID.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the plan.")
    plan_dimension_ids: Optional[List[StrictStr]] = Field(default=None, description="The IDs of the dimensions defined for the plan.", alias="planDimensionIds")
    scenarios: Optional[List[DataservicesDatamodelTransfersScenarioOrSnapshotDTO]] = Field(default=None, description="The available scenarios for the plan.")
    snapshots: Optional[List[DataservicesDatamodelTransfersScenarioOrSnapshotDTO]] = Field(default=None, description="The available snapshots for the plan.")
    subject_id: Optional[StrictStr] = Field(default=None, description="The ID of subject for the plan.", alias="subjectId")
    __properties: ClassVar[List[str]] = ["defaultContexts", "id", "name", "planDimensionIds", "scenarios", "snapshots", "subjectId"]

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
        """Create an instance of DataservicesDatamodelTransfersPlanningPlanDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in default_contexts (list)
        _items = []
        if self.default_contexts:
            for _item_default_contexts in self.default_contexts:
                if _item_default_contexts:
                    _items.append(_item_default_contexts.to_dict())
            _dict['defaultContexts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in scenarios (list)
        _items = []
        if self.scenarios:
            for _item_scenarios in self.scenarios:
                if _item_scenarios:
                    _items.append(_item_scenarios.to_dict())
            _dict['scenarios'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in snapshots (list)
        _items = []
        if self.snapshots:
            for _item_snapshots in self.snapshots:
                if _item_snapshots:
                    _items.append(_item_snapshots.to_dict())
            _dict['snapshots'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataservicesDatamodelTransfersPlanningPlanDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "defaultContexts": [DataservicesDatamodelTransfersPlanningPlanContextDTO.from_dict(_item) for _item in obj["defaultContexts"]] if obj.get("defaultContexts") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "planDimensionIds": obj.get("planDimensionIds"),
            "scenarios": [DataservicesDatamodelTransfersScenarioOrSnapshotDTO.from_dict(_item) for _item in obj["scenarios"]] if obj.get("scenarios") is not None else None,
            "snapshots": [DataservicesDatamodelTransfersScenarioOrSnapshotDTO.from_dict(_item) for _item in obj["snapshots"]] if obj.get("snapshots") is not None else None,
            "subjectId": obj.get("subjectId")
        })
        return _obj


