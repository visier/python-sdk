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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_analytic_model.models.dataservices_datamodel_transfers_object_reference_dto import DataservicesDatamodelTransfersObjectReferenceDTO
from visier_api_analytic_model.models.dataservices_datamodel_transfers_population_configuration_dto import DataservicesDatamodelTransfersPopulationConfigurationDTO
from typing import Optional, Set
from typing_extensions import Self

class DataservicesDatamodelTransfersAnalyticObjectDTO(BaseModel):
    """
    Analytic objects are the various items that users can analyze in Visier. Analytic objects include subjects, events, and overlays.
    """ # noqa: E501
    data_end_date: Optional[StrictStr] = Field(default=None, description="The date from which data is no longer available for this analytic object.  Note: Format is the number of milliseconds since midnight 01 January, 1970 UTC as a string.  Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON's inherent  limitation in representing large numbers.", alias="dataEndDate")
    data_start_date: Optional[StrictStr] = Field(default=None, description="The date from which data becomes available for this analytic object.  Note: Format is the number of milliseconds since midnight 01 January, 1970 UTC as a string.  Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON's inherent  limitation in representing large numbers.", alias="dataStartDate")
    description: Optional[StrictStr] = Field(default=None, description="The localized description of the analytic object.")
    dimension_ids: Optional[List[StrictStr]] = Field(default=None, description="A list of strings representing IDs of the dimensions that belong to this analytic object.", alias="dimensionIds")
    display_name: Optional[StrictStr] = Field(default=None, description="The localized display name of the analytic object.", alias="displayName")
    id: Optional[StrictStr] = Field(default=None, description="The unique ID of the analytic object.  Note: See `AnalyticObjects` to get the ID.")
    object_references: Optional[List[DataservicesDatamodelTransfersObjectReferenceDTO]] = Field(default=None, description="A list of references from this analytic object to other analytic objects.  Note: If there are no references, this field is omitted.", alias="objectReferences")
    population_configuration: Optional[DataservicesDatamodelTransfersPopulationConfigurationDTO] = Field(default=None, description="A set of property and dimension references configured by Visier or an administrator to tell the platform what  properties and dimensions to use when doing population insight calculations. These are the distinguishing  properties, change history properties, and grouping dimensions to use in AI insights. This field is optional and  is only available for subjects.", alias="populationConfiguration")
    property_ids: Optional[List[StrictStr]] = Field(default=None, description="A list of strings representing IDs of the properties that belong to this analytic object.", alias="propertyIds")
    selection_concept_ids: Optional[List[StrictStr]] = Field(default=None, description="A list of strings representing IDs of the selection concepts that belong to this analytic object.  Note: If there are no selection concepts, this field is omitted.", alias="selectionConceptIds")
    type: Optional[StrictStr] = Field(default=None, description="The analytic object type: SUBJECT, EVENT, or OVERLAY.")
    __properties: ClassVar[List[str]] = ["dataEndDate", "dataStartDate", "description", "dimensionIds", "displayName", "id", "objectReferences", "populationConfiguration", "propertyIds", "selectionConceptIds", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SUBJECT', 'EVENT', 'OVERLAY']):
            raise ValueError("must be one of enum values ('SUBJECT', 'EVENT', 'OVERLAY')")
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
        """Create an instance of DataservicesDatamodelTransfersAnalyticObjectDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in object_references (list)
        _items = []
        if self.object_references:
            for _item_object_references in self.object_references:
                if _item_object_references:
                    _items.append(_item_object_references.to_dict())
            _dict['objectReferences'] = _items
        # override the default output from pydantic by calling `to_dict()` of population_configuration
        if self.population_configuration:
            _dict['populationConfiguration'] = self.population_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataservicesDatamodelTransfersAnalyticObjectDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataEndDate": obj.get("dataEndDate"),
            "dataStartDate": obj.get("dataStartDate"),
            "description": obj.get("description"),
            "dimensionIds": obj.get("dimensionIds"),
            "displayName": obj.get("displayName"),
            "id": obj.get("id"),
            "objectReferences": [DataservicesDatamodelTransfersObjectReferenceDTO.from_dict(_item) for _item in obj["objectReferences"]] if obj.get("objectReferences") is not None else None,
            "populationConfiguration": DataservicesDatamodelTransfersPopulationConfigurationDTO.from_dict(obj["populationConfiguration"]) if obj.get("populationConfiguration") is not None else None,
            "propertyIds": obj.get("propertyIds"),
            "selectionConceptIds": obj.get("selectionConceptIds"),
            "type": obj.get("type")
        })
        return _obj


