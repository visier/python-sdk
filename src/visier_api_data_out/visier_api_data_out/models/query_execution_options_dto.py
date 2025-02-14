# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1739
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
from visier_api_data_out.models.cell_distribution_options_dto import CellDistributionOptionsDTO
from visier_api_data_out.models.internal_query_execution_options_dto import InternalQueryExecutionOptionsDTO
from typing import Optional, Set
from typing_extensions import Self

class QueryExecutionOptionsDTO(BaseModel):
    """
    A QueryExecutionOptions provides additional instructions to perform a query.
    """ # noqa: E501
    axes_overall_value_mode: Optional[StrictStr] = Field(default=None, description="If `axes` is defined, use `axesOverallValueMode` to specify the type of overall values to return across the axes. Valid values:   * `NONE`: Returns the metric's values for the selected axes and doesn't return overall values. This is the default.  * `AGGREGATE`: Returns the metric's overall values for the selected axes members.  * `OVERALL`: Returns the metric's overall values for all axes members.   **Note**: `AGGREGATE` is not supported for lookup overlays because the overall values of selected members cannot be calculated directly from the data.   Example: Let's say you want to know the Headcount of the locations Canada and US and the genders Male and Female.    When `axesOverallValueMode` is `NONE`, the query returns these values:  * 100 (Canada, Male)  * 100 (US, Male)  * 100 (Canada, Female)  * 100 (US, Female)    When `axesOverallValueMode` is `AGGREGATE`, the query returns these values:  * 100 (Canada, Male)  * 100 (US, Male)  * 100 (Canada, Female)  * 100 (US, Female)  * 400 (Overall, Overall)  * 200 (Overall, Male)  * 200 (Overall, Female)  * 200 (Canada, Overall)  * 200 (US, Overall)   When `axesOverallValueMode` is `OVERALL`, the query returns these values:  * 100 (Canada, Male)  * 100 (US, Male)  * 100 (Canada, Female)  * 100 (US, Female)  * 800 (Overall, Overall)  * 400 (Overall, Male)  * 400 (Overall, Female)  * 400 (Canada, Overall)  * 400 (US, Overall)    In this example, `OVERALL` returns higher overall values than `AGGREGATE` because `AGGREGATE` returns the overall values for the selected locations (Canada, US) and genders (Male, Female), whereas `OVERALL` returns the overall values across all locations and genders in the data.", alias="axesOverallValueMode")
    axis_visibility: Optional[StrictStr] = Field(default=None, description="The amount of information to return about each axis. Default is SIMPLE.", alias="axisVisibility")
    calendar_type: Optional[StrictStr] = Field(default=None, description="The calendar type to use. This will be used for all time calculations unless explicitly overridden in  the calculation itself. Default is TENANT_CALENDAR.", alias="calendarType")
    cell_distribution_options: Optional[CellDistributionOptionsDTO] = Field(default=None, alias="cellDistributionOptions")
    currency_conversion_code: Optional[StrictStr] = Field(default=None, description="The target currency for all currency conversions.  If not specified, the tenant default currency will be used.", alias="currencyConversionCode")
    currency_conversion_date: Optional[StrictStr] = Field(default=None, description="The currency conversion date to use. If defined, the currency conversion will use the exchange rates as of this date.  Default is the exchange rate at the end of the query time interval. Format is the number of milliseconds since  midnight 01 January, 1970 UTC as a string. Note: Epochs are expressed as 64-bit integers and represented as  stringified longs in JSON due to JSON's inherent limitation in representing large numbers.", alias="currencyConversionDate")
    currency_conversion_mode: Optional[StrictStr] = Field(default=None, description="The currency conversion mode to use. This will be used for all currency conversion calculations  unless explicitly overridden in the calculation itself. Default is TENANT_CURRENCY_CONVERSION.", alias="currencyConversionMode")
    enable_descending_space: Optional[StrictBool] = Field(default=None, description="If true, filter non-time axis member sets to only include members that are in aggregate positions or whose previous position is a leaf", alias="enableDescendingSpace")
    enable_sparse_results: Optional[StrictBool] = Field(default=None, description="Retrieve sparse cell sets. Sparse results only retrieve non-zero and non-null cells. Whether a result is truly sparse  or not is determined by the Visier server.", alias="enableSparseResults")
    internal: Optional[InternalQueryExecutionOptionsDTO] = None
    lineage_depth: Optional[StrictInt] = Field(default=None, description="The max number of levels of nesting to unwind when determining the lineage for a derived metric value.", alias="lineageDepth")
    member_display_mode: Optional[StrictStr] = Field(default=None, description="Control how member values are displayed. You can override the `memberDisplayMode` on a per-axis basis, if required.   Valid values are `DEFAULT`, `COMPACT`, `DISPLAY`, or `MDX`. Default is `DEFAULT`.   * `DEFAULT`: The default member name representation. For non-time members, this returns the technical member name path.    For time members, this includes a bracketed member index.    For example, Time instant member: `2019-06-01T00:00:00.000Z - [0]`    For example, Time interval member: `2022-06-01T00:00:00.000Z/2022-07-01T00:00:00.000Z - [12]`  * `COMPACT`: Shortens the member name representation. For time intervals, the member name is the end time of the interval.     For example, Time instant member: `2019-06-01T00:00:00.000Z`     For example, Time interval member: `2022-07-01T00:00:00.000Z` where the interval member name was `2022-06-01T00:00:00.000Z/2022-07-01T00:00:00.000Z - [12]`  * `DISPLAY`: Emits the members' display names whenever possible. When combined with `axisVisibility = VERBOSE`, the full display name path will be emitted.  * `MDX`: Emits member name paths where each element is enclosed in square brackets, `[]`. Multidimensional expression (MDX) display mode automatically encloses time members in square brackets and puts them in `COMPACT` format.    For example, Location member `North America.United States.California` becomes `[North America].[United States].[California]` in MDX display mode.    For example, Time instant member `2019-06-01T00:00:00.000Z - [0]` becomes `[2019-06-01T00:00:00.000Z]` in MDX display mode.  * `COMPACT_DISPLAY`: Emit the members' display names after compacting. This applies primarily to time members for event-based metrics. Compact display is required when    running multi-metric queries containing both event-based and subject-based metrics. Multi-metric queries with `DISPLAY` mode are changed    automatically to `COMPACT_DISPLAY`.    For example, Time interval member `2022-06-01T00:00:00.000Z/2022-07-01T00:00:00.000Z - [12]` becomes `Jun 30, 2022` in `COMPACT_DISPLAY` mode.    The exact format of the compacted time member display name depends on the the user's locale.", alias="memberDisplayMode")
    null_visibility: Optional[StrictStr] = Field(default=None, description="Show or hide null or N/A values in the result. Default is SHOW.", alias="nullVisibility")
    zero_visibility: Optional[StrictStr] = Field(default=None, description="Show or hide zeros in the result. Default is SHOW.", alias="zeroVisibility")
    __properties: ClassVar[List[str]] = ["axesOverallValueMode", "axisVisibility", "calendarType", "cellDistributionOptions", "currencyConversionCode", "currencyConversionDate", "currencyConversionMode", "enableDescendingSpace", "enableSparseResults", "internal", "lineageDepth", "memberDisplayMode", "nullVisibility", "zeroVisibility"]

    @field_validator('axes_overall_value_mode')
    def axes_overall_value_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NONE', 'AGGREGATE', 'OVERALL']):
            raise ValueError("must be one of enum values ('NONE', 'AGGREGATE', 'OVERALL')")
        return value

    @field_validator('axis_visibility')
    def axis_visibility_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SIMPLE', 'VERBOSE']):
            raise ValueError("must be one of enum values ('SIMPLE', 'VERBOSE')")
        return value

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

    @field_validator('member_display_mode')
    def member_display_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DEFAULT', 'COMPACT', 'DISPLAY', 'MDX', 'COMPACT_DISPLAY']):
            raise ValueError("must be one of enum values ('DEFAULT', 'COMPACT', 'DISPLAY', 'MDX', 'COMPACT_DISPLAY')")
        return value

    @field_validator('null_visibility')
    def null_visibility_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SHOW', 'HIDE', 'ELIMINATE']):
            raise ValueError("must be one of enum values ('SHOW', 'HIDE', 'ELIMINATE')")
        return value

    @field_validator('zero_visibility')
    def zero_visibility_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SHOW', 'HIDE', 'ELIMINATE']):
            raise ValueError("must be one of enum values ('SHOW', 'HIDE', 'ELIMINATE')")
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
        """Create an instance of QueryExecutionOptionsDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cell_distribution_options
        if self.cell_distribution_options:
            _dict['cellDistributionOptions'] = self.cell_distribution_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of internal
        if self.internal:
            _dict['internal'] = self.internal.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QueryExecutionOptionsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "axesOverallValueMode": obj.get("axesOverallValueMode"),
            "axisVisibility": obj.get("axisVisibility"),
            "calendarType": obj.get("calendarType"),
            "cellDistributionOptions": CellDistributionOptionsDTO.from_dict(obj["cellDistributionOptions"]) if obj.get("cellDistributionOptions") is not None else None,
            "currencyConversionCode": obj.get("currencyConversionCode"),
            "currencyConversionDate": obj.get("currencyConversionDate"),
            "currencyConversionMode": obj.get("currencyConversionMode"),
            "enableDescendingSpace": obj.get("enableDescendingSpace"),
            "enableSparseResults": obj.get("enableSparseResults"),
            "internal": InternalQueryExecutionOptionsDTO.from_dict(obj["internal"]) if obj.get("internal") is not None else None,
            "lineageDepth": obj.get("lineageDepth"),
            "memberDisplayMode": obj.get("memberDisplayMode"),
            "nullVisibility": obj.get("nullVisibility"),
            "zeroVisibility": obj.get("zeroVisibility")
        })
        return _obj


