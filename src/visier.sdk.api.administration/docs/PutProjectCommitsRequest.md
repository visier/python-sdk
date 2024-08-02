# PutProjectCommitsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The unique identifier of the draft project you want to import committed changes into. | [optional] 

## Example

```python
from visier.sdk.api.administration.models.put_project_commits_request import PutProjectCommitsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutProjectCommitsRequest from a JSON string
put_project_commits_request_instance = PutProjectCommitsRequest.from_json(json)
# print the JSON string representation of the object
print(PutProjectCommitsRequest.to_json())

# convert the object into a dict
put_project_commits_request_dict = put_project_commits_request_instance.to_dict()
# create an instance of PutProjectCommitsRequest from a dict
put_project_commits_request_from_dict = PutProjectCommitsRequest.from_dict(put_project_commits_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


