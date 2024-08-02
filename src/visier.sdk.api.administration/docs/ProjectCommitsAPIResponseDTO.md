# ProjectCommitsAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commits** | [**List[CommitDTO]**](CommitDTO.md) | A list of committed changes in the project. | [optional] 

## Example

```python
from visier.sdk.api.administration.models.project_commits_api_response_dto import ProjectCommitsAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCommitsAPIResponseDTO from a JSON string
project_commits_api_response_dto_instance = ProjectCommitsAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(ProjectCommitsAPIResponseDTO.to_json())

# convert the object into a dict
project_commits_api_response_dto_dict = project_commits_api_response_dto_instance.to_dict()
# create an instance of ProjectCommitsAPIResponseDTO from a dict
project_commits_api_response_dto_from_dict = ProjectCommitsAPIResponseDTO.from_dict(project_commits_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


