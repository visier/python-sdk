# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PredictionDTO(BaseModel):
    """
    A prediction is a forecast of future events with advanced machine learning models.
    """ # noqa: E501
    data_end_date: Optional[StrictStr] = Field(default=None, description="The date from which data is no longer available for this prediction.  Note: Format is the number of milliseconds since midnight 01 January, 1970 UTC as a string.  Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON's inherent  limitation in representing large numbers.", alias="dataEndDate")
    data_start_date: Optional[StrictStr] = Field(default=None, description="The date from which data becomes available for this prediction.  Note: Format is the number of milliseconds since midnight 01 January, 1970 UTC as a string.  Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON's inherent  limitation in representing large numbers.", alias="dataStartDate")
    description: Optional[StrictStr] = Field(default=None, description="The localized description of the prediction.")
    display_name: Optional[StrictStr] = Field(default=None, description="The localized display name of the prediction.", alias="displayName")
    event: Optional[StrictStr] = Field(default=None, description="The object name of the event to predict. The prediction's training data uses past occurrences of the event to  make predictions. For example, the Predicted Risk of Resignation model uses the Employee_Exit event to estimate  likelihood of exit from the organization.")
    event_filter: Optional[StrictStr] = Field(default=None, description="The object name of a selection concept to filter event occurrences in the prediction's training data.", alias="eventFilter")
    factor_concepts: Optional[List[StrictStr]] = Field(default=None, description="The list of unique IDs of the concepts used as prediction factors.", alias="factorConcepts")
    factor_dimensions: Optional[List[StrictStr]] = Field(default=None, description="The list of unique IDs of the dimensions used as prediction factors.", alias="factorDimensions")
    factor_properties: Optional[List[StrictStr]] = Field(default=None, description="The list of unique IDs of the properties used as prediction factors.  Note: Factors are conditions used as part of a Visier prediction. For example, Compensation might be a factor in  predicting an individual's risk of resignation. Factors are chosen based on:  - Availability in tenants.  - Prediction impact, such as salary.  - Reducing bias.", alias="factorProperties")
    factors_name: Optional[StrictStr] = Field(default=None, description="The unique name of the factor property. The prediction's formula references the factor property as an object. This is automatically generated.", alias="factorsName")
    id: Optional[StrictStr] = Field(default=None, description="The unique ID of the prediction.  Note: See `Predictions` to get the ID.")
    is_multi_tenant: Optional[StrictBool] = Field(default=None, description="If `true`, this prediction applies to more than one tenant. If \"false\", the prediction only applies to the current tenant.", alias="isMultiTenant")
    label_property: Optional[StrictStr] = Field(default=None, description="The unique ID of the property label for the prediction. This is automatically generated.", alias="labelProperty")
    minimum_training_months: Optional[StrictStr] = Field(default=None, description="The minimum amount of time, in months, to train the prediction model.", alias="minimumTrainingMonths")
    score_name: Optional[StrictStr] = Field(default=None, description="The unique name of the score property.  The prediction's formula references the score property as an object. This is automatically generated.", alias="scoreName")
    subject: Optional[StrictStr] = Field(default=None, description="The object name of the subject that the prediction applies to. For example, Employee.")
    subject_filter: Optional[StrictStr] = Field(default=None, description="The object name of a selection concept to filter the subject population. Filtering the population selects  specific subject members in the prediction's training data. For example, using the isHighPerformer concept will  filter the prediction to only high performing employees.", alias="subjectFilter")
    subject_key: Optional[StrictStr] = Field(default=None, description="The unique ID of the subject's property that the prediction applies to. For example, Employee.EmployeeID.", alias="subjectKey")
    subject_parent_key: Optional[StrictStr] = Field(default=None, description="The unique ID of the reference that connects a subject member to other members. For example, Employee.Direct_Manager.  Note: The `subjectParentKey` defines parent, child, and peer relationships between subject members.", alias="subjectParentKey")
    __properties: ClassVar[List[str]] = ["dataEndDate", "dataStartDate", "description", "displayName", "event", "eventFilter", "factorConcepts", "factorDimensions", "factorProperties", "factorsName", "id", "isMultiTenant", "labelProperty", "minimumTrainingMonths", "scoreName", "subject", "subjectFilter", "subjectKey", "subjectParentKey"]

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
        """Create an instance of PredictionDTO from a JSON string"""
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
        """Create an instance of PredictionDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataEndDate": obj.get("dataEndDate"),
            "dataStartDate": obj.get("dataStartDate"),
            "description": obj.get("description"),
            "displayName": obj.get("displayName"),
            "event": obj.get("event"),
            "eventFilter": obj.get("eventFilter"),
            "factorConcepts": obj.get("factorConcepts"),
            "factorDimensions": obj.get("factorDimensions"),
            "factorProperties": obj.get("factorProperties"),
            "factorsName": obj.get("factorsName"),
            "id": obj.get("id"),
            "isMultiTenant": obj.get("isMultiTenant"),
            "labelProperty": obj.get("labelProperty"),
            "minimumTrainingMonths": obj.get("minimumTrainingMonths"),
            "scoreName": obj.get("scoreName"),
            "subject": obj.get("subject"),
            "subjectFilter": obj.get("subjectFilter"),
            "subjectKey": obj.get("subjectKey"),
            "subjectParentKey": obj.get("subjectParentKey")
        })
        return _obj


