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
from visier_api_administration.models.servicing_publicapi_transfers_user_property_dto import ServicingPublicapiTransfersUserPropertyDTO
from typing import Optional, Set
from typing_extensions import Self

class ServicingPublicapiTransfersDynamicPropertyMappingDTO(BaseModel):
    """
    ServicingPublicapiTransfersDynamicPropertyMappingDTO
    """ # noqa: E501
    hierarchy_property_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the property.", alias="hierarchyPropertyId")
    hierarchy_property_status: Optional[StrictStr] = Field(default=None, description="The property's validity status. Valid values: `Valid`, `NotFound`.  * **Valid**: The object exists and has loaded data.  * **NotFound**: The object doesn't exist.", alias="hierarchyPropertyStatus")
    user_property: Optional[ServicingPublicapiTransfersUserPropertyDTO] = Field(default=None, description="The user property that you want to link the name property or organization head to.", alias="userProperty")
    __properties: ClassVar[List[str]] = ["hierarchyPropertyId", "hierarchyPropertyStatus", "userProperty"]

    @field_validator('hierarchy_property_status')
    def hierarchy_property_status_validate_enum(cls, value):
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
        """Create an instance of ServicingPublicapiTransfersDynamicPropertyMappingDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user_property
        if self.user_property:
            _dict['userProperty'] = self.user_property.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServicingPublicapiTransfersDynamicPropertyMappingDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hierarchyPropertyId": obj.get("hierarchyPropertyId"),
            "hierarchyPropertyStatus": obj.get("hierarchyPropertyStatus"),
            "userProperty": ServicingPublicapiTransfersUserPropertyDTO.from_dict(obj["userProperty"]) if obj.get("userProperty") is not None else None
        })
        return _obj


