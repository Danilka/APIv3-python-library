# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import sib_api_v3_sdk
from sib_api_v3_sdk.api.reseller_api import ResellerApi  # noqa: E501
from sib_api_v3_sdk.rest import ApiException


class TestResellerApi(unittest.TestCase):
    """ResellerApi unit test stubs"""

    def setUp(self):
        self.api = sib_api_v3_sdk.api.reseller_api.ResellerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_credits(self):
        """Test case for add_credits

        Add Email and/or SMS credits to a specific child account  # noqa: E501
        """
        pass

    def test_associate_ip_to_child(self):
        """Test case for associate_ip_to_child

        Associate a dedicated IP to the child  # noqa: E501
        """
        pass

    def test_create_reseller_child(self):
        """Test case for create_reseller_child

        Creates a reseller child  # noqa: E501
        """
        pass

    def test_delete_reseller_child(self):
        """Test case for delete_reseller_child

        Deletes a single reseller child based on the childAuthKey supplied  # noqa: E501
        """
        pass

    def test_dissociate_ip_from_child(self):
        """Test case for dissociate_ip_from_child

        Dissociate a dedicated IP to the child  # noqa: E501
        """
        pass

    def test_get_child_info(self):
        """Test case for get_child_info

        Gets the info about a specific child account  # noqa: E501
        """
        pass

    def test_get_reseller_childs(self):
        """Test case for get_reseller_childs

        Gets the list of all reseller's children accounts  # noqa: E501
        """
        pass

    def test_remove_credits(self):
        """Test case for remove_credits

        Remove Email and/or SMS credits from a specific child account  # noqa: E501
        """
        pass

    def test_update_reseller_child(self):
        """Test case for update_reseller_child

        Updates infos of reseller's child based on the childAuthKey supplied  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
