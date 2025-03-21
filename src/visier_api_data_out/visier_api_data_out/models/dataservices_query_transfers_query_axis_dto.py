# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1793
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
from visier_api_data_out.models.dataservices_datamodel_transfers_selection_concept_reference_dto import DataservicesDatamodelTransfersSelectionConceptReferenceDTO
from visier_api_data_out.models.dataservices_query_transfers_query_axis_options_dto import DataservicesQueryTransfersQueryAxisOptionsDTO
from visier_api_data_out.models.dataservices_query_transfers_query_dimension_data_member_selection_dto import DataservicesQueryTransfersQueryDimensionDataMemberSelectionDTO
from visier_api_data_out.models.dataservices_query_transfers_query_dimension_leaf_selection_dto import DataservicesQueryTransfersQueryDimensionLeafSelectionDTO
from visier_api_data_out.models.dataservices_query_transfers_query_dimension_level_selection_dto import DataservicesQueryTransfersQueryDimensionLevelSelectionDTO
from visier_api_data_out.models.dataservices_query_transfers_query_dimension_member_selection_dto import DataservicesQueryTransfersQueryDimensionMemberSelectionDTO
from visier_api_data_out.models.dataservices_query_transfers_query_member_map_selection_dto import DataservicesQueryTransfersQueryMemberMapSelectionDTO
from visier_api_data_out.models.dataservices_query_transfers_query_numeric_ranges_dto import DataservicesQueryTransfersQueryNumericRangesDTO
from typing import Optional, Set
from typing_extensions import Self

