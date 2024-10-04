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

class ProcessingJobRequestDTO(BaseModel):
    """
    ProcessingJobRequestDTO
    """ # noqa: E501
    all_tenants: Optional[StrictBool] = Field(default=None, description="If `true`, runs processing jobs for all accessible analytic tenants. Default is `false`. Only valid for requests from an administrating tenant.", alias="allTenants")
    data_category_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the data category to run the job. If omitted, runs a job using the primary data category.  To retrieve a list of all data categories, see `GET /v1/op/data/categories`.", alias="dataCategoryId")
    excluded_tenants: Optional[List[StrictStr]] = Field(default=None, description="The unique IDs of the tenants to exclude from the extraction job. Only valid if `allTenants` is \"true\". Only valid for requests from an administrating tenant.", alias="excludedTenants")
    publish_to_production: Optional[StrictBool] = Field(default=None, description="If `true`, publishes the generated data version to production. Default is `false`.", alias="publishToProduction")
    tenants: Optional[List[StrictStr]] = Field(default=None, description="The tenant codes of the tenants to run processing jobs for. If omitted, runs a processing job for the tenant associated with the user who made the API request. Only valid for requests from an administrating tenant.")
    __properties: ClassVar[List[str]] = ["allTenants", "dataCategoryId", "excludedTenants", "publishToProduction", "tenants"]

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
        """Create an instance of ProcessingJobRequestDTO from a JSON string"""
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
        """Create an instance of ProcessingJobRequestDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allTenants": obj.get("allTenants"),
            "dataCategoryId": obj.get("dataCategoryId"),
            "excludedTenants": obj.get("excludedTenants"),
            "publishToProduction": obj.get("publishToProduction"),
            "tenants": obj.get("tenants")
        })
        return _obj


