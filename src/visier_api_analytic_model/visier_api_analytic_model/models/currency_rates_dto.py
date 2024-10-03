# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1497
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_analytic_model.models.currency_rate_dto import CurrencyRateDTO
from typing import Optional, Set
from typing_extensions import Self

class CurrencyRatesDTO(BaseModel):
    """
    A collection of currency exchange rates.  Note: Currencies may have different exchange rates in different time intervals, depending what rate data is stored in Visier.  For example, USD:CAD can be 1.2 between January 1 - March 1, while USD:EUR can be 0.92 between January 1 - February 1, but 0.88 between February  1 - March 1.
    """ # noqa: E501
    currency_rates: Optional[List[CurrencyRateDTO]] = Field(default=None, alias="currencyRates")
    __properties: ClassVar[List[str]] = ["currencyRates"]

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
        """Create an instance of CurrencyRatesDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in currency_rates (list)
        _items = []
        if self.currency_rates:
            for _item_currency_rates in self.currency_rates:
                if _item_currency_rates:
                    _items.append(_item_currency_rates.to_dict())
            _dict['currencyRates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CurrencyRatesDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currencyRates": [CurrencyRateDTO.from_dict(_item) for _item in obj["currencyRates"]] if obj.get("currencyRates") is not None else None
        })
        return _obj


