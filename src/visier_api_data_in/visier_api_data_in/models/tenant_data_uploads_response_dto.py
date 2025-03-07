# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1772
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
from visier_api_data_in.models.tenant_data_upload_status_response_dto import TenantDataUploadStatusResponseDTO
from typing import Optional, Set
from typing_extensions import Self

class TenantDataUploadsResponseDTO(BaseModel):
    """
    TenantDataUploadsResponseDTO
    """ # noqa: E501
    tenant_code: Optional[StrictStr] = Field(default=None, description="The tenant code of the analytic tenant owning the data uploads.", alias="tenantCode")
    uploads: Optional[List[TenantDataUploadStatusResponseDTO]] = Field(default=None, description="The data uploads completed for the specified analytic tenant. The list is empty if no previous data uploads are found for the analytic tenant.")
    __properties: ClassVar[List[str]] = ["tenantCode", "uploads"]

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
        """Create an instance of TenantDataUploadsResponseDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in uploads (list)
        _items = []
        if self.uploads:
            for _item_uploads in self.uploads:
                if _item_uploads:
                    _items.append(_item_uploads.to_dict())
            _dict['uploads'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantDataUploadsResponseDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantCode": obj.get("tenantCode"),
            "uploads": [TenantDataUploadStatusResponseDTO.from_dict(_item) for _item in obj["uploads"]] if obj.get("uploads") is not None else None
        })
        return _obj


