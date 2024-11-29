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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ExtractionJob(BaseModel):
    """
    ExtractionJob
    """ # noqa: E501
    current_stage: Optional[StrictStr] = Field(default=None, description="The current stage of the job. This is not returned if the stage is \"Completed\".  - Valid values: Initialize, Retrieve Main Subject, Retrieve Secondary Subjects, Retrieve Custom Subjects, Process Records, Publish Artifacts, Publish Records, Completed.", alias="currentStage")
    extraction_job_id: Optional[StrictStr] = Field(default=None, description="The ID of the extraction job.", alias="extractionJobId")
    status: Optional[StrictStr] = Field(default=None, description="The current state of the job.  - Valid values: Pending, Running, Succeeded, Failed, Error, Cancelling, Cancelled, RolledBack, Rescheduling, Rescheduled.")
    tenant_code: Optional[StrictStr] = Field(default=None, description="The tenant code of the analytic tenant for the extraction job.", alias="tenantCode")
    __properties: ClassVar[List[str]] = ["currentStage", "extractionJobId", "status", "tenantCode"]

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
        """Create an instance of ExtractionJob from a JSON string"""
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
        """Create an instance of ExtractionJob from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currentStage": obj.get("currentStage"),
            "extractionJobId": obj.get("extractionJobId"),
            "status": obj.get("status"),
            "tenantCode": obj.get("tenantCode")
        })
        return _obj


