# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1892
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
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_process_concept_definition_dto import ServicingV2ObjectconfigurationProcessConceptDefinitionDTO
from typing import Optional, Set
from typing_extensions import Self

class ServicingV2ObjectconfigurationConceptTypeDetailsDTO(BaseModel):
    """
    ServicingV2ObjectconfigurationConceptTypeDetailsDTO
    """ # noqa: E501
    process: Optional[ServicingV2ObjectconfigurationProcessConceptDefinitionDTO] = Field(default=None, description="The process concept's associated objects, such as its analytic object and status dimension.")
    __properties: ClassVar[List[str]] = ["process"]

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
        """Create an instance of ServicingV2ObjectconfigurationConceptTypeDetailsDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of process
        if self.process:
            _dict['process'] = self.process.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServicingV2ObjectconfigurationConceptTypeDetailsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "process": ServicingV2ObjectconfigurationProcessConceptDefinitionDTO.from_dict(obj["process"]) if obj.get("process") is not None else None
        })
        return _obj


