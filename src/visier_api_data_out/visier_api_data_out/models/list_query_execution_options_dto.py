# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1694
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

class ListQueryExecutionOptionsDTO(BaseModel):
    """
    A ListQueryExecutionOptions provides additional instructions to perform a list query.
    """ # noqa: E501
    calendar_type: Optional[StrictStr] = Field(default=None, description="The calendar type to use. This will be used for all time calculations unless explicitly overridden in  the calculation itself. Default is TENANT_CALENDAR.", alias="calendarType")
    currency_conversion_code: Optional[StrictStr] = Field(default=None, description="The optional target currency for all currency conversions.  If not specified, the tenant default currency will be used.", alias="currencyConversionCode")
    currency_conversion_date: Optional[StrictStr] = Field(default=None, description="The currency conversion date to use. If defined, the currency conversion will use the exchange rates as of this date.", alias="currencyConversionDate")
    currency_conversion_mode: Optional[StrictStr] = Field(default=None, description="The currency conversion mode to use. This will be used for all currency conversion calculations unless explicitly  overridden in the calculation itself. Default is TENANT_CURRENCY_CONVERSION.", alias="currencyConversionMode")
    date_time_display_mode: Optional[StrictStr] = Field(default=None, description="Control how date-time values are displayed in the result set.  Supported values:  * `EPOCH`: The number of elapsed milliseconds since January 1, 1970 in UTC timezone. This is the default.  * `DATETIME`: The date-time value displayed in `yyyy-MM-dd HH:mm:ssZZ` format.", alias="dateTimeDisplayMode")
    limit: Optional[StrictInt] = Field(default=None, description="The maximum number of entries to return. Default is to return all entries. If `page` is defined but  limit is not defined, limit will be set to a default value of 1000.")
    multiple_tables: Optional[StrictBool] = Field(default=None, description="Option to return multiple table files as zipped archive for derived metrics.  Default is false. If false, one table is returned for the drill-through metric.", alias="multipleTables")
    omit_header: Optional[StrictBool] = Field(default=None, description="Option to omit the header from the result.  If true, queryMode must be either FILL or FAIL.  Default is false.", alias="omitHeader")
    page: Optional[StrictInt] = Field(default=None, description="A page defines a subset of the overall result set. The number of rows per page is equal to limit  with the exception of the last page in the result set which may contain fewer rows. `Page` is an index  that begins at 0. The index to start retrieving results is calculated by multiplying `page` by `limit`.")
    query_mode: Optional[StrictStr] = Field(default=None, description="Determines how the query should handle column definitions that the query is unable to resolve. Default is DEFAULT.", alias="queryMode")
    record_mode: Optional[StrictStr] = Field(default=None, description="Influences the type of records used to build the result set, such as whether to return  one record per entity that is valid in the provided time range or each change record  falls in the time frame.", alias="recordMode")
    __properties: ClassVar[List[str]] = ["calendarType", "currencyConversionCode", "currencyConversionDate", "currencyConversionMode", "dateTimeDisplayMode", "limit", "multipleTables", "omitHeader", "page", "queryMode", "recordMode"]

    @field_validator('calendar_type')
    def calendar_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['TENANT_CALENDAR', 'GREGORIAN_CALENDAR']):
            raise ValueError("must be one of enum values ('TENANT_CALENDAR', 'GREGORIAN_CALENDAR')")
        return value

    @field_validator('currency_conversion_mode')
    def currency_conversion_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['TENANT_CURRENCY_CONVERSION', 'VISIER_CURRENCY_CONVERSION']):
            raise ValueError("must be one of enum values ('TENANT_CURRENCY_CONVERSION', 'VISIER_CURRENCY_CONVERSION')")
        return value

    @field_validator('date_time_display_mode')
    def date_time_display_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['EPOCH', 'DATETIME']):
            raise ValueError("must be one of enum values ('EPOCH', 'DATETIME')")
        return value

    @field_validator('query_mode')
    def query_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DEFAULT', 'FILL', 'FAIL']):
            raise ValueError("must be one of enum values ('DEFAULT', 'FILL', 'FAIL')")
        return value

    @field_validator('record_mode')
    def record_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NORMAL', 'CHANGES']):
            raise ValueError("must be one of enum values ('NORMAL', 'CHANGES')")
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
        """Create an instance of ListQueryExecutionOptionsDTO from a JSON string"""
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
        """Create an instance of ListQueryExecutionOptionsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "calendarType": obj.get("calendarType"),
            "currencyConversionCode": obj.get("currencyConversionCode"),
            "currencyConversionDate": obj.get("currencyConversionDate"),
            "currencyConversionMode": obj.get("currencyConversionMode"),
            "dateTimeDisplayMode": obj.get("dateTimeDisplayMode"),
            "limit": obj.get("limit"),
            "multipleTables": obj.get("multipleTables"),
            "omitHeader": obj.get("omitHeader"),
            "page": obj.get("page"),
            "queryMode": obj.get("queryMode"),
            "recordMode": obj.get("recordMode")
        })
        return _obj


