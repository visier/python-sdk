# coding: utf-8

"""
    API Reference

    Detailed API reference documentation for Visier APIs. Includes all endpoints, headers, path parameters, query parameters, request body schema, response schema, JSON request samples, and JSON response samples.

    The version of the OpenAPI document: 22222222.99201.2050
    Contact: alpine@visier.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SalaryBenchmarkInput(BaseModel):
    """
    SalaryBenchmarkInput
    """ # noqa: E501
    uuid: StrictStr = Field(description="A unique identifier of the individual requests. ")
    job: StrictStr = Field(description="The job member ID. ")
    industry: Optional[StrictStr] = Field(default=None, description="The industry member ID. If the ID is not provided, the response returns the benchmark value across all industries. ")
    naics_code: Optional[StrictStr] = Field(default=None, description="The North American Industry Classification System (NAICS) code.  If the NAICS code is not provided, the response returns the benchmark value across all industries. If both `naicsCode` and `industry` are provided, the response returns the benchmark value for the `industry` parameter. The entered `naicsCode` will not be applied. ", alias="naicsCode")
    location: Optional[StrictStr] = Field(default=None, description="The location member ID. If the ID is not provided, the response returns the benchmark value across all locations. ")
    company_size: Optional[StrictStr] = Field(default=None, description="The company size member ID. If the ID is not provided, the response returns the benchmark value across all company sizes. ", alias="companySize")
    career_level: Optional[StrictStr] = Field(default=None, description="The career level member ID. If the ID is not provided, the response returns the benchmark value across all career levels. ", alias="careerLevel")
    __properties: ClassVar[List[str]] = ["uuid", "job", "industry", "naicsCode", "location", "companySize", "careerLevel"]

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
        """Create an instance of SalaryBenchmarkInput from a JSON string"""
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
        """Create an instance of SalaryBenchmarkInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "job": obj.get("job"),
            "industry": obj.get("industry"),
            "naicsCode": obj.get("naicsCode"),
            "location": obj.get("location"),
            "companySize": obj.get("companySize"),
            "careerLevel": obj.get("careerLevel")
        })
        return _obj


