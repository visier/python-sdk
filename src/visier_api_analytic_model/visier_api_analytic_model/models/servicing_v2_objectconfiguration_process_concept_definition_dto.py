# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_process_concept_metric_list_dto import ServicingV2ObjectconfigurationProcessConceptMetricListDTO
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_process_concept_outcome_list_dto import ServicingV2ObjectconfigurationProcessConceptOutcomeListDTO
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_process_concept_property_list_dto import ServicingV2ObjectconfigurationProcessConceptPropertyListDTO
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_process_concept_stage_list_dto import ServicingV2ObjectconfigurationProcessConceptStageListDTO
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_tag_reference_list_dto import ServicingV2ObjectconfigurationTagReferenceListDTO
from typing import Optional, Set
from typing_extensions import Self

class ServicingV2ObjectconfigurationProcessConceptDefinitionDTO(BaseModel):
    """
    The process concept's associated objects, such as its analytic object and status dimension.
    """ # noqa: E501
    analytic_object_name: Optional[StrictStr] = Field(default=None, description="The object name of the analytic object for the process concept.", alias="analyticObjectName")
    status_dimension_object_name: Optional[StrictStr] = Field(default=None, description="The object name of the status dimension for the process concept.", alias="statusDimensionObjectName")
    participation_concept_uuid: Optional[StrictStr] = Field(default=None, description="The UUID of the participation concept for the process concept.", alias="participationConceptUuid")
    on_hold_concept_uuid: Optional[StrictStr] = Field(default=None, description="The UUID of the on-hold concept for the process concept.", alias="onHoldConceptUuid")
    stage_list: Optional[ServicingV2ObjectconfigurationProcessConceptStageListDTO] = Field(default=None, description="The process concept's stages.", alias="stageList")
    outcome_list: Optional[ServicingV2ObjectconfigurationProcessConceptOutcomeListDTO] = Field(default=None, description="The process concept's outcomes.", alias="outcomeList")
    metric_list: Optional[ServicingV2ObjectconfigurationProcessConceptMetricListDTO] = Field(default=None, description="The process concept's associated metrics.", alias="metricList")
    property_list: Optional[ServicingV2ObjectconfigurationProcessConceptPropertyListDTO] = Field(default=None, description="The process concept's associated properties.", alias="propertyList")
    tag_list: Optional[ServicingV2ObjectconfigurationTagReferenceListDTO] = Field(default=None, description="The tags assigned to the object.", alias="tagList")
    visible_in_analytics: Optional[StrictBool] = Field(default=None, description="If `true`, the object is visible to end users in the solution.", alias="visibleInAnalytics")
    include_with_vee: Optional[StrictBool] = Field(default=None, description="If `true`, the object is available in Vee's responses.", alias="includeWithVee")
    __properties: ClassVar[List[str]] = ["analyticObjectName", "statusDimensionObjectName", "participationConceptUuid", "onHoldConceptUuid", "stageList", "outcomeList", "metricList", "propertyList", "tagList", "visibleInAnalytics", "includeWithVee"]

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
        """Create an instance of ServicingV2ObjectconfigurationProcessConceptDefinitionDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of stage_list
        if self.stage_list:
            _dict['stageList'] = self.stage_list.to_dict()
        # override the default output from pydantic by calling `to_dict()` of outcome_list
        if self.outcome_list:
            _dict['outcomeList'] = self.outcome_list.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metric_list
        if self.metric_list:
            _dict['metricList'] = self.metric_list.to_dict()
        # override the default output from pydantic by calling `to_dict()` of property_list
        if self.property_list:
            _dict['propertyList'] = self.property_list.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tag_list
        if self.tag_list:
            _dict['tagList'] = self.tag_list.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServicingV2ObjectconfigurationProcessConceptDefinitionDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "analyticObjectName": obj.get("analyticObjectName"),
            "statusDimensionObjectName": obj.get("statusDimensionObjectName"),
            "participationConceptUuid": obj.get("participationConceptUuid"),
            "onHoldConceptUuid": obj.get("onHoldConceptUuid"),
            "stageList": ServicingV2ObjectconfigurationProcessConceptStageListDTO.from_dict(obj["stageList"]) if obj.get("stageList") is not None else None,
            "outcomeList": ServicingV2ObjectconfigurationProcessConceptOutcomeListDTO.from_dict(obj["outcomeList"]) if obj.get("outcomeList") is not None else None,
            "metricList": ServicingV2ObjectconfigurationProcessConceptMetricListDTO.from_dict(obj["metricList"]) if obj.get("metricList") is not None else None,
            "propertyList": ServicingV2ObjectconfigurationProcessConceptPropertyListDTO.from_dict(obj["propertyList"]) if obj.get("propertyList") is not None else None,
            "tagList": ServicingV2ObjectconfigurationTagReferenceListDTO.from_dict(obj["tagList"]) if obj.get("tagList") is not None else None,
            "visibleInAnalytics": obj.get("visibleInAnalytics"),
            "includeWithVee": obj.get("includeWithVee")
        })
        return _obj


