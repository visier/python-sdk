# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1508
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UploadToExclude(BaseModel):
    """
    UploadToExclude
    """ # noqa: E501
    exclude_all: Optional[StrictBool] = Field(default=None, description="If `true`, all data uploads are excluded for the analytic tenant.", alias="excludeAll")
    max_upload_time: Optional[StrictStr] = Field(default=None, description="An ISO8601 time such as `\"2001-10-25T13:45:35.999\"` for the latest upload time. If defined, omit `uploadTimes`. If omitted and `minUploadTime` is defined, excludes files up to latest time available.", alias="maxUploadTime")
    min_upload_time: Optional[StrictStr] = Field(default=None, description="An ISO8601 time such as `\"2001-10-25T13:45:35.999\"` for the earliest upload time. If defined, omit `uploadTimes`. If omitted and `maxUploadTime` is defined, excludes files up to earliest time available.", alias="minUploadTime")
    sources: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated list of strings representing the object name of each source to exclude. If `uploadTimes` is omitted, excludes files for the given sources for all `uploadTimes`.")
    tenant_code: Optional[StrictStr] = Field(default=None, description="The tenant code of the analytic tenant you are excluding a data upload for.", alias="tenantCode")
    upload_times: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated list of ISO8601 time strings such as `\"2001-10-25T13:45:35.999\"` representing the upload time of each data upload to exclude.", alias="uploadTimes")
    __properties: ClassVar[List[str]] = ["excludeAll", "maxUploadTime", "minUploadTime", "sources", "tenantCode", "uploadTimes"]

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
        """Create an instance of UploadToExclude from a JSON string"""
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
        """Create an instance of UploadToExclude from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "excludeAll": obj.get("excludeAll"),
            "maxUploadTime": obj.get("maxUploadTime"),
            "minUploadTime": obj.get("minUploadTime"),
            "sources": obj.get("sources"),
            "tenantCode": obj.get("tenantCode"),
            "uploadTimes": obj.get("uploadTimes")
        })
        return _obj


