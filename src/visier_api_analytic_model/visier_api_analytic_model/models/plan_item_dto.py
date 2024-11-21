# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 22222222.99201.1598
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
from typing import Optional, Set
from typing_extensions import Self

class PlanItemDTO(BaseModel):
    """
    A plan item is a metric in your plan. The available plan items depend on the planning model.
    """ # noqa: E501
    data_type: Optional[StrictStr] = Field(default=None, description="The data type of the plan item. The data types are:  - rate    - Converts values into a percentage in the planning grid. The provided value is multiplied by 100 to get the display value.      For example, a provided value of 0.5 is displayed as 50% in the grid.  - number    - Displays values as whole numbers. Decimal values are rounded to a whole number when displayed in the planning grid.  - currency    - Displays values as a currency. Values must not contain thousand separators, currency codes, or currency symbols.  - decimal    - Displays values with decimals.", alias="dataType")
    display_name: Optional[StrictStr] = Field(default=None, description="The display name of the plan item.", alias="displayName")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the plan item.")
    __properties: ClassVar[List[str]] = ["dataType", "displayName", "id"]

    @field_validator('data_type')
    def data_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['unknown', 'number', 'currency', 'decimal', 'rate']):
            raise ValueError("must be one of enum values ('unknown', 'number', 'currency', 'decimal', 'rate')")
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
        """Create an instance of PlanItemDTO from a JSON string"""
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
        """Create an instance of PlanItemDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataType": obj.get("dataType"),
            "displayName": obj.get("displayName"),
            "id": obj.get("id")
        })
        return _obj


