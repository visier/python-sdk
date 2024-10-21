# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1537
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

class DirectDataJobConfigDTO(BaseModel):
    """
    Whether the direct data intake job is a primary job or a supplemental job.
    """ # noqa: E501
    extend_objects: Optional[List[StrictStr]] = Field(default=None, description="The target analytic objects to load using extension tables.  You can extend objects if the job type is supplemental and the target objects already contain data from a previous data version.  This allows you to load data for objects that already contain data in Visier.", alias="extendObjects")
    supplemental_mode: Optional[StrictStr] = Field(default=None, description="The configuration for the processing job as a primary job (default) or a supplemental job. If a primary job is already defined, the direct data   intake job must be supplemental. The valid values are `IS_PRIMARY`, `IS_SUPPLEMENTAL`, and `UNCHANGED`.", alias="supplementalMode")
    __properties: ClassVar[List[str]] = ["extendObjects", "supplementalMode"]

    @field_validator('supplemental_mode')
    def supplemental_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['UNCHANGED', 'IS_PRIMARY', 'IS_SUPPLEMENTAL']):
            raise ValueError("must be one of enum values ('UNCHANGED', 'IS_PRIMARY', 'IS_SUPPLEMENTAL')")
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
        """Create an instance of DirectDataJobConfigDTO from a JSON string"""
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
        """Create an instance of DirectDataJobConfigDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "extendObjects": obj.get("extendObjects"),
            "supplementalMode": obj.get("supplementalMode")
        })
        return _obj


