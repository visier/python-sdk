# coding: utf-8

"""
    Visier Data Out APIs

    Visier APIs for getting data out of Visier, such as aggregate data and data version information.

    The version of the OpenAPI document: 22222222.99201.1508
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

from visier_api_data_out.api.vee_api import VeeApi


class TestVeeApi(unittest.TestCase):
    """VeeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VeeApi()

    def tearDown(self) -> None:
        pass

    def test_vee_feedback(self) -> None:
        """Test case for vee_feedback

        Submit Vee feedback
        """
        pass

    def test_vee_question_request(self) -> None:
        """Test case for vee_question_request

        Ask Vee a question
        """
        pass

    def test_vee_sample_questions(self) -> None:
        """Test case for vee_sample_questions

        Retrieve a list of sample questions to ask Vee
        """
        pass


if __name__ == '__main__':
    unittest.main()
