# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sib_api_v3_sdk.api_client import ApiClient


class ListsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_contact_to_list(self, list_id, contact_emails, **kwargs):  # noqa: E501
        """Add existing contacts to a list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.add_contact_to_list(list_id, contact_emails, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int list_id: Id of the list (required)
        :param AddContactToList contact_emails: Emails addresses of the contacts (required)
        :return: PostContactInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.add_contact_to_list_with_http_info(list_id, contact_emails, **kwargs)  # noqa: E501
        else:
            (data) = self.add_contact_to_list_with_http_info(list_id, contact_emails, **kwargs)  # noqa: E501
            return data

    def add_contact_to_list_with_http_info(self, list_id, contact_emails, **kwargs):  # noqa: E501
        """Add existing contacts to a list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.add_contact_to_list_with_http_info(list_id, contact_emails, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int list_id: Id of the list (required)
        :param AddContactToList contact_emails: Emails addresses of the contacts (required)
        :return: PostContactInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'contact_emails']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_contact_to_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `add_contact_to_list`")  # noqa: E501
        # verify the required parameter 'contact_emails' is set
        if ('contact_emails' not in params or
                params['contact_emails'] is None):
            raise ValueError("Missing the required parameter `contact_emails` when calling `add_contact_to_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['listId'] = params['list_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contact_emails' in params:
            body_params = params['contact_emails']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/lists/{listId}/contacts/add', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostContactInfo',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_list(self, create_list, **kwargs):  # noqa: E501
        """Create a list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.create_list(create_list, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param CreateList create_list: Values to create a list (required)
        :return: CreateModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.create_list_with_http_info(create_list, **kwargs)  # noqa: E501
        else:
            (data) = self.create_list_with_http_info(create_list, **kwargs)  # noqa: E501
            return data

    def create_list_with_http_info(self, create_list, **kwargs):  # noqa: E501
        """Create a list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.create_list_with_http_info(create_list, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param CreateList create_list: Values to create a list (required)
        :return: CreateModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_list']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_list' is set
        if ('create_list' not in params or
                params['create_list'] is None):
            raise ValueError("Missing the required parameter `create_list` when calling `create_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_list' in params:
            body_params = params['create_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/lists', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateModel',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_list(self, list_id, **kwargs):  # noqa: E501
        """Delete a list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.delete_list(list_id, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int list_id: Id of the list (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.delete_list_with_http_info(list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_list_with_http_info(list_id, **kwargs)  # noqa: E501
            return data

    def delete_list_with_http_info(self, list_id, **kwargs):  # noqa: E501
        """Delete a list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.delete_list_with_http_info(list_id, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int list_id: Id of the list (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `delete_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['listId'] = params['list_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/lists/{listId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_contacts_from_list(self, list_id, **kwargs):  # noqa: E501
        """Get the contacts in a list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_contacts_from_list(list_id, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int list_id: Id of the list (required)
        :param datetime modified_since: Filter (urlencoded) the contacts modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). Prefer to pass your timezone in date-time format for accurate result.
        :param int limit: Number of documents per page
        :param int offset: Index of the first document of the page
        :return: GetContacts
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.get_contacts_from_list_with_http_info(list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_contacts_from_list_with_http_info(list_id, **kwargs)  # noqa: E501
            return data

    def get_contacts_from_list_with_http_info(self, list_id, **kwargs):  # noqa: E501
        """Get the contacts in a list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_contacts_from_list_with_http_info(list_id, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int list_id: Id of the list (required)
        :param datetime modified_since: Filter (urlencoded) the contacts modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). Prefer to pass your timezone in date-time format for accurate result.
        :param int limit: Number of documents per page
        :param int offset: Index of the first document of the page
        :return: GetContacts
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'modified_since', 'limit', 'offset']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_contacts_from_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `get_contacts_from_list`")  # noqa: E501

        if 'limit' in params and params['limit'] > 500:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_contacts_from_list`, must be a value less than or equal to `500`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['listId'] = params['list_id']  # noqa: E501

        query_params = []
        if 'modified_since' in params:
            query_params.append(('modifiedSince', params['modified_since']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/lists/{listId}/contacts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetContacts',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_folder_lists(self, folder_id, **kwargs):  # noqa: E501
        """Get the lists in a folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_folder_lists(folder_id, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int folder_id: Id of the folder (required)
        :param int limit: Number of documents per page
        :param int offset: Index of the first document of the page
        :return: GetFolderLists
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.get_folder_lists_with_http_info(folder_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_folder_lists_with_http_info(folder_id, **kwargs)  # noqa: E501
            return data

    def get_folder_lists_with_http_info(self, folder_id, **kwargs):  # noqa: E501
        """Get the lists in a folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_folder_lists_with_http_info(folder_id, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int folder_id: Id of the folder (required)
        :param int limit: Number of documents per page
        :param int offset: Index of the first document of the page
        :return: GetFolderLists
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_id', 'limit', 'offset']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_folder_lists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_id' is set
        if ('folder_id' not in params or
                params['folder_id'] is None):
            raise ValueError("Missing the required parameter `folder_id` when calling `get_folder_lists`")  # noqa: E501

        if 'limit' in params and params['limit'] > 50:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_folder_lists`, must be a value less than or equal to `50`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'folder_id' in params:
            path_params['folderId'] = params['folder_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/folders/{folderId}/lists', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetFolderLists',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_list(self, list_id, **kwargs):  # noqa: E501
        """Get the details of a list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_list(list_id, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int list_id: Id of the list (required)
        :return: GetExtendedList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.get_list_with_http_info(list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_list_with_http_info(list_id, **kwargs)  # noqa: E501
            return data

    def get_list_with_http_info(self, list_id, **kwargs):  # noqa: E501
        """Get the details of a list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_list_with_http_info(list_id, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int list_id: Id of the list (required)
        :return: GetExtendedList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `get_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['listId'] = params['list_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/lists/{listId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetExtendedList',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_lists(self, **kwargs):  # noqa: E501
        """Get all the lists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_lists(asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int limit: Number of documents per page
        :param int offset: Index of the first document of the page
        :return: GetLists
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.get_lists_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_lists_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_lists_with_http_info(self, **kwargs):  # noqa: E501
        """Get all the lists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.get_lists_with_http_info(asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int limit: Number of documents per page
        :param int offset: Index of the first document of the page
        :return: GetLists
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_lists" % key
                )
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 50:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_lists`, must be a value less than or equal to `50`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/lists', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetLists',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_contact_from_list(self, list_id, contact_emails, **kwargs):  # noqa: E501
        """Remove existing contacts from a list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.remove_contact_from_list(list_id, contact_emails, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int list_id: Id of the list (required)
        :param RemoveContactFromList contact_emails: Emails adresses of the contact (required)
        :return: PostContactInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.remove_contact_from_list_with_http_info(list_id, contact_emails, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_contact_from_list_with_http_info(list_id, contact_emails, **kwargs)  # noqa: E501
            return data

    def remove_contact_from_list_with_http_info(self, list_id, contact_emails, **kwargs):  # noqa: E501
        """Remove existing contacts from a list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.remove_contact_from_list_with_http_info(list_id, contact_emails, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int list_id: Id of the list (required)
        :param RemoveContactFromList contact_emails: Emails adresses of the contact (required)
        :return: PostContactInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'contact_emails']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_contact_from_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `remove_contact_from_list`")  # noqa: E501
        # verify the required parameter 'contact_emails' is set
        if ('contact_emails' not in params or
                params['contact_emails'] is None):
            raise ValueError("Missing the required parameter `contact_emails` when calling `remove_contact_from_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['listId'] = params['list_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contact_emails' in params:
            body_params = params['contact_emails']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/lists/{listId}/contacts/remove', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostContactInfo',  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_list(self, list_id, update_list, **kwargs):  # noqa: E501
        """Update a list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.update_list(list_id, update_list, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int list_id: Id of the list (required)
        :param UpdateList update_list: Values to update a list (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('asynchronous'):
            return self.update_list_with_http_info(list_id, update_list, **kwargs)  # noqa: E501
        else:
            (data) = self.update_list_with_http_info(list_id, update_list, **kwargs)  # noqa: E501
            return data

    def update_list_with_http_info(self, list_id, update_list, **kwargs):  # noqa: E501
        """Update a list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass asynchronous=True
        >>> thread = api.update_list_with_http_info(list_id, update_list, asynchronous=True)
        >>> result = thread.get()

        :param asynchronous bool
        :param int list_id: Id of the list (required)
        :param UpdateList update_list: Values to update a list (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'update_list']  # noqa: E501
        all_params.append('asynchronous')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `update_list`")  # noqa: E501
        # verify the required parameter 'update_list' is set
        if ('update_list' not in params or
                params['update_list'] is None):
            raise ValueError("Missing the required parameter `update_list` when calling `update_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['listId'] = params['list_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_list' in params:
            body_params = params['update_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/lists/{listId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            asynchronous=params.get('asynchronous'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
