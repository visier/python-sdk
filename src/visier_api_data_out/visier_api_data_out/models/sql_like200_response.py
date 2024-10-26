# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1547
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from visier_api_data_out.models.cell_set_dto import CellSetDTO
from visier_api_data_out.models.table_response_dto import TableResponseDTO
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict, ClassVar
from typing_extensions import Literal, Self

SQLLIKE200RESPONSE_ONE_OF_SCHEMAS = ["CellSetDTO", "TableResponseDTO"]

class SqlLike200Response(BaseModel):
    """
    SqlLike200Response
    """
    # data type: TableResponseDTO
    oneof_schema_1_validator: Optional[TableResponseDTO] = None
    # data type: CellSetDTO
    oneof_schema_2_validator: Optional[CellSetDTO] = None
    actual_instance: Optional[Union[CellSetDTO, TableResponseDTO]] = None
    one_of_schemas: Set[str] = { "CellSetDTO", "TableResponseDTO" }
    _default_values: ClassVar[Dict[str, Any]]  = { "CellSetDTO": CellSetDTO(), "TableResponseDTO": TableResponseDTO() }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = SqlLike200Response.model_construct()
        error_messages = []
        match = 0
        # validate data type: TableResponseDTO
        if not isinstance(v, TableResponseDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TableResponseDTO`")
        else:
            match += 1
        # validate data type: CellSetDTO
        if not isinstance(v, CellSetDTO):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CellSetDTO`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in SqlLike200Response with oneOf schemas: CellSetDTO, TableResponseDTO. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in SqlLike200Response with oneOf schemas: CellSetDTO, TableResponseDTO. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into TableResponseDTO
        try:
            actual_instance = TableResponseDTO.from_json(json_str)
            if actual_instance and actual_instance != cls._default_values[TableResponseDTO.__name__]:
                instance.actual_instance = actual_instance
                match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CellSetDTO
        try:
            actual_instance = CellSetDTO.from_json(json_str)
            if actual_instance and actual_instance != cls._default_values[CellSetDTO.__name__]:
                instance.actual_instance = actual_instance
                match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into SqlLike200Response with oneOf schemas: CellSetDTO, TableResponseDTO. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into SqlLike200Response with oneOf schemas: CellSetDTO, TableResponseDTO. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], CellSetDTO, TableResponseDTO]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


