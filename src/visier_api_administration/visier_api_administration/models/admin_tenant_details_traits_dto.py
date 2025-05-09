# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1892
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
from typing import Optional, Set
from typing_extensions import Self

class AdminTenantDetailsTraitsDTO(BaseModel):
    """
    The tenant's traits, including aggregation rights, tenant type, and data profile type.
    """ # noqa: E501
    aggregation_rights: Optional[StrictBool] = Field(default=None, description="If `true`, the tenant is opted in to Visier's data aggregation program, such as Visier Benchmarks. Default is `false`. If `false`, `aggregationRights` isn't returned in the response.", alias="aggregationRights")
    tenant_type: Optional[StrictStr] = Field(default=None, description="The tenant's type. Valid values:  * `ENTERPRISE`: An analytic tenant managed by Visier that represents an enterprise customer's instance of Visier.  * `PARTNER`: An administrating tenant that manages one or more analytic tenants. Partner tenants are managed by non-Visier administrators, such as an embedded partner or system integration partner.  * `PARTNER_CUSTOMER`: An analytic tenant managed by a partner that represents the partner's customer's instance of Visier.", alias="tenantType")
    data_profile_type: Optional[StrictStr] = Field(default=None, description="The tenant's data profile, which designates how the tenant's data is used. Valid values:  * `Regular`: An analytic tenant managed by Visier that represents an enterprise customer's instance of Visier.  * `Integration`: A partner tenant for development, staging, and testing.  * `Demo`: A Visier tenant for demonstrations and training.  * `Cat`: A consolidated analytics tenant for aggregating data from multiple analytic tenants in a single tenant.  * `Test`: A Visier tenant for development and testing.", alias="dataProfileType")
    __properties: ClassVar[List[str]] = ["aggregationRights", "tenantType", "dataProfileType"]

    @field_validator('tenant_type')
    def tenant_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ROOT_ADMIN', 'ROOT', 'BLUEPRINT', 'ENTERPRISE', 'ENTERPRISE_ROOT', 'BENCHMARK', 'PARTNER', 'PARTNER_CUSTOMER', 'SMB_BP', 'SMB_CUSTOMER', 'UNKNOWN']):
            raise ValueError("must be one of enum values ('ROOT_ADMIN', 'ROOT', 'BLUEPRINT', 'ENTERPRISE', 'ENTERPRISE_ROOT', 'BENCHMARK', 'PARTNER', 'PARTNER_CUSTOMER', 'SMB_BP', 'SMB_CUSTOMER', 'UNKNOWN')")
        return value

    @field_validator('data_profile_type')
    def data_profile_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Regular', 'Integration', 'Demo', 'Cat', 'Test']):
            raise ValueError("must be one of enum values ('Regular', 'Integration', 'Demo', 'Cat', 'Test')")
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
        """Create an instance of AdminTenantDetailsTraitsDTO from a JSON string"""
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
        """Create an instance of AdminTenantDetailsTraitsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aggregationRights": obj.get("aggregationRights"),
            "tenantType": obj.get("tenantType"),
            "dataProfileType": obj.get("dataProfileType")
        })
        return _obj