class DataservicesQueryTransfersQueryAxisDTO(BaseModel):
    """
    An axis of a query used to group data points.
    """ # noqa: E501
    dimension_data_member_selection: Optional[DataservicesQueryTransfersQueryDimensionDataMemberSelectionDTO] = Field(default=None, description="An axis comprised of all leaf, including data, members of an existing dimension in Visier.", alias="dimensionDataMemberSelection")
    dimension_leaf_member_selection: Optional[DataservicesQueryTransfersQueryDimensionLeafSelectionDTO] = Field(default=None, description="An axis comprised of all non-data leaf members of an existing dimension in Visier.", alias="dimensionLeafMemberSelection")
    dimension_level_selection: Optional[DataservicesQueryTransfersQueryDimensionLevelSelectionDTO] = Field(default=None, description="An axis that uses levels of existing dimensions in Visier.", alias="dimensionLevelSelection")
    dimension_level_with_uncategorized_value_selection: Optional[DataservicesQueryTransfersQueryDimensionLevelSelectionDTO] = Field(default=None, description="An axis that uses existing dimension levels in Visier, including uncategorized levels.", alias="dimensionLevelWithUncategorizedValueSelection")
    dimension_member_selection: Optional[DataservicesQueryTransfersQueryDimensionMemberSelectionDTO] = Field(default=None, description="An axis that uses existing dimension members in Visier.", alias="dimensionMemberSelection")
    formula: Optional[StrictStr] = Field(default=None, description="An axis expressed as a formula.")
    member_map_selection: Optional[DataservicesQueryTransfersQueryMemberMapSelectionDTO] = Field(default=None, description="An axis that uses an existing member map in Visier.", alias="memberMapSelection")
    numeric_ranges: Optional[DataservicesQueryTransfersQueryNumericRangesDTO] = Field(default=None, description="An axis that uses an existing range dimension in Visier and defines the ranges to query.", alias="numericRanges")
    selection_concept: Optional[DataservicesDatamodelTransfersSelectionConceptReferenceDTO] = Field(default=None, description="An axis that uses an existing selection concept in Visier.  The resulting axis consists of 3 positions: True, False, and Unknown.", alias="selectionConcept")
    table_axis_options: Optional[DataservicesQueryTransfersQueryAxisOptionsDTO] = Field(default=None, description="Additional transformations to perform on this axis. Only available when the Accept header is a table format, such as text/csv or application/jsonlines.", alias="tableAxisOptions")
    __properties: ClassVar[List[str]] = ["dimensionDataMemberSelection", "dimensionLeafMemberSelection", "dimensionLevelSelection", "dimensionLevelWithUncategorizedValueSelection", "dimensionMemberSelection", "formula", "memberMapSelection", "numericRanges", "selectionConcept", "tableAxisOptions"]

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
        """Create an instance of DataservicesQueryTransfersQueryAxisDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dimension_data_member_selection
        if self.dimension_data_member_selection:
            _dict['dimensionDataMemberSelection'] = self.dimension_data_member_selection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dimension_leaf_member_selection
        if self.dimension_leaf_member_selection:
            _dict['dimensionLeafMemberSelection'] = self.dimension_leaf_member_selection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dimension_level_selection
        if self.dimension_level_selection:
            _dict['dimensionLevelSelection'] = self.dimension_level_selection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dimension_level_with_uncategorized_value_selection
        if self.dimension_level_with_uncategorized_value_selection:
            _dict['dimensionLevelWithUncategorizedValueSelection'] = self.dimension_level_with_uncategorized_value_selection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dimension_member_selection
        if self.dimension_member_selection:
            _dict['dimensionMemberSelection'] = self.dimension_member_selection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of member_map_selection
        if self.member_map_selection:
            _dict['memberMapSelection'] = self.member_map_selection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of numeric_ranges
        if self.numeric_ranges:
            _dict['numericRanges'] = self.numeric_ranges.to_dict()
        # override the default output from pydantic by calling `to_dict()` of selection_concept
        if self.selection_concept:
            _dict['selectionConcept'] = self.selection_concept.to_dict()
        # override the default output from pydantic by calling `to_dict()` of table_axis_options
        if self.table_axis_options:
            _dict['tableAxisOptions'] = self.table_axis_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataservicesQueryTransfersQueryAxisDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dimensionDataMemberSelection": DataservicesQueryTransfersQueryDimensionDataMemberSelectionDTO.from_dict(obj["dimensionDataMemberSelection"]) if obj.get("dimensionDataMemberSelection") is not None else None,
            "dimensionLeafMemberSelection": DataservicesQueryTransfersQueryDimensionLeafSelectionDTO.from_dict(obj["dimensionLeafMemberSelection"]) if obj.get("dimensionLeafMemberSelection") is not None else None,
            "dimensionLevelSelection": DataservicesQueryTransfersQueryDimensionLevelSelectionDTO.from_dict(obj["dimensionLevelSelection"]) if obj.get("dimensionLevelSelection") is not None else None,
            "dimensionLevelWithUncategorizedValueSelection": DataservicesQueryTransfersQueryDimensionLevelSelectionDTO.from_dict(obj["dimensionLevelWithUncategorizedValueSelection"]) if obj.get("dimensionLevelWithUncategorizedValueSelection") is not None else None,
            "dimensionMemberSelection": DataservicesQueryTransfersQueryDimensionMemberSelectionDTO.from_dict(obj["dimensionMemberSelection"]) if obj.get("dimensionMemberSelection") is not None else None,
            "formula": obj.get("formula"),
            "memberMapSelection": DataservicesQueryTransfersQueryMemberMapSelectionDTO.from_dict(obj["memberMapSelection"]) if obj.get("memberMapSelection") is not None else None,
            "numericRanges": DataservicesQueryTransfersQueryNumericRangesDTO.from_dict(obj["numericRanges"]) if obj.get("numericRanges") is not None else None,
            "selectionConcept": DataservicesDatamodelTransfersSelectionConceptReferenceDTO.from_dict(obj["selectionConcept"]) if obj.get("selectionConcept") is not None else None,
            "tableAxisOptions": DataservicesQueryTransfersQueryAxisOptionsDTO.from_dict(obj["tableAxisOptions"]) if obj.get("tableAxisOptions") is not None else None
        })
        return _obj


