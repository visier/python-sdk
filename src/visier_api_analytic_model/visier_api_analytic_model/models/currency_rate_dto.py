# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CurrencyRateDTO(BaseModel):
    """
    Information about a currency exchange rate.
    """ # noqa: E501
    end_time: Optional[StrictStr] = Field(default=None, description="The latest time instant to retrieve exchange rates from.  **Note:** Format is the number of milliseconds since Jan 1, 1970 12:00 AM UTC.", alias="endTime")
    from_currency_code: Optional[StrictStr] = Field(default=None, description="The currency to convert **from**.  **Note:** If USD is the `fromCurrencyCode`, you are retrieving the exchange rates from USD to a different currency.", alias="fromCurrencyCode")
    rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The numeric value of the exchange rate.  **Note:** If **decimals** is specified, rate rounds to that value. If **decimals** is undefined, **rate** rounds to 2 significant figures after the decimal point.")
    start_time: Optional[StrictStr] = Field(default=None, description="The earliest time instant to retrieve exchange rates from.  **Note:** Format is the number of milliseconds since Jan 1, 1970 12:00 AM UTC.", alias="startTime")
    to_currency_code: Optional[StrictStr] = Field(default=None, description="The currency to convert **to**.  **Note:** If USD is the `toCurrencyCode`, you are retrieving the exchange rates from a different currency to USD.", alias="toCurrencyCode")
    __properties: ClassVar[List[str]] = ["endTime", "fromCurrencyCode", "rate", "startTime", "toCurrencyCode"]

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
        """Create an instance of CurrencyRateDTO from a JSON string"""
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
        """Create an instance of CurrencyRateDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "endTime": obj.get("endTime"),
            "fromCurrencyCode": obj.get("fromCurrencyCode"),
            "rate": obj.get("rate"),
            "startTime": obj.get("startTime"),
            "toCurrencyCode": obj.get("toCurrencyCode")
        })
        return _obj


