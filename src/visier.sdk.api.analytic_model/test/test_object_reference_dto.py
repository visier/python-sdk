# coding: utf-8

"""
    Visier Analytic Model APIs

    Visier APIs for retrieving and configuring your analytic model in Visier.

    The version of the OpenAPI document: 0.0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.sdk.api.analytic_model.models.object_reference_dto import ObjectReferenceDTO

class TestObjectReferenceDTO(unittest.TestCase):
    """ObjectReferenceDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObjectReferenceDTO:
        """Test ObjectReferenceDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObjectReferenceDTO`
        """
        model = ObjectReferenceDTO()
        if include_optional:
            return ObjectReferenceDTO(
                description = '',
                display_name = '',
                from_object = '',
                id = '',
                is_strong_reference = True,
                to_object = '',
                type = 'SUBJECT_REFERENCE'
            )
        else:
            return ObjectReferenceDTO(
        )
        """

    def testObjectReferenceDTO(self):
        """Test ObjectReferenceDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
