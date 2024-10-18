# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1534
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
from visier_api_data_in.models.icims_basic_auth_params_dto import IcimsBasicAuthParamsDTO
from visier_api_data_in.models.icims_client_credentials_auth_params_dto import IcimsClientCredentialsAuthParamsDTO
from typing import Optional, Set
from typing_extensions import Self

class IcimsAuthParamsDTO(BaseModel):
    """
    IcimsAuthParamsDTO
    """ # noqa: E501
    basic_auth: Optional[IcimsBasicAuthParamsDTO] = Field(default=None, alias="basicAuth")
    client_credentials: Optional[IcimsClientCredentialsAuthParamsDTO] = Field(default=None, alias="clientCredentials")
    customer_id: Optional[StrictStr] = Field(default=None, alias="customerId")
    __properties: ClassVar[List[str]] = ["basicAuth", "clientCredentials", "customerId"]

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
        """Create an instance of IcimsAuthParamsDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of basic_auth
        if self.basic_auth:
            _dict['basicAuth'] = self.basic_auth.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client_credentials
        if self.client_credentials:
            _dict['clientCredentials'] = self.client_credentials.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IcimsAuthParamsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "basicAuth": IcimsBasicAuthParamsDTO.from_dict(obj["basicAuth"]) if obj.get("basicAuth") is not None else None,
            "clientCredentials": IcimsClientCredentialsAuthParamsDTO.from_dict(obj["clientCredentials"]) if obj.get("clientCredentials") is not None else None,
            "customerId": obj.get("customerId")
        })
        return _obj


