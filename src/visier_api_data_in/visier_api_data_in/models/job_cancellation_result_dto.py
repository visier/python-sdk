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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class JobCancellationResultDTO(BaseModel):
    """
    JobCancellationResultDTO
    """ # noqa: E501
    cancel_status: Optional[StrictStr] = Field(default=None, description="The status of the cancellation.", alias="cancelStatus")
    job_id: Optional[StrictStr] = Field(default=None, description="The job ID of the job that the cancel operation was conducted for.", alias="jobId")
    job_status: Optional[StrictStr] = Field(default=None, description="The job status after the cancel operation. If successful, the status is either Cancelled or Cancelling.", alias="jobStatus")
    job_type: Optional[StrictStr] = Field(default=None, description="The job type associated with the job ID.", alias="jobType")
    message: Optional[StrictStr] = Field(default=None, description="If applicable, the message explains what errors occurred while cancelling the jobs.")
    parent_job_id: Optional[StrictStr] = Field(default=None, description="If applicable, the job ID of the job that spawned the given job.", alias="parentJobId")
    tenant_code: Optional[StrictStr] = Field(default=None, description="The analytic tenant whose job the cancel operation was conducted for.", alias="tenantCode")
    __properties: ClassVar[List[str]] = ["cancelStatus", "jobId", "jobStatus", "jobType", "message", "parentJobId", "tenantCode"]

    @field_validator('cancel_status')
    def cancel_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CANCEL_FAILED', 'CANCEL_SUCCEEDED']):
            raise ValueError("must be one of enum values ('CANCEL_FAILED', 'CANCEL_SUCCEEDED')")
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
        """Create an instance of JobCancellationResultDTO from a JSON string"""
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
        """Create an instance of JobCancellationResultDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cancelStatus": obj.get("cancelStatus"),
            "jobId": obj.get("jobId"),
            "jobStatus": obj.get("jobStatus"),
            "jobType": obj.get("jobType"),
            "message": obj.get("message"),
            "parentJobId": obj.get("parentJobId"),
            "tenantCode": obj.get("tenantCode")
        })
        return _obj


