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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_analytic_model.models.dimension_change_definition_dto import DimensionChangeDefinitionDTO
from typing import Optional, Set
from typing_extensions import Self

class DimensionChangeDefinitionsByTenantDTO(BaseModel):
    """
    DimensionChangeDefinitionsByTenantDTO
    """ # noqa: E501
    dimensions: Optional[List[DimensionChangeDefinitionDTO]] = Field(default=None, description="The list of dimensions to update.")
    project_id: Optional[StrictStr] = Field(default=None, description="To make changes in a project, specify a project ID.", alias="projectId")
    tenant_code: Optional[StrictStr] = Field(default=None, description="The tenant code of the tenant in which to update dimensions.", alias="tenantCode")
    __properties: ClassVar[List[str]] = ["dimensions", "projectId", "tenantCode"]

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
        """Create an instance of DimensionChangeDefinitionsByTenantDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in dimensions (list)
        _items = []
        if self.dimensions:
            for _item_dimensions in self.dimensions:
                if _item_dimensions:
                    _items.append(_item_dimensions.to_dict())
            _dict['dimensions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DimensionChangeDefinitionsByTenantDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dimensions": [DimensionChangeDefinitionDTO.from_dict(_item) for _item in obj["dimensions"]] if obj.get("dimensions") is not None else None,
            "projectId": obj.get("projectId"),
            "tenantCode": obj.get("tenantCode")
        })
        return _obj


