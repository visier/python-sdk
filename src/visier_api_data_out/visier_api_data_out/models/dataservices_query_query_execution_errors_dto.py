# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1892
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
from visier_api_data_out.models.dataservices_query_query_execution_error_details_dto import DataservicesQueryQueryExecutionErrorDetailsDTO
from typing import Optional, Set
from typing_extensions import Self

class DataservicesQueryQueryExecutionErrorsDTO(BaseModel):
    """
    The errors that occurred during query execution.
    """ # noqa: E501
    error_code: Optional[StrictStr] = Field(default=None, description="A brief identifier of the type of error.", alias="errorCode")
    message: Optional[StrictStr] = Field(default=None, description="The message of the error.")
    all_error_details: Optional[List[DataservicesQueryQueryExecutionErrorDetailsDTO]] = Field(default=None, description="The list of the error details.", alias="allErrorDetails")
    __properties: ClassVar[List[str]] = ["errorCode", "message", "allErrorDetails"]

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
        """Create an instance of DataservicesQueryQueryExecutionErrorsDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in all_error_details (list)
        _items = []
        if self.all_error_details:
            for _item_all_error_details in self.all_error_details:
                if _item_all_error_details:
                    _items.append(_item_all_error_details.to_dict())
            _dict['allErrorDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataservicesQueryQueryExecutionErrorsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "errorCode": obj.get("errorCode"),
            "message": obj.get("message"),
            "allErrorDetails": [DataservicesQueryQueryExecutionErrorDetailsDTO.from_dict(_item) for _item in obj["allErrorDetails"]] if obj.get("allErrorDetails") is not None else None
        })
        return _obj


