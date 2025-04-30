# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1876
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
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_basic_information_dto import ServicingV2ObjectconfigurationBasicInformationDTO
from visier_api_analytic_model.models.servicing_v2_objectconfiguration_property_type_details_dto import ServicingV2ObjectconfigurationPropertyTypeDetailsDTO
from typing import Optional, Set
from typing_extensions import Self

class ServicingV2ObjectconfigurationPropertyDefinitionDTO(BaseModel):
    """
    ServicingV2ObjectconfigurationPropertyDefinitionDTO
    """ # noqa: E501
    uuid: Optional[StrictStr] = Field(default=None, description="The UUID identifying the property.")
    object_name: Optional[StrictStr] = Field(default=None, description="The object name of the property.", alias="objectName")
    basic_information: Optional[ServicingV2ObjectconfigurationBasicInformationDTO] = Field(default=None, description="Fields that identify and describe the property, such as its display name, description, and explanation.", alias="basicInformation")
    details: Optional[ServicingV2ObjectconfigurationPropertyTypeDetailsDTO] = Field(default=None, description="The property type and its details.")
    __properties: ClassVar[List[str]] = ["uuid", "objectName", "basicInformation", "details"]

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
        """Create an instance of ServicingV2ObjectconfigurationPropertyDefinitionDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of basic_information
        if self.basic_information:
            _dict['basicInformation'] = self.basic_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of details
        if self.details:
            _dict['details'] = self.details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServicingV2ObjectconfigurationPropertyDefinitionDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "objectName": obj.get("objectName"),
            "basicInformation": ServicingV2ObjectconfigurationBasicInformationDTO.from_dict(obj["basicInformation"]) if obj.get("basicInformation") is not None else None,
            "details": ServicingV2ObjectconfigurationPropertyTypeDetailsDTO.from_dict(obj["details"]) if obj.get("details") is not None else None
        })
        return _obj


