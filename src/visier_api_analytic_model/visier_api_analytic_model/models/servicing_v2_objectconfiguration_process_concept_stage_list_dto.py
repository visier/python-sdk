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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_process_concept_stage_dto import ServicingV2ObjectconfigurationProcessConceptStageDTO
from typing import Optional, Set
from typing_extensions import Self

class ServicingV2ObjectconfigurationProcessConceptStageListDTO(BaseModel):
    """
    The process concept's stages.
    """ # noqa: E501
    stages: Optional[List[ServicingV2ObjectconfigurationProcessConceptStageDTO]] = Field(default=None, description="Each stage in the process concept.")
    __properties: ClassVar[List[str]] = ["stages"]

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
        """Create an instance of ServicingV2ObjectconfigurationProcessConceptStageListDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in stages (list)
        _items = []
        if self.stages:
            for _item_stages in self.stages:
                if _item_stages:
                    _items.append(_item_stages.to_dict())
            _dict['stages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServicingV2ObjectconfigurationProcessConceptStageListDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "stages": [ServicingV2ObjectconfigurationProcessConceptStageDTO.from_dict(_item) for _item in obj["stages"]] if obj.get("stages") is not None else None
        })
        return _obj


