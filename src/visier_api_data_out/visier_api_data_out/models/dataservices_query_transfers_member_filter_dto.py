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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier_api_data_out.models.dataservices_common_member_values_dto import DataservicesCommonMemberValuesDTO
from visier_api_data_out.models.dataservices_datamodel_transfers_dimension_reference_dto import DataservicesDatamodelTransfersDimensionReferenceDTO
from typing import Optional, Set
from typing_extensions import Self

class DataservicesQueryTransfersMemberFilterDTO(BaseModel):
    """
    Member filters are dimension member values to filter by in your query. The member filters are  defined within the filters section of a query definition. You can filter by dimension members in  aggregate and list queries.
    """ # noqa: E501
    dimension: Optional[DataservicesDatamodelTransfersDimensionReferenceDTO] = Field(default=None, description="The dimension in which the members belong.")
    values: Optional[DataservicesCommonMemberValuesDTO] = Field(default=None, description="The dimension members to filter by.")
    __properties: ClassVar[List[str]] = ["dimension", "values"]

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
        """Create an instance of DataservicesQueryTransfersMemberFilterDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dimension
        if self.dimension:
            _dict['dimension'] = self.dimension.to_dict()
        # override the default output from pydantic by calling `to_dict()` of values
        if self.values:
            _dict['values'] = self.values.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataservicesQueryTransfersMemberFilterDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dimension": DataservicesDatamodelTransfersDimensionReferenceDTO.from_dict(obj["dimension"]) if obj.get("dimension") is not None else None,
            "values": DataservicesCommonMemberValuesDTO.from_dict(obj["values"]) if obj.get("values") is not None else None
        })
        return _obj


