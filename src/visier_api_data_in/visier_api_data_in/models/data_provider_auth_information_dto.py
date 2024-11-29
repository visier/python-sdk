# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_data_in.models.data_provider_auth_params_dto import DataProviderAuthParamsDTO
from visier_api_data_in.models.data_provider_basic_information_dto import DataProviderBasicInformationDTO
from visier_api_data_in.models.data_provider_basic_metadata_dto import DataProviderBasicMetadataDTO
from typing import Optional, Set
from typing_extensions import Self

class DataProviderAuthInformationDTO(BaseModel):
    """
    DataProviderAuthInformationDTO
    """ # noqa: E501
    data_provider_auth_params: Optional[DataProviderAuthParamsDTO] = Field(default=None, description="The authentication information for the credential.", alias="dataProviderAuthParams")
    data_provider_basic_information: Optional[DataProviderBasicInformationDTO] = Field(default=None, description="The display name and description for the credential.", alias="dataProviderBasicInformation")
    data_provider_metadata: Optional[DataProviderBasicMetadataDTO] = Field(default=None, alias="dataProviderMetadata")
    __properties: ClassVar[List[str]] = ["dataProviderAuthParams", "dataProviderBasicInformation", "dataProviderMetadata"]

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
        """Create an instance of DataProviderAuthInformationDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of data_provider_auth_params
        if self.data_provider_auth_params:
            _dict['dataProviderAuthParams'] = self.data_provider_auth_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_provider_basic_information
        if self.data_provider_basic_information:
            _dict['dataProviderBasicInformation'] = self.data_provider_basic_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_provider_metadata
        if self.data_provider_metadata:
            _dict['dataProviderMetadata'] = self.data_provider_metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataProviderAuthInformationDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataProviderAuthParams": DataProviderAuthParamsDTO.from_dict(obj["dataProviderAuthParams"]) if obj.get("dataProviderAuthParams") is not None else None,
            "dataProviderBasicInformation": DataProviderBasicInformationDTO.from_dict(obj["dataProviderBasicInformation"]) if obj.get("dataProviderBasicInformation") is not None else None,
            "dataProviderMetadata": DataProviderBasicMetadataDTO.from_dict(obj["dataProviderMetadata"]) if obj.get("dataProviderMetadata") is not None else None
        })
        return _obj


