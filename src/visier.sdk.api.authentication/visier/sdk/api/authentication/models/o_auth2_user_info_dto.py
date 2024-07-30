# coding: utf-8

"""
    Visier Authentication APIs

    Visier APIs for authenticating with Visier. To use Visier's public APIs, you must first authenticate yourself as a Visier user who is allowed to use Visier APIs.

    The version of the OpenAPI document: 22222222.99201.1418
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier.sdk.api.authentication.models.o_auth2_user_subnet_info_dto import OAuth2UserSubnetInfoDTO
from visier.sdk.api.authentication.models.o_auth2_user_tenant_details_dto import OAuth2UserTenantDetailsDTO
from visier.sdk.api.authentication.models.servicing_capability_proto_enum_access_lookup_dto import ServicingCapabilityProtoEnumAccessLookupDTO
from typing import Optional, Set
from typing_extensions import Self

class OAuth2UserInfoDTO(BaseModel):
    """
    Response from OAuth 2 `userinfo` endpoint.
    """ # noqa: E501
    email: Optional[StrictStr] = Field(default=None, description="The user's email address.")
    name: Optional[StrictStr] = Field(default=None, description="The user's Common Name.")
    subject: Optional[StrictStr] = Field(default=None, description="The user's display name.")
    visiercapabilities: Optional[ServicingCapabilityProtoEnumAccessLookupDTO] = Field(default=None, description="The user's profile capabilities.", alias="visier:capabilities")
    visierexport_subnets: Optional[OAuth2UserSubnetInfoDTO] = Field(default=None, description="Subnet restrictions controlling the IP addresses from which data and metadata requests can be made.", alias="visier:export_subnets")
    visiersubnets: Optional[OAuth2UserSubnetInfoDTO] = Field(default=None, description="Subnet restrictions controlling the IP addresses from which users can access the tenant.", alias="visier:subnets")
    visiertenant_details: Optional[OAuth2UserTenantDetailsDTO] = Field(default=None, description="Detailed information about the analytic tenant. Included in the response if `includeTenantDetail` is `true`.", alias="visier:tenant_details")
    visieruser_id: Optional[StrictStr] = Field(default=None, description="The user's unique ID.", alias="visier:user_id")
    __properties: ClassVar[List[str]] = ["email", "name", "subject", "visier:capabilities", "visier:export_subnets", "visier:subnets", "visier:tenant_details", "visier:user_id"]

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
        """Create an instance of OAuth2UserInfoDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of visiercapabilities
        if self.visiercapabilities:
            _dict['visier:capabilities'] = self.visiercapabilities.to_dict()
        # override the default output from pydantic by calling `to_dict()` of visierexport_subnets
        if self.visierexport_subnets:
            _dict['visier:export_subnets'] = self.visierexport_subnets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of visiersubnets
        if self.visiersubnets:
            _dict['visier:subnets'] = self.visiersubnets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of visiertenant_details
        if self.visiertenant_details:
            _dict['visier:tenant_details'] = self.visiertenant_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OAuth2UserInfoDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "name": obj.get("name"),
            "subject": obj.get("subject"),
            "visier:capabilities": ServicingCapabilityProtoEnumAccessLookupDTO.from_dict(obj["visier:capabilities"]) if obj.get("visier:capabilities") is not None else None,
            "visier:export_subnets": OAuth2UserSubnetInfoDTO.from_dict(obj["visier:export_subnets"]) if obj.get("visier:export_subnets") is not None else None,
            "visier:subnets": OAuth2UserSubnetInfoDTO.from_dict(obj["visier:subnets"]) if obj.get("visier:subnets") is not None else None,
            "visier:tenant_details": OAuth2UserTenantDetailsDTO.from_dict(obj["visier:tenant_details"]) if obj.get("visier:tenant_details") is not None else None,
            "visier:user_id": obj.get("visier:user_id")
        })
        return _obj


