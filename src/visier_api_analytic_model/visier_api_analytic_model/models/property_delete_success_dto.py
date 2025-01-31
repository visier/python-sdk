# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1701
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
from visier_api_analytic_model.models.dependent_dto import DependentDTO
from typing import Optional, Set
from typing_extensions import Self

class PropertyDeleteSuccessDTO(BaseModel):
    """
    Details about a successful property deletion.
    """ # noqa: E501
    derived_dependents_deleted: Optional[List[DependentDTO]] = Field(default=None, description="The derived dependents that were deleted along with the property.", alias="derivedDependentsDeleted")
    display_name: Optional[StrictStr] = Field(default=None, description="The display name of the property.", alias="displayName")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the property.")
    project_id: Optional[StrictStr] = Field(default=None, description="The project in which the property was deleted.", alias="projectId")
    reference_dependents_ignored: Optional[List[DependentDTO]] = Field(default=None, description="Dependents that reference the property and were ignored during deletion.", alias="referenceDependentsIgnored")
    tenant_code: Optional[StrictStr] = Field(default=None, description="The tenant in which the property was deleted.", alias="tenantCode")
    __properties: ClassVar[List[str]] = ["derivedDependentsDeleted", "displayName", "id", "projectId", "referenceDependentsIgnored", "tenantCode"]

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
        """Create an instance of PropertyDeleteSuccessDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in derived_dependents_deleted (list)
        _items = []
        if self.derived_dependents_deleted:
            for _item_derived_dependents_deleted in self.derived_dependents_deleted:
                if _item_derived_dependents_deleted:
                    _items.append(_item_derived_dependents_deleted.to_dict())
            _dict['derivedDependentsDeleted'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reference_dependents_ignored (list)
        _items = []
        if self.reference_dependents_ignored:
            for _item_reference_dependents_ignored in self.reference_dependents_ignored:
                if _item_reference_dependents_ignored:
                    _items.append(_item_reference_dependents_ignored.to_dict())
            _dict['referenceDependentsIgnored'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PropertyDeleteSuccessDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "derivedDependentsDeleted": [DependentDTO.from_dict(_item) for _item in obj["derivedDependentsDeleted"]] if obj.get("derivedDependentsDeleted") is not None else None,
            "displayName": obj.get("displayName"),
            "id": obj.get("id"),
            "projectId": obj.get("projectId"),
            "referenceDependentsIgnored": [DependentDTO.from_dict(_item) for _item in obj["referenceDependentsIgnored"]] if obj.get("referenceDependentsIgnored") is not None else None,
            "tenantCode": obj.get("tenantCode")
        })
        return _obj


