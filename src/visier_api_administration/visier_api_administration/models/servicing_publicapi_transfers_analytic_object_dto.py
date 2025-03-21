# coding: utf-8

"""
    Visier Administration APIs

    Visier APIs for managing your tenant or tenants in Visier. You can programmatically manage user accounts in Visier, the profiles and permissions assigned to users, and to make changes in projects and publish projects to production. Administrating tenant users can use administration APIs to manage their analytic tenants and consolidated analytics tenants.<br>**Note:** If you submit API requests for changes that cause a project to publish to production (such as assigning permissions to users or updating permissions), each request is individually published to production, resulting in hundreds or thousands of production versions. We recommend that you use the `ProjectID` request header to make changes in a project, if `ProjectID` is available for the API endpoint.

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
from visier_api_administration.models.servicing_publicapi_transfers_related_analytic_object_dto import ServicingPublicapiTransfersRelatedAnalyticObjectDTO
from visier_api_administration.models.servicing_publicapi_transfers_securable_dimension_dto import ServicingPublicapiTransfersSecurableDimensionDTO
from visier_api_administration.models.servicing_publicapi_transfers_securable_property_dto import ServicingPublicapiTransfersSecurablePropertyDTO
from typing import Optional, Set
from typing_extensions import Self

class ServicingPublicapiTransfersAnalyticObjectDTO(BaseModel):
    """
    ServicingPublicapiTransfersAnalyticObjectDTO
    """ # noqa: E501
    analytic_object_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the analytic object.", alias="analyticObjectId")
    display_name: Optional[StrictStr] = Field(default=None, description="An identifiable name to display in Visier, such as \"Employee\".", alias="displayName")
    object_type: Optional[StrictStr] = Field(default=None, description="The analytic object type.", alias="objectType")
    related_objects: Optional[List[ServicingPublicapiTransfersRelatedAnalyticObjectDTO]] = Field(default=None, description="The analytic objects related to the data security object.", alias="relatedObjects")
    securable_dimensions: Optional[List[ServicingPublicapiTransfersSecurableDimensionDTO]] = Field(default=None, description="A list of dimensions that are available to define population access filters in the permission.", alias="securableDimensions")
    securable_properties: Optional[List[ServicingPublicapiTransfersSecurablePropertyDTO]] = Field(default=None, description="All available properties from the data security object and its related analytic objects that you can configure data access for.", alias="securableProperties")
    __properties: ClassVar[List[str]] = ["analyticObjectId", "displayName", "objectType", "relatedObjects", "securableDimensions", "securableProperties"]

    @field_validator('object_type')
    def object_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Event', 'Subject', 'BusinessOutcomeOverlay', 'PlanOrBudgetOverlay', 'ExternalBenchmark', 'VisierBenchmark', 'UsageOverlay', 'OtherOverlay', 'InternalComparison', 'PlanAnalyticObject']):
            raise ValueError("must be one of enum values ('Event', 'Subject', 'BusinessOutcomeOverlay', 'PlanOrBudgetOverlay', 'ExternalBenchmark', 'VisierBenchmark', 'UsageOverlay', 'OtherOverlay', 'InternalComparison', 'PlanAnalyticObject')")
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
        """Create an instance of ServicingPublicapiTransfersAnalyticObjectDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in related_objects (list)
        _items = []
        if self.related_objects:
            for _item_related_objects in self.related_objects:
                if _item_related_objects:
                    _items.append(_item_related_objects.to_dict())
            _dict['relatedObjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in securable_dimensions (list)
        _items = []
        if self.securable_dimensions:
            for _item_securable_dimensions in self.securable_dimensions:
                if _item_securable_dimensions:
                    _items.append(_item_securable_dimensions.to_dict())
            _dict['securableDimensions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in securable_properties (list)
        _items = []
        if self.securable_properties:
            for _item_securable_properties in self.securable_properties:
                if _item_securable_properties:
                    _items.append(_item_securable_properties.to_dict())
            _dict['securableProperties'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServicingPublicapiTransfersAnalyticObjectDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "analyticObjectId": obj.get("analyticObjectId"),
            "displayName": obj.get("displayName"),
            "objectType": obj.get("objectType"),
            "relatedObjects": [ServicingPublicapiTransfersRelatedAnalyticObjectDTO.from_dict(_item) for _item in obj["relatedObjects"]] if obj.get("relatedObjects") is not None else None,
            "securableDimensions": [ServicingPublicapiTransfersSecurableDimensionDTO.from_dict(_item) for _item in obj["securableDimensions"]] if obj.get("securableDimensions") is not None else None,
            "securableProperties": [ServicingPublicapiTransfersSecurablePropertyDTO.from_dict(_item) for _item in obj["securableProperties"]] if obj.get("securableProperties") is not None else None
        })
        return _obj


