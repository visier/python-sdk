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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_administration.models.inherited_access_config_dto import InheritedAccessConfigDTO
from visier_api_administration.models.inherited_reference_member_filter_config_dto import InheritedReferenceMemberFilterConfigDTO
from visier_api_administration.models.member_filter_config_dto import MemberFilterConfigDTO
from visier_api_administration.models.property_set_config_dto import PropertySetConfigDTO
from typing import Optional, Set
from typing_extensions import Self

class DataSecurityProfileDTO(BaseModel):
    """
    DataSecurityProfileDTO
    """ # noqa: E501
    all_data_point_access: Optional[StrictBool] = Field(default=None, description="If `true`, the permission grants access to the entire population. If `false`, define `memberFilterConfigs` to set custom population access.", alias="allDataPointAccess")
    analytic_object_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the analytic object assigned data security in this permission.", alias="analyticObjectId")
    analytic_object_status: Optional[StrictStr] = Field(default=None, description="The analytic object's validity status. Valid values: Valid, NoData, NotFound.  * **Valid**: The object exists and has loaded data.  * **NoData**: The object exists but doesn't have loaded data.  * **NotFound**: The object doesn't exist.", alias="analyticObjectStatus")
    inherited_access_configs: Optional[List[InheritedAccessConfigDTO]] = Field(default=None, description="The events and related objects inherited from the analytic object.  By default, all events and related objects associated with the analytic object will be inherited from the analytic object in a permission.  For example, if you assign access to Employee, then access to the Employee Exit event is inherited in the permission.  To remove access to an event or related object, add the object to `inheritedAccessConfigs` with `removeAccess`: true.  To add custom filters to an event or related object, add the object to `inheritedAccessConfigs` and define `memberFilterConfigs`.", alias="inheritedAccessConfigs")
    inherited_reference_member_filter_config: Optional[InheritedReferenceMemberFilterConfigDTO] = Field(default=None, description="Configures the analytic object to inherit population access filters from. The target analytic object must be assigned population access in the permission and have a binding (strong) reference from the source analytic object.  * For example, assume `Applicant` -> `Requisition` is configured to be a binding (strong) reference.  For `Applicant` (source analytic object) to inherit population access filters from `Requisition` (target analytic object), in the Applicant `dataSecurityProfile`, set `inheritedReferenceMemberFilterConfig` to `Requisition`. In this example, Applicant will inherit filters from Requisition because Requsition is assigned data security in this permission and there is a binding (strong) reference from Applicant to Requisition.", alias="inheritedReferenceMemberFilterConfig")
    member_filter_configs: Optional[List[MemberFilterConfigDTO]] = Field(default=None, description="Custom filters that define population access for an item in the permission.", alias="memberFilterConfigs")
    property_set_config: Optional[PropertySetConfigDTO] = Field(default=None, description="A list of objects representing the data access for an analytic object’s properties.", alias="propertySetConfig")
    __properties: ClassVar[List[str]] = ["allDataPointAccess", "analyticObjectId", "analyticObjectStatus", "inheritedAccessConfigs", "inheritedReferenceMemberFilterConfig", "memberFilterConfigs", "propertySetConfig"]

    @field_validator('analytic_object_status')
    def analytic_object_status_validate_enum(cls, value):
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
        """Create an instance of DataSecurityProfileDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in inherited_access_configs (list)
        _items = []
        if self.inherited_access_configs:
            for _item_inherited_access_configs in self.inherited_access_configs:
                if _item_inherited_access_configs:
                    _items.append(_item_inherited_access_configs.to_dict())
            _dict['inheritedAccessConfigs'] = _items
        # override the default output from pydantic by calling `to_dict()` of inherited_reference_member_filter_config
        if self.inherited_reference_member_filter_config:
            _dict['inheritedReferenceMemberFilterConfig'] = self.inherited_reference_member_filter_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in member_filter_configs (list)
        _items = []
        if self.member_filter_configs:
            for _item_member_filter_configs in self.member_filter_configs:
                if _item_member_filter_configs:
                    _items.append(_item_member_filter_configs.to_dict())
            _dict['memberFilterConfigs'] = _items
        # override the default output from pydantic by calling `to_dict()` of property_set_config
        if self.property_set_config:
            _dict['propertySetConfig'] = self.property_set_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataSecurityProfileDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allDataPointAccess": obj.get("allDataPointAccess"),
            "analyticObjectId": obj.get("analyticObjectId"),
            "analyticObjectStatus": obj.get("analyticObjectStatus"),
            "inheritedAccessConfigs": [InheritedAccessConfigDTO.from_dict(_item) for _item in obj["inheritedAccessConfigs"]] if obj.get("inheritedAccessConfigs") is not None else None,
            "inheritedReferenceMemberFilterConfig": InheritedReferenceMemberFilterConfigDTO.from_dict(obj["inheritedReferenceMemberFilterConfig"]) if obj.get("inheritedReferenceMemberFilterConfig") is not None else None,
            "memberFilterConfigs": [MemberFilterConfigDTO.from_dict(_item) for _item in obj["memberFilterConfigs"]] if obj.get("memberFilterConfigs") is not None else None,
            "propertySetConfig": PropertySetConfigDTO.from_dict(obj["propertySetConfig"]) if obj.get("propertySetConfig") is not None else None
        })
        return _obj


