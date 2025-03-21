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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_administration.models.admin_publicapi_transfers_business_location_dto import AdminPublicapiTransfersBusinessLocationDTO
from visier_api_administration.models.admin_publicapi_transfers_custom_property_dto import AdminPublicapiTransfersCustomPropertyDTO
from visier_api_administration.models.admin_publicapi_transfers_home_analysis_by_user_group_dto import AdminPublicapiTransfersHomeAnalysisByUserGroupDTO
from typing import Optional, Set
from typing_extensions import Self

class AdminPublicapiTransfersTenantManagementAPIUpdateRequestDTO(BaseModel):
    """
    AdminPublicapiTransfersTenantManagementAPIUpdateRequestDTO
    """ # noqa: E501
    allowed_o_auth_idp_url_domains: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated list of strings that represent the URLs, or domains, that are allowed in the idp_url OAuth parameter. This is optional.", alias="allowedOAuthIdpUrlDomains")
    click_through_link: Optional[StrictStr] = Field(default=None, description="A custom URL to redirect users into your portal to see the relevant content. This URL is used for links that are shared by and with your users through the sharing capability or email content. This is optional. Causes the API request to take longer because it must publish a project to production.", alias="clickThroughLink")
    custom_properties: Optional[List[AdminPublicapiTransfersCustomPropertyDTO]] = Field(default=None, description="A list of objects that represent different customizable properties for the analytic tenant. This is optional.", alias="customProperties")
    default_currency: Optional[StrictStr] = Field(default=None, description="The default currency to show in the application for the tenant.", alias="defaultCurrency")
    embeddable_domains: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated list of strings that represent the URLs, or domains, in which Visier can be embedded. If domains at the administrating tenant level match the domains at the analytic tenant level, you do not need to include a domain for each analytic tenant. This is optional.", alias="embeddableDomains")
    enabled: Optional[StrictBool] = Field(default=None, description="If true, the tenant is enabled. Enabled tenants have access to Visier visualizations.")
    home_analysis_by_user_group: Optional[List[AdminPublicapiTransfersHomeAnalysisByUserGroupDTO]] = Field(default=None, description="A list of objects representing the analysis to display to specific user groups when users log in. This is optional. Causes the API request to take longer because it must publish a project to production.", alias="homeAnalysisByUserGroup")
    home_analysis_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the analysis to display for this tenant when a user logs in. This is optional. Causes the API request to take longer because it must publish a project to production.   Retrieve the ID by opening an analysis in the production version of a tenant and copying the string after the last forward slash (/) in the URL. For example: https://jupiter.visier.com/hr/prod/appcontainer?previewId=-eZPm8xvo3SUMpD4Q5pdE-6mCj9CQ9K699XgqRGwtOxagH5x2IzDFawlWn3hYqFEfU7nP0YK9ASEzmrNfAihGg..&previewType=Production#/analytics/myanalyses/`8a4c1d4f-eb61-4da0-9e5b-55bef757c30e`.   The `homeAnalysisID` is `8a4c1d4f-eb61-4da0-9e5b-55bef757c30e`. Alternatively, retrieve the ID by copying the `Analysis ID` or `contentId` found by following the `Embed a Visualization` documentation.", alias="homeAnalysisId")
    industry_code: Optional[StrictInt] = Field(default=None, description="The 6-digit NAICS code for the industry to which the analytic tenant belongs. If the code is unknown, type 0.   For 2-digit codes, add trailing zeros at the end to reach 6 digits, such as 620000. Required if creating new tenants.", alias="industryCode")
    primary_business_location: Optional[AdminPublicapiTransfersBusinessLocationDTO] = Field(default=None, description="The primary location of operations or where business is performed. This field is optional.", alias="primaryBusinessLocation")
    purchased_modules: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated collection of strings that represent the Visier modules assigned to the new analytic tenant. Required if creating new tenants.   To get the module name:  1. In Visier, open a project and navigate to **Model > Modules**.  2. Select a module.  3. In **Basic Information**, copy the **Object name**. This is the module name.", alias="purchasedModules")
    sso_instance_issuers: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated list of strings that represent the issuers for the SSO providers that can authenticate this tenant. This is optional.", alias="ssoInstanceIssuers")
    tenant_code: Optional[StrictStr] = Field(default=None, description="A unique identifier for the newly created analytic tenant. Required if creating new tenants.", alias="tenantCode")
    tenant_display_name: Optional[StrictStr] = Field(default=None, description="A new display name to assign to the analytic tenant. Required if creating new tenants.", alias="tenantDisplayName")
    tenant_short_name: Optional[StrictStr] = Field(default=None, description="A new short name to assign to the tenant. Required for analytic tenants.", alias="tenantShortName")
    update_action: Optional[StrictStr] = Field(default=None, description="Specifies the way you want to update values. Default is MERGE.  Valid values:  - `MERGE`: Combine the existing values with the new values.  - `REPLACE`: Remove existing values and let the new values take their place.", alias="updateAction")
    vanity_url_name: Optional[StrictStr] = Field(default=None, description="A new vanity name to assign to the tenant. Omit for new Embedded analytic tenants.", alias="vanityUrlName")
    __properties: ClassVar[List[str]] = ["allowedOAuthIdpUrlDomains", "clickThroughLink", "customProperties", "defaultCurrency", "embeddableDomains", "enabled", "homeAnalysisByUserGroup", "homeAnalysisId", "industryCode", "primaryBusinessLocation", "purchasedModules", "ssoInstanceIssuers", "tenantCode", "tenantDisplayName", "tenantShortName", "updateAction", "vanityUrlName"]

    @field_validator('update_action')
    def update_action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MERGE', 'REPLACE']):
            raise ValueError("must be one of enum values ('MERGE', 'REPLACE')")
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
        """Create an instance of AdminPublicapiTransfersTenantManagementAPIUpdateRequestDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in home_analysis_by_user_group (list)
        _items = []
        if self.home_analysis_by_user_group:
            for _item_home_analysis_by_user_group in self.home_analysis_by_user_group:
                if _item_home_analysis_by_user_group:
                    _items.append(_item_home_analysis_by_user_group.to_dict())
            _dict['homeAnalysisByUserGroup'] = _items
        # override the default output from pydantic by calling `to_dict()` of primary_business_location
        if self.primary_business_location:
            _dict['primaryBusinessLocation'] = self.primary_business_location.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdminPublicapiTransfersTenantManagementAPIUpdateRequestDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowedOAuthIdpUrlDomains": obj.get("allowedOAuthIdpUrlDomains"),
            "clickThroughLink": obj.get("clickThroughLink"),
            "customProperties": [AdminPublicapiTransfersCustomPropertyDTO.from_dict(_item) for _item in obj["customProperties"]] if obj.get("customProperties") is not None else None,
            "defaultCurrency": obj.get("defaultCurrency"),
            "embeddableDomains": obj.get("embeddableDomains"),
            "enabled": obj.get("enabled"),
            "homeAnalysisByUserGroup": [AdminPublicapiTransfersHomeAnalysisByUserGroupDTO.from_dict(_item) for _item in obj["homeAnalysisByUserGroup"]] if obj.get("homeAnalysisByUserGroup") is not None else None,
            "homeAnalysisId": obj.get("homeAnalysisId"),
            "industryCode": obj.get("industryCode"),
            "primaryBusinessLocation": AdminPublicapiTransfersBusinessLocationDTO.from_dict(obj["primaryBusinessLocation"]) if obj.get("primaryBusinessLocation") is not None else None,
            "purchasedModules": obj.get("purchasedModules"),
            "ssoInstanceIssuers": obj.get("ssoInstanceIssuers"),
            "tenantCode": obj.get("tenantCode"),
            "tenantDisplayName": obj.get("tenantDisplayName"),
            "tenantShortName": obj.get("tenantShortName"),
            "updateAction": obj.get("updateAction"),
            "vanityUrlName": obj.get("vanityUrlName")
        })
        return _obj


