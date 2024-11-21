# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1598
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

class DownloadSourceFilesDTO(BaseModel):
    """
    DownloadSourceFilesDTO
    """ # noqa: E501
    download_all: Optional[StrictBool] = Field(default=None, description="If `true`, downloads all uploaded files for all sources. Default is `false`.", alias="downloadAll")
    max_timestamp: Optional[StrictStr] = Field(default=None, description="The latest upload time to download files up to in ISO-8601 format, such as `\"2001-10-25T13:45:35.999\"`. If omitted, downloads files up to the latest available time.", alias="maxTimestamp")
    min_timestamp: Optional[StrictStr] = Field(default=None, description="The earliest upload time to download files from in ISO-8601 format, such as `\"2001-10-25T13:45:35.999\"`. If omitted, downloads files from the earliest available time.", alias="minTimestamp")
    source_ids: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated list of strings representing the unique identifier of each source to download.", alias="sourceIds")
    sources: Optional[List[StrictStr]] = Field(default=None, description="A comma-separated list of strings representing the object name of each source to download.")
    __properties: ClassVar[List[str]] = ["downloadAll", "maxTimestamp", "minTimestamp", "sourceIds", "sources"]

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
        """Create an instance of DownloadSourceFilesDTO from a JSON string"""
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
        """Create an instance of DownloadSourceFilesDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "downloadAll": obj.get("downloadAll"),
            "maxTimestamp": obj.get("maxTimestamp"),
            "minTimestamp": obj.get("minTimestamp"),
            "sourceIds": obj.get("sourceIds"),
            "sources": obj.get("sources")
        })
        return _obj


