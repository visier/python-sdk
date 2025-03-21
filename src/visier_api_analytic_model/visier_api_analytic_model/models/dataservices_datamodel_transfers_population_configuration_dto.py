# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_analytic_model.models.dataservices_datamodel_transfers_dimension_reference_dto import DataservicesDatamodelTransfersDimensionReferenceDTO
from visier_api_analytic_model.models.dataservices_datamodel_transfers_property_reference_dto import DataservicesDatamodelTransfersPropertyReferenceDTO
from typing import Optional, Set
from typing_extensions import Self

class DataservicesDatamodelTransfersPopulationConfigurationDTO(BaseModel):
    """
    A set of property and dimension references configured by Visier or an administrator to tell the platform what  properties and dimensions to use when doing population insight calculations. These are the distinguishing properties,  change history properties, and grouping dimensions to use in AI insights.
    """ # noqa: E501
    change_history_properties: Optional[List[DataservicesDatamodelTransfersPropertyReferenceDTO]] = Field(default=None, description="Properties that are used by default to compare subject members over time.", alias="changeHistoryProperties")
    distinguishing_properties: Optional[List[DataservicesDatamodelTransfersPropertyReferenceDTO]] = Field(default=None, description="Properties that are used by default to compare subject members.", alias="distinguishingProperties")
    grouping_dimensions: Optional[List[DataservicesDatamodelTransfersDimensionReferenceDTO]] = Field(default=None, description="Dimensions to use for grouping and clustering the population.", alias="groupingDimensions")
    __properties: ClassVar[List[str]] = ["changeHistoryProperties", "distinguishingProperties", "groupingDimensions"]

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
        """Create an instance of DataservicesDatamodelTransfersPopulationConfigurationDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in change_history_properties (list)
        _items = []
        if self.change_history_properties:
            for _item_change_history_properties in self.change_history_properties:
                if _item_change_history_properties:
                    _items.append(_item_change_history_properties.to_dict())
            _dict['changeHistoryProperties'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in distinguishing_properties (list)
        _items = []
        if self.distinguishing_properties:
            for _item_distinguishing_properties in self.distinguishing_properties:
                if _item_distinguishing_properties:
                    _items.append(_item_distinguishing_properties.to_dict())
            _dict['distinguishingProperties'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in grouping_dimensions (list)
        _items = []
        if self.grouping_dimensions:
            for _item_grouping_dimensions in self.grouping_dimensions:
                if _item_grouping_dimensions:
                    _items.append(_item_grouping_dimensions.to_dict())
            _dict['groupingDimensions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataservicesDatamodelTransfersPopulationConfigurationDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "changeHistoryProperties": [DataservicesDatamodelTransfersPropertyReferenceDTO.from_dict(_item) for _item in obj["changeHistoryProperties"]] if obj.get("changeHistoryProperties") is not None else None,
            "distinguishingProperties": [DataservicesDatamodelTransfersPropertyReferenceDTO.from_dict(_item) for _item in obj["distinguishingProperties"]] if obj.get("distinguishingProperties") is not None else None,
            "groupingDimensions": [DataservicesDatamodelTransfersDimensionReferenceDTO.from_dict(_item) for _item in obj["groupingDimensions"]] if obj.get("groupingDimensions") is not None else None
        })
        return _obj


