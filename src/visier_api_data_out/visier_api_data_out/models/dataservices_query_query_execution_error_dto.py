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
from visier_api_data_out.models.dataservices_query_query_execution_errors_dto import DataservicesQueryQueryExecutionErrorsDTO
from typing import Optional, Set
from typing_extensions import Self

class DataservicesQueryQueryExecutionErrorDTO(BaseModel):
    """
    An error that occurred during query execution. A QueryExecutionError returns as part of a  successful batch aggregation query for any queries that failed. This is different from errors,  which return for failed requests.
    """ # noqa: E501
    error_code: Optional[StrictStr] = Field(default=None, description="A brief identifier of the type of error.", alias="errorCode")
    message: Optional[StrictStr] = Field(default=None, description="The details of the error.")
    all_errors: Optional[List[DataservicesQueryQueryExecutionErrorsDTO]] = Field(default=None, description="All errors", alias="allErrors")
    __properties: ClassVar[List[str]] = ["errorCode", "message", "allErrors"]

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
        """Create an instance of DataservicesQueryQueryExecutionErrorDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in all_errors (list)
        _items = []
        if self.all_errors:
            for _item_all_errors in self.all_errors:
                if _item_all_errors:
                    _items.append(_item_all_errors.to_dict())
            _dict['allErrors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataservicesQueryQueryExecutionErrorDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "errorCode": obj.get("errorCode"),
            "message": obj.get("message"),
            "allErrors": [DataservicesQueryQueryExecutionErrorsDTO.from_dict(_item) for _item in obj["allErrors"]] if obj.get("allErrors") is not None else None
        })
        return _obj


