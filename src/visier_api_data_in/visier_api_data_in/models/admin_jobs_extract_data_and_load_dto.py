# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1876
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AdminJobsExtractDataAndLoadDTO(BaseModel):
    """
    AdminJobsExtractDataAndLoadDTO
    """ # noqa: E501
    tenants: Optional[List[StrictStr]] = Field(default=None, description="A list of analytic tenants to dispatch extraction jobs for. One extraction job is dispatched per tenant. Only valid for requests from an administrating tenant.")
    all_tenants: Optional[StrictBool] = Field(default=None, description="If `true`, one extraction job is dispatched for each accessible analytic tenant. Only valid for requests from an administrating tenant.", alias="allTenants")
    override_last_extraction_timestamp: Optional[StrictStr] = Field(default=None, description="An epoch timestamp in milliseconds from which to retrieve data. This overrides the last extraction date to retrieve more data.", alias="overrideLastExtractionTimestamp")
    publish_data_load_artifacts: Optional[StrictBool] = Field(default=None, description="If `true`, the generated data load artifacts are published to production immediately.", alias="publishDataLoadArtifacts")
    run_processing_job: Optional[StrictBool] = Field(default=None, description="If `true`, a processing job is spawned after a dispatched extraction job runs successfully.", alias="runProcessingJob")
    data_category_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the data category on which to trigger the extraction job. Default is the tenant's primary data category.", alias="dataCategoryId")
    disable_artifact_generation: Optional[StrictBool] = Field(default=None, description="If `true`, the job does not generate data load artifacts. If unspecified, the default is `false`.", alias="disableArtifactGeneration")
    connector_ids: Optional[List[StrictStr]] = Field(default=None, description="The unique identifiers of the connectors to run extraction jobs.", alias="connectorIds")
    last_extraction_time_offset_weeks: Optional[StrictInt] = Field(default=None, description="The number of weeks in the past to retrieve data. This overrides the last extraction date to retrieve more data.", alias="lastExtractionTimeOffsetWeeks")
    months_to_extract: Optional[StrictInt] = Field(default=None, description="The number of months to retrieve snapshot data.", alias="monthsToExtract")
    extract_to_time_override: Optional[StrictStr] = Field(default=None, description="An epoch timestamp in milliseconds for the end time up to which to retrieve data.", alias="extractToTimeOverride")
    batch_size_override: Optional[StrictInt] = Field(default=None, description="The maximum number of subjects the job can retrieve in each batch.", alias="batchSizeOverride")
    sql_batch_size: Optional[StrictInt] = Field(default=None, description="The maximum number of SQL table records the job can retrieve in each batch.", alias="sqlBatchSize")
    force_update_existing_artifacts: Optional[StrictBool] = Field(default=None, description="If `true` and `disableArtifactGeneration` is `false`, updates extractor artifacts, which may overwrite the artifacts' manual overrides. Ignored if `disableArtifactGeneration` is `true`.", alias="forceUpdateExistingArtifacts")
    excluded_tenants: Optional[List[StrictStr]] = Field(default=None, description="The unique identifiers of the tenants to exclude from the extraction job. Only valid if `allTenants` is `true`. Only valid for requests from an administrating tenant.", alias="excludedTenants")
    spill_debug_info_partitions_dto: Optional[StrictStr] = Field(default=None, description="The partitioning of debugging info to be generated, if any. Valid values are:  - `spillNone`: No debugging info is generated.  - `spillStagesAndRecords`: Debugging info is generated for stages and records.  - `spillAll`: Debugging info is generated for all partitions.", alias="spillDebugInfoPartitionsDTO")
    spill_debug_info_detail_level_dto: Optional[StrictStr] = Field(default=None, description="The detail level of the debugging info to be generated. Valid values are:  - `fileAndLine`: Debugging info is generated for file and line.  - `mappingName`: Debugging info is generated for mapping name.", alias="spillDebugInfoDetailLevelDTO")
    last_extraction_time_offset_months: Optional[StrictInt] = Field(default=None, description="The number of months to offset the last extraction time. This overrides the last extraction date backward to retrieve more data.", alias="lastExtractionTimeOffsetMonths")
    last_extraction_time_offset_mode: Optional[StrictStr] = Field(default=None, description="The mode used to offset the last extraction time (weeks vs months)", alias="lastExtractionTimeOffsetMode")
    offset_week_option: Optional[StrictStr] = Field(default=None, description="The week options used to offset the last extraction time (first of day / last of day)", alias="offsetWeekOption")
    offset_month_option: Optional[StrictStr] = Field(default=None, description="The month options used to offset the last extraction time (first of month / last of month)", alias="offsetMonthOption")
    credential_id: Optional[StrictStr] = Field(default=None, alias="credentialId")
    __properties: ClassVar[List[str]] = ["tenants", "allTenants", "overrideLastExtractionTimestamp", "publishDataLoadArtifacts", "runProcessingJob", "dataCategoryId", "disableArtifactGeneration", "connectorIds", "lastExtractionTimeOffsetWeeks", "monthsToExtract", "extractToTimeOverride", "batchSizeOverride", "sqlBatchSize", "forceUpdateExistingArtifacts", "excludedTenants", "spillDebugInfoPartitionsDTO", "spillDebugInfoDetailLevelDTO", "lastExtractionTimeOffsetMonths", "lastExtractionTimeOffsetMode", "offsetWeekOption", "offsetMonthOption", "credentialId"]

    @field_validator('spill_debug_info_partitions_dto')
    def spill_debug_info_partitions_dto_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['spillNone', 'spillStagesAndRecords', 'spillAll']):
            raise ValueError("must be one of enum values ('spillNone', 'spillStagesAndRecords', 'spillAll')")
        return value

    @field_validator('spill_debug_info_detail_level_dto')
    def spill_debug_info_detail_level_dto_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['fileAndLine', 'mappingName']):
            raise ValueError("must be one of enum values ('fileAndLine', 'mappingName')")
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
        """Create an instance of AdminJobsExtractDataAndLoadDTO from a JSON string"""
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
        """Create an instance of AdminJobsExtractDataAndLoadDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenants": obj.get("tenants"),
            "allTenants": obj.get("allTenants"),
            "overrideLastExtractionTimestamp": obj.get("overrideLastExtractionTimestamp"),
            "publishDataLoadArtifacts": obj.get("publishDataLoadArtifacts"),
            "runProcessingJob": obj.get("runProcessingJob"),
            "dataCategoryId": obj.get("dataCategoryId"),
            "disableArtifactGeneration": obj.get("disableArtifactGeneration"),
            "connectorIds": obj.get("connectorIds"),
            "lastExtractionTimeOffsetWeeks": obj.get("lastExtractionTimeOffsetWeeks"),
            "monthsToExtract": obj.get("monthsToExtract"),
            "extractToTimeOverride": obj.get("extractToTimeOverride"),
            "batchSizeOverride": obj.get("batchSizeOverride"),
            "sqlBatchSize": obj.get("sqlBatchSize"),
            "forceUpdateExistingArtifacts": obj.get("forceUpdateExistingArtifacts"),
            "excludedTenants": obj.get("excludedTenants"),
            "spillDebugInfoPartitionsDTO": obj.get("spillDebugInfoPartitionsDTO"),
            "spillDebugInfoDetailLevelDTO": obj.get("spillDebugInfoDetailLevelDTO"),
            "lastExtractionTimeOffsetMonths": obj.get("lastExtractionTimeOffsetMonths"),
            "lastExtractionTimeOffsetMode": obj.get("lastExtractionTimeOffsetMode"),
            "offsetWeekOption": obj.get("offsetWeekOption"),
            "offsetMonthOption": obj.get("offsetMonthOption"),
            "credentialId": obj.get("credentialId")
        })
        return _obj


