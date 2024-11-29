# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_data_in.models.extraction_job import ExtractionJob
from typing import Optional, Set
from typing_extensions import Self

class ExtractionJobAndStatusResponse(BaseModel):
    """
    ExtractionJobAndStatusResponse
    """ # noqa: E501
    extraction_jobs: Optional[List[ExtractionJob]] = Field(default=None, description="A list of extraction job information.", alias="extractionJobs")
    limit: Optional[StrictInt] = Field(default=None, description="The number of extraction jobs to return. The maximum number of jobs to return is 1000.")
    parent_job_id: Optional[StrictStr] = Field(default=None, description="The ID of the dispatching job that generated the extraction jobs.", alias="parentJobId")
    parent_tenant_code: Optional[StrictStr] = Field(default=None, description="The tenant that owns the dispatching job. This is usually the administrating tenant.", alias="parentTenantCode")
    start: Optional[StrictInt] = Field(default=None, description="The index to start retrieving results from, also known as offset. The index begins at 0.")
    __properties: ClassVar[List[str]] = ["extractionJobs", "limit", "parentJobId", "parentTenantCode", "start"]

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
        """Create an instance of ExtractionJobAndStatusResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in extraction_jobs (list)
        _items = []
        if self.extraction_jobs:
            for _item_extraction_jobs in self.extraction_jobs:
                if _item_extraction_jobs:
                    _items.append(_item_extraction_jobs.to_dict())
            _dict['extractionJobs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExtractionJobAndStatusResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "extractionJobs": [ExtractionJob.from_dict(_item) for _item in obj["extractionJobs"]] if obj.get("extractionJobs") is not None else None,
            "limit": obj.get("limit"),
            "parentJobId": obj.get("parentJobId"),
            "parentTenantCode": obj.get("parentTenantCode"),
            "start": obj.get("start")
        })
        return _obj


