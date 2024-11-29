# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_administration.models.custom_tenant_property_dto import CustomTenantPropertyDTO
from visier_api_administration.models.tenant_module_dto import TenantModuleDTO
from typing import Optional, Set
from typing_extensions import Self

class TenantDetailAPIDTO(BaseModel):
    """
    TenantDetailAPIDTO
    """ # noqa: E501
    can_administer_other_tenants: Optional[StrictBool] = Field(default=None, description="If true, the tenant is an administrating tenant.", alias="canAdministerOtherTenants")
    current_data_version: Optional[StrictStr] = Field(default=None, description="The data version ID that the tenant is using.", alias="currentDataVersion")
    custom_properties: Optional[List[CustomTenantPropertyDTO]] = Field(default=None, description="A set of key-value pairs that represent different customizable properties for the analytic tenant.", alias="customProperties")
    data_version_date: Optional[StrictStr] = Field(default=None, description="The date that the data version was published to production.", alias="dataVersionDate")
    embeddable_domains: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated list of strings that represent the URLs, or domains, in which Visier can be embedded.", alias="embeddableDomains")
    industry_code: Optional[StrictInt] = Field(default=None, description="The 6-digit NAICS code for the industry to which the analytic tenant belongs.", alias="industryCode")
    modules: Optional[List[TenantModuleDTO]] = Field(default=None, description="The modules assigned to the analytic tenant.")
    provision_date: Optional[StrictStr] = Field(default=None, description="The date that the tenant was created.", alias="provisionDate")
    sso_instance_issuers: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated list of strings that represent the issuers for the SSO providers that can authenticate this tenant.", alias="ssoInstanceIssuers")
    status: Optional[StrictStr] = Field(default=None, description="Whether the tenant is enabled or disabled.")
    tenant_code: Optional[StrictStr] = Field(default=None, description="The tenant code of the analytic tenant. For example, \"WFF_j1r~i1o\".", alias="tenantCode")
    tenant_display_name: Optional[StrictStr] = Field(default=None, description="An identifiable tenant name that is displayed within Visier. For example, \"Callisto\".", alias="tenantDisplayName")
    vanity_url_name: Optional[StrictStr] = Field(default=None, description="The name of the administrating tenant used in Visier URLs.", alias="vanityUrlName")
    __properties: ClassVar[List[str]] = ["canAdministerOtherTenants", "currentDataVersion", "customProperties", "dataVersionDate", "embeddableDomains", "industryCode", "modules", "provisionDate", "ssoInstanceIssuers", "status", "tenantCode", "tenantDisplayName", "vanityUrlName"]

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
        """Create an instance of TenantDetailAPIDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in custom_properties (list)
        _items = []
        if self.custom_properties:
            for _item_custom_properties in self.custom_properties:
                if _item_custom_properties:
                    _items.append(_item_custom_properties.to_dict())
            _dict['customProperties'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in modules (list)
        _items = []
        if self.modules:
            for _item_modules in self.modules:
                if _item_modules:
                    _items.append(_item_modules.to_dict())
            _dict['modules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantDetailAPIDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "canAdministerOtherTenants": obj.get("canAdministerOtherTenants"),
            "currentDataVersion": obj.get("currentDataVersion"),
            "customProperties": [CustomTenantPropertyDTO.from_dict(_item) for _item in obj["customProperties"]] if obj.get("customProperties") is not None else None,
            "dataVersionDate": obj.get("dataVersionDate"),
            "embeddableDomains": obj.get("embeddableDomains"),
            "industryCode": obj.get("industryCode"),
            "modules": [TenantModuleDTO.from_dict(_item) for _item in obj["modules"]] if obj.get("modules") is not None else None,
            "provisionDate": obj.get("provisionDate"),
            "ssoInstanceIssuers": obj.get("ssoInstanceIssuers"),
            "status": obj.get("status"),
            "tenantCode": obj.get("tenantCode"),
            "tenantDisplayName": obj.get("tenantDisplayName"),
            "vanityUrlName": obj.get("vanityUrlName")
        })
        return _obj


