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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class StartExtractionModel(BaseModel):
    """
    StartExtractionModel
    """ # noqa: E501
    all_tenants: Optional[StrictBool] = Field(default=None, description="If `true`, one extraction job is dispatched for each accessible analytic tenant. Only valid for requests from an administrating tenant.", alias="allTenants")
    batch_size_override: Optional[StrictInt] = Field(default=None, description="The maximum number of subjects the job can retrieve in each batch.", alias="batchSizeOverride")
    connector_ids: Optional[List[StrictStr]] = Field(default=None, description="The unique identifiers of the connectors to run extraction jobs.", alias="connectorIds")
    data_category_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the data category on which to trigger the extraction job. Default is the tenant's primary data category.", alias="dataCategoryId")
    disable_artifact_generation: Optional[StrictBool] = Field(default=None, description="If `true`, the job does not generate data load artifacts. If unspecified, the default is `false`.", alias="disableArtifactGeneration")
    excluded_tenants: Optional[List[StrictStr]] = Field(default=None, description="The unique IDs of the tenants to exclude from the extraction job. Only valid if `allTenants` is \"true\". Only valid for requests from an administrating tenant.", alias="excludedTenants")
    extract_to_time_override: Optional[StrictStr] = Field(default=None, description="An epoch timestamp in milliseconds for the end time up to which to retrieve data.", alias="extractToTimeOverride")
    force_update_existing_artifacts: Optional[StrictBool] = Field(default=None, description="If `true` and `disableArtifactGeneration` is `false`, updates extractor artifacts, which may overwrite the artifacts' manual overrides. Ignored if `disableArtifactGeneration` is `true`.", alias="forceUpdateExistingArtifacts")
    last_extraction_time_offset_weeks: Optional[StrictInt] = Field(default=None, description="The number of weeks in the past to retrieve data. This overrides the last extraction date to retrieve more data.", alias="lastExtractionTimeOffsetWeeks")
    months_to_extract: Optional[StrictInt] = Field(default=None, description="The number of months to retrieve snapshot data.", alias="monthsToExtract")
    override_last_extraction_timestamp: Optional[StrictStr] = Field(default=None, description="The time from which to extract data.", alias="overrideLastExtractionTimestamp")
    publish_data_load_artifacts: Optional[StrictBool] = Field(default=None, description="If `true`, the generated data load artifacts are published to production immediately.", alias="publishDataLoadArtifacts")
    run_processing_job: Optional[StrictBool] = Field(default=None, description="If `true`, a processing job is spawned after a dispatched extraction job runs successfully.", alias="runProcessingJob")
    sql_batch_size: Optional[StrictInt] = Field(default=None, description="The maximum amount of SQL table records the job can retrieve in each batch.", alias="sqlBatchSize")
    tenants: Optional[List[StrictStr]] = Field(default=None, description="A list of analytic tenants to dispatch extraction jobs for. One extraction job is dispatched per tenant. Only valid for requests from an administrating tenant.")
    __properties: ClassVar[List[str]] = ["allTenants", "batchSizeOverride", "connectorIds", "dataCategoryId", "disableArtifactGeneration", "excludedTenants", "extractToTimeOverride", "forceUpdateExistingArtifacts", "lastExtractionTimeOffsetWeeks", "monthsToExtract", "overrideLastExtractionTimestamp", "publishDataLoadArtifacts", "runProcessingJob", "sqlBatchSize", "tenants"]

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
        """Create an instance of StartExtractionModel from a JSON string"""
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
        """Create an instance of StartExtractionModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allTenants": obj.get("allTenants"),
            "batchSizeOverride": obj.get("batchSizeOverride"),
            "connectorIds": obj.get("connectorIds"),
            "dataCategoryId": obj.get("dataCategoryId"),
            "disableArtifactGeneration": obj.get("disableArtifactGeneration"),
            "excludedTenants": obj.get("excludedTenants"),
            "extractToTimeOverride": obj.get("extractToTimeOverride"),
            "forceUpdateExistingArtifacts": obj.get("forceUpdateExistingArtifacts"),
            "lastExtractionTimeOffsetWeeks": obj.get("lastExtractionTimeOffsetWeeks"),
            "monthsToExtract": obj.get("monthsToExtract"),
            "overrideLastExtractionTimestamp": obj.get("overrideLastExtractionTimestamp"),
            "publishDataLoadArtifacts": obj.get("publishDataLoadArtifacts"),
            "runProcessingJob": obj.get("runProcessingJob"),
            "sqlBatchSize": obj.get("sqlBatchSize"),
            "tenants": obj.get("tenants")
        })
        return _obj


