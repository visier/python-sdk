# coding: utf-8

"""
    API Reference

    Detailed API reference documentation for Visier APIs. Includes all endpoints, headers, path parameters, query parameters, request body schema, response schema, JSON request samples, and JSON response samples.

    The version of the OpenAPI document: 22222222.99201.2050
    Contact: alpine@visier.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from visier_platform_sdk.models.plan_patch_consolidate_action_request import PlanPatchConsolidateActionRequest
from visier_platform_sdk.models.plan_patch_reopen_action_request import PlanPatchReopenActionRequest
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

PLANPATCHREQUEST_ONE_OF_SCHEMAS = ["PlanPatchConsolidateActionRequest", "PlanPatchReopenActionRequest"]

class PlanPatchRequest(BaseModel):
    """
    If reopening a subplan, this is the subplan to update. If consolidating subplans, this is the main plan to update.
    """
    # data type: PlanPatchConsolidateActionRequest
    oneof_schema_1_validator: Optional[PlanPatchConsolidateActionRequest] = None
    # data type: PlanPatchReopenActionRequest
    oneof_schema_2_validator: Optional[PlanPatchReopenActionRequest] = None
    actual_instance: Optional[Union[PlanPatchConsolidateActionRequest, PlanPatchReopenActionRequest]] = None
    one_of_schemas: Set[str] = { "PlanPatchConsolidateActionRequest", "PlanPatchReopenActionRequest" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

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
        instance = PlanPatchRequest.model_construct()
        error_messages = []
        match = 0
        # validate data type: PlanPatchConsolidateActionRequest
        if not isinstance(v, PlanPatchConsolidateActionRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PlanPatchConsolidateActionRequest`")
        else:
            match += 1
        # validate data type: PlanPatchReopenActionRequest
        if not isinstance(v, PlanPatchReopenActionRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PlanPatchReopenActionRequest`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in PlanPatchRequest with oneOf schemas: PlanPatchConsolidateActionRequest, PlanPatchReopenActionRequest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in PlanPatchRequest with oneOf schemas: PlanPatchConsolidateActionRequest, PlanPatchReopenActionRequest. Details: " + ", ".join(error_messages))
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

        # deserialize data into PlanPatchConsolidateActionRequest
        try:
            instance.actual_instance = PlanPatchConsolidateActionRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PlanPatchReopenActionRequest
        try:
            instance.actual_instance = PlanPatchReopenActionRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into PlanPatchRequest with oneOf schemas: PlanPatchConsolidateActionRequest, PlanPatchReopenActionRequest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into PlanPatchRequest with oneOf schemas: PlanPatchConsolidateActionRequest, PlanPatchReopenActionRequest. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], PlanPatchConsolidateActionRequest, PlanPatchReopenActionRequest]]:
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


