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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_analytic_model.models.perspective_node_dto import PerspectiveNodeDTO
from typing import Optional, Set
from typing_extensions import Self

class PerspectiveConfigurationDTO(BaseModel):
    """
    PerspectiveConfigurationDTO
    """ # noqa: E501
    perspective_id: Optional[StrictStr] = Field(default=None, description="The UUID of the perspective.", alias="perspectiveId")
    perspective_name: Optional[StrictStr] = Field(default=None, description="The display name of the perspective.", alias="perspectiveName")
    perspective_nodes: Optional[List[PerspectiveNodeDTO]] = Field(default=None, description="A list of nodes in the perspective.", alias="perspectiveNodes")
    __properties: ClassVar[List[str]] = ["perspectiveId", "perspectiveName", "perspectiveNodes"]

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
        """Create an instance of PerspectiveConfigurationDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in perspective_nodes (list)
        _items = []
        if self.perspective_nodes:
            for _item_perspective_nodes in self.perspective_nodes:
                if _item_perspective_nodes:
                    _items.append(_item_perspective_nodes.to_dict())
            _dict['perspectiveNodes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PerspectiveConfigurationDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "perspectiveId": obj.get("perspectiveId"),
            "perspectiveName": obj.get("perspectiveName"),
            "perspectiveNodes": [PerspectiveNodeDTO.from_dict(_item) for _item in obj["perspectiveNodes"]] if obj.get("perspectiveNodes") is not None else None
        })
        return _obj


