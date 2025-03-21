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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_administration.models.admin_publicapi_transfers_custom_tenant_property_dto import AdminPublicapiTransfersCustomTenantPropertyDTO
from typing import Optional, Set
from typing_extensions import Self

class AdminPublicapiTransfersTenantProvisionAPIDTO(BaseModel):
    """
    AdminPublicapiTransfersTenantProvisionAPIDTO
    """ # noqa: E501
    allowed_o_auth_idp_url_domains: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated list of strings that represent the URLs, or domains, which can be used as values for the idp_url  OAuth parameter.", alias="allowedOAuthIdpUrlDomains")
    custom_properties: Optional[List[AdminPublicapiTransfersCustomTenantPropertyDTO]] = Field(default=None, description="A set of key-value pairs that represent different customizable properties for the analytic tenant.", alias="customProperties")
    embeddable_domains: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated list of strings that represent the URLs, or domains, in which Visier can be embedded. If  domains at the administrating tenant level match the domains at the analytic tenant level, you do not need  to include a domain for each analytic tenant.", alias="embeddableDomains")
    industry_code: Optional[StrictInt] = Field(default=None, description="The 6-digit NAICS code for the industry to which the analytic tenant belongs. If the code is unknown, type 0.   For 2-digit codes, add trailing zeros at the end to reach 6 digits, such as 620000.", alias="industryCode")
    purchased_modules: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated list of strings that represent the Visier modules assigned to the analytic tenant.", alias="purchasedModules")
    sso_instance_issuers: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated list of strings that represent the issuers for the SSO providers that can authenticate this tenant.", alias="ssoInstanceIssuers")
    tenant_code: Optional[StrictStr] = Field(default=None, description="The unique identifier of the analytic tenant.", alias="tenantCode")
    tenant_display_name: Optional[StrictStr] = Field(default=None, description="The display name that is assigned to the analytic tenant.", alias="tenantDisplayName")
    __properties: ClassVar[List[str]] = ["allowedOAuthIdpUrlDomains", "customProperties", "embeddableDomains", "industryCode", "purchasedModules", "ssoInstanceIssuers", "tenantCode", "tenantDisplayName"]

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
        """Create an instance of AdminPublicapiTransfersTenantProvisionAPIDTO from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdminPublicapiTransfersTenantProvisionAPIDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowedOAuthIdpUrlDomains": obj.get("allowedOAuthIdpUrlDomains"),
            "customProperties": [AdminPublicapiTransfersCustomTenantPropertyDTO.from_dict(_item) for _item in obj["customProperties"]] if obj.get("customProperties") is not None else None,
            "embeddableDomains": obj.get("embeddableDomains"),
            "industryCode": obj.get("industryCode"),
            "purchasedModules": obj.get("purchasedModules"),
            "ssoInstanceIssuers": obj.get("ssoInstanceIssuers"),
            "tenantCode": obj.get("tenantCode"),
            "tenantDisplayName": obj.get("tenantDisplayName")
        })
        return _obj


