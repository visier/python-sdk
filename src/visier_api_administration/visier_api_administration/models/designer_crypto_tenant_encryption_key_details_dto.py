# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

    The version of the OpenAPI document: 22222222.99201.1905
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
from typing import Optional, Set
from typing_extensions import Self

class DesignerCryptoTenantEncryptionKeyDetailsDTO(BaseModel):
    """
    Information about who generated an encryption key, its key name, algorithm, generation date, and expiration date.
    """ # noqa: E501
    key_name: Optional[StrictStr] = Field(default=None, description="The encryption key's display name. The name may only contain alphanumeric or dash (-) characters and must be between 6 and 36 characters long.", alias="keyName")
    algorithm: Optional[StrictStr] = Field(default=None, description="The hash-based message authentication code and cryptographic hash function associated with the encryption key.")
    generated_by: Optional[StrictStr] = Field(default=None, description="The user who generated the key.", alias="generatedBy")
    date_generated: Optional[StrictStr] = Field(default=None, description="The UTC date that the key was generated in milliseconds since the Unix epoch.", alias="dateGenerated")
    expiry_date: Optional[StrictStr] = Field(default=None, description="The UTC expiration date of the key in milliseconds since the Unix epoch.", alias="expiryDate")
    __properties: ClassVar[List[str]] = ["keyName", "algorithm", "generatedBy", "dateGenerated", "expiryDate"]

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
        """Create an instance of DesignerCryptoTenantEncryptionKeyDetailsDTO from a JSON string"""
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
        """Create an instance of DesignerCryptoTenantEncryptionKeyDetailsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyName": obj.get("keyName"),
            "algorithm": obj.get("algorithm"),
            "generatedBy": obj.get("generatedBy"),
            "dateGenerated": obj.get("dateGenerated"),
            "expiryDate": obj.get("expiryDate")
        })
        return _obj


