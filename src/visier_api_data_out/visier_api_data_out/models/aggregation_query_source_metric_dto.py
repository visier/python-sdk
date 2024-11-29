# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AggregationQuerySourceMetricDTO(BaseModel):
    """
    The column definition for a single metric within a `metrics` query.
    """ # noqa: E501
    column_name: Optional[StrictStr] = Field(default=None, description="The column name in the CSV file. Default is to use id as the column name.", alias="columnName")
    formula: Optional[StrictStr] = Field(default=None, description="An ad-hoc metric formula. The response returns the results of the aggregate.  See the formula dictionary in Visier to find functions and objects you can use in a formula.")
    id: Optional[StrictStr] = Field(default=None, description="The unique ID of the metric. Note: See `Metrics` to get the ID.  If columnName is omitted, id is the column name in the CSV file.")
    qualifying_path: Optional[StrictStr] = Field(default=None, description="The base qualifying path to prefix the axes and filters' qualifying paths with.  You must specify the qualifying path on a metric if the convergent analytic object of the metric doesn't match the  starting object in the qualifying paths of the axes and filters.   For example, consider a multi-metric query that contains metrics that count the number of applicants and requisitions,  grouped by the country of the recruiter's direct manager. The following sample shows how to use qualifyingPath to specify  the object reference traversal path from each metric's convergent analytic object to the start of the path for the axes.  In this example, there is only one convergent analytic object.  ```  \"source\": {      \"metrics\": {         \"columns\": [             {                 \"id\": \"employeeCount\"             },             {                 \"id\": \"applicantCount\",                 \"qualifyingPath\": \"Applicant.Requisition.Recruiter\"             },             {                 \"id\": \"requisitionCount\",                 \"qualifyingPath\": \"Requisition.Recruiter\"             }         ]     }  },  \"axes\": [     {         \"dimensionLevelSelection\": {             \"dimension\": {                 \"name\": \"Location\",                 \"qualifyingPath\": \"Employee.Direct_Manager\"             },             \"levelIds\": [                 \"Location_1\"             ]         }     }  ]  ```  **Note:**  * `employeeCount` doesn't need a `qualifyingPath` because it's already convergent with the start of the axis path.  * The metrics' qualifying paths must provide the reference name that resolves to the first object of the axis' qualifying path as their last path segment. In this case, Recruiter is a named reference pointing to Employee. The final qualifying paths for the metrics are:      * `employeeCount`: Employee.Direct_Manager      * `applicantCount`: Applicant.Requisition.Recruiter.Direct_Manager      * `requisitionCount`: Requisition.Recruiter.Direct_Manager", alias="qualifyingPath")
    __properties: ClassVar[List[str]] = ["columnName", "formula", "id", "qualifyingPath"]

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
        """Create an instance of AggregationQuerySourceMetricDTO from a JSON string"""
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
        """Create an instance of AggregationQuerySourceMetricDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "columnName": obj.get("columnName"),
            "formula": obj.get("formula"),
            "id": obj.get("id"),
            "qualifyingPath": obj.get("qualifyingPath")
        })
        return _obj


