# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_administration.models.servicing_publicapi_transfers_dynamic_property_mapping_dto import ServicingPublicapiTransfersDynamicPropertyMappingDTO
from typing import Optional, Set
from typing_extensions import Self

class ServicingPublicapiTransfersDynamicDimensionFilterDTO(BaseModel):
    """
    ServicingPublicapiTransfersDynamicDimensionFilterDTO
    """ # noqa: E501
    dimension_id: Optional[StrictStr] = Field(default=None, description="The dimension ID associated with the filter.", alias="dimensionId")
    dimension_status: Optional[StrictStr] = Field(default=None, description="The dimension's validity status. Valid values: Valid, NoData, NotFound.  * **Valid**: The object exists and has loaded data.  * **NoData**: The object exists but doesn't have loaded data.  * **NotFound**: The object doesn't exist.", alias="dimensionStatus")
    dynamic_property_mappings: Optional[List[ServicingPublicapiTransfersDynamicPropertyMappingDTO]] = Field(default=None, description="The properties assigned population access in the dynamic filter.", alias="dynamicPropertyMappings")
    subject_reference_path: Optional[List[StrictStr]] = Field(default=None, description="The subject reference path.", alias="subjectReferencePath")
    __properties: ClassVar[List[str]] = ["dimensionId", "dimensionStatus", "dynamicPropertyMappings", "subjectReferencePath"]

    @field_validator('dimension_status')
    def dimension_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Unset', 'Valid', 'NoData', 'NotFound']):
            raise ValueError("must be one of enum values ('Unset', 'Valid', 'NoData', 'NotFound')")
        return value

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
        """Create an instance of ServicingPublicapiTransfersDynamicDimensionFilterDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in dynamic_property_mappings (list)
        _items = []
        if self.dynamic_property_mappings:
            for _item_dynamic_property_mappings in self.dynamic_property_mappings:
                if _item_dynamic_property_mappings:
                    _items.append(_item_dynamic_property_mappings.to_dict())
            _dict['dynamicPropertyMappings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServicingPublicapiTransfersDynamicDimensionFilterDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dimensionId": obj.get("dimensionId"),
            "dimensionStatus": obj.get("dimensionStatus"),
            "dynamicPropertyMappings": [ServicingPublicapiTransfersDynamicPropertyMappingDTO.from_dict(_item) for _item in obj["dynamicPropertyMappings"]] if obj.get("dynamicPropertyMappings") is not None else None,
            "subjectReferencePath": obj.get("subjectReferencePath")
        })
        return _obj


