# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1876
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
from visier_api_analytic_model.models.servicing_objectconfiguration_dependent_dto import ServicingObjectconfigurationDependentDTO
from typing import Optional, Set
from typing_extensions import Self

class ServicingObjectconfigurationPropertyDeleteFailureDTO(BaseModel):
    """
    Details about a failed property deletion.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the property.")
    display_name: Optional[StrictStr] = Field(default=None, description="The display name of the property.", alias="displayName")
    message: Optional[StrictStr] = Field(default=None, description="An error message describing the cause of the failure.")
    rci: Optional[StrictStr] = Field(default=None, description="The root cause identifier to provide to Visier Technical Support if you require further troubleshooting.")
    tenant_code: Optional[StrictStr] = Field(default=None, description="The tenant in which the property wasn't deleted.", alias="tenantCode")
    project_id: Optional[StrictStr] = Field(default=None, description="The project in which the property wasn't deleted.", alias="projectId")
    derived_dependents_to_delete: Optional[List[ServicingObjectconfigurationDependentDTO]] = Field(default=None, description="The derived dependents that would have been deleted if the deletion was successful.", alias="derivedDependentsToDelete")
    reference_dependents_to_ignore: Optional[List[ServicingObjectconfigurationDependentDTO]] = Field(default=None, description="Dependents that reference this property and could be affected.", alias="referenceDependentsToIgnore")
    __properties: ClassVar[List[str]] = ["id", "displayName", "message", "rci", "tenantCode", "projectId", "derivedDependentsToDelete", "referenceDependentsToIgnore"]

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
        """Create an instance of ServicingObjectconfigurationPropertyDeleteFailureDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in derived_dependents_to_delete (list)
        _items = []
        if self.derived_dependents_to_delete:
            for _item_derived_dependents_to_delete in self.derived_dependents_to_delete:
                if _item_derived_dependents_to_delete:
                    _items.append(_item_derived_dependents_to_delete.to_dict())
            _dict['derivedDependentsToDelete'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reference_dependents_to_ignore (list)
        _items = []
        if self.reference_dependents_to_ignore:
            for _item_reference_dependents_to_ignore in self.reference_dependents_to_ignore:
                if _item_reference_dependents_to_ignore:
                    _items.append(_item_reference_dependents_to_ignore.to_dict())
            _dict['referenceDependentsToIgnore'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServicingObjectconfigurationPropertyDeleteFailureDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "displayName": obj.get("displayName"),
            "message": obj.get("message"),
            "rci": obj.get("rci"),
            "tenantCode": obj.get("tenantCode"),
            "projectId": obj.get("projectId"),
            "derivedDependentsToDelete": [ServicingObjectconfigurationDependentDTO.from_dict(_item) for _item in obj["derivedDependentsToDelete"]] if obj.get("derivedDependentsToDelete") is not None else None,
            "referenceDependentsToIgnore": [ServicingObjectconfigurationDependentDTO.from_dict(_item) for _item in obj["referenceDependentsToIgnore"]] if obj.get("referenceDependentsToIgnore") is not None else None
        })
        return _obj


