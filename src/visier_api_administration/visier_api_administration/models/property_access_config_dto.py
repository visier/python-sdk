# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PropertyAccessConfigDTO(BaseModel):
    """
    PropertyAccessConfigDTO
    """ # noqa: E501
    access_level: Optional[StrictStr] = Field(default=None, description="The access level of the property. Valid values are: `Aggregate`, `Detailed`.  * **Aggregate**: The property can only be accessed as part of an aggregate.  * **Detailed**: The property can be accessed at a detailed level.", alias="accessLevel")
    analytic_object_id: Optional[StrictStr] = Field(default=None, description="The analytic object ID of the property.", alias="analyticObjectId")
    analytic_object_reference_paths: Optional[List[StrictStr]] = Field(default=None, description="The path to the analytic object reference. Empty if the configuration is not a reference.", alias="analyticObjectReferencePaths")
    property_id: Optional[StrictStr] = Field(default=None, description="The property ID associated with the property access configuration.", alias="propertyId")
    property_status: Optional[StrictStr] = Field(default=None, description="The property's validity status. Valid values: `Valid`, `NoData`, `NotFound`.  * **Valid**: The object exists and has loaded data.  * **NoData**: The object exists but doesn't have loaded data.  * **NotFound**: The object doesn't exist.", alias="propertyStatus")
    __properties: ClassVar[List[str]] = ["accessLevel", "analyticObjectId", "analyticObjectReferencePaths", "propertyId", "propertyStatus"]

    @field_validator('access_level')
    def access_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['None', 'Aggregate', 'Detailed']):
            raise ValueError("must be one of enum values ('None', 'Aggregate', 'Detailed')")
        return value

    @field_validator('property_status')
    def property_status_validate_enum(cls, value):
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
        """Create an instance of PropertyAccessConfigDTO from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PropertyAccessConfigDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessLevel": obj.get("accessLevel"),
            "analyticObjectId": obj.get("analyticObjectId"),
            "analyticObjectReferencePaths": obj.get("analyticObjectReferencePaths"),
            "propertyId": obj.get("propertyId"),
            "propertyStatus": obj.get("propertyStatus")
        })
        return _obj


