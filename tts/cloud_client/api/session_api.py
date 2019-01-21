# coding: utf-8

"""
    SessionService documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloud_client.cloud_api_client import CloudApiClient


class SessionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = CloudApiClient()
        self.api_client = api_client

    def check(self, x_session_id, **kwargs):  # noqa: E501
        """Check session state  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.check(x_session_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_session_id: Session identifier (required)
        :return: AuthStatusDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.check_with_http_info(x_session_id, **kwargs)  # noqa: E501
        else:
            (data) = self.check_with_http_info(x_session_id, **kwargs)  # noqa: E501
            return data

    def check_with_http_info(self, x_session_id, **kwargs):  # noqa: E501
        """Check session state  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.check_with_http_info(x_session_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_session_id: Session identifier (required)
        :return: AuthStatusDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_id' is set
        if ('x_session_id' not in params or
                params['x_session_id'] is None):
            raise ValueError("Missing the required parameter `x_session_id` when calling `check`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_session_id' in params:
            header_params['X-Session-ID'] = params['x_session_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vksession/rest/session', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthStatusDto',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_domains(self, **kwargs):  # noqa: E501
        """Get All domains for auth without session  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_domains(async=True)
        >>> result = thread.get()

        :param async bool
        :return: DomainDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_domains_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_domains_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_domains_with_http_info(self, **kwargs):  # noqa: E501
        """Get All domains for auth without session  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_domains_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: DomainDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_domains" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vksession/rest/domains', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainDto',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_granted_privileges(self, x_session_id, body, **kwargs):  # noqa: E501
        """Get current user privileges  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_granted_privileges(x_session_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_session_id: Session identifier (required)
        :param ModuleNamesDto body: Module names (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_granted_privileges_with_http_info(x_session_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.get_granted_privileges_with_http_info(x_session_id, body, **kwargs)  # noqa: E501
            return data

    def get_granted_privileges_with_http_info(self, x_session_id, body, **kwargs):  # noqa: E501
        """Get current user privileges  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_granted_privileges_with_http_info(x_session_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_session_id: Session identifier (required)
        :param ModuleNamesDto body: Module names (required)
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_granted_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_id' is set
        if ('x_session_id' not in params or
                params['x_session_id'] is None):
            raise ValueError("Missing the required parameter `x_session_id` when calling `get_granted_privileges`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_granted_privileges`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_session_id' in params:
            header_params['X-Session-ID'] = params['x_session_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vksession/rest/privileges', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def login(self, credentials, **kwargs):  # noqa: E501
        """Log in to system and obtain session identifier. Pass sessionId in &#39;X-Session-ID&#39; header in all other API requests  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.login(credentials, async=True)
        >>> result = thread.get()

        :param async bool
        :param AuthRequestDto credentials: User's credentials (required)
        :return: AuthResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.login_with_http_info(credentials, **kwargs)  # noqa: E501
        else:
            (data) = self.login_with_http_info(credentials, **kwargs)  # noqa: E501
            return data

    def login_with_http_info(self, credentials, **kwargs):  # noqa: E501
        """Log in to system and obtain session identifier. Pass sessionId in &#39;X-Session-ID&#39; header in all other API requests  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.login_with_http_info(credentials, async=True)
        >>> result = thread.get()

        :param async bool
        :param AuthRequestDto credentials: User's credentials (required)
        :return: AuthResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credentials']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credentials' is set
        if ('credentials' not in params or
                params['credentials'] is None):
            raise ValueError("Missing the required parameter `credentials` when calling `login`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'credentials' in params:
            body_params = params['credentials']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vksession/rest/session', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def logout(self, x_session_id, **kwargs):  # noqa: E501
        """Log out of system  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.logout(x_session_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_session_id: Session identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.logout_with_http_info(x_session_id, **kwargs)  # noqa: E501
        else:
            (data) = self.logout_with_http_info(x_session_id, **kwargs)  # noqa: E501
            return data

    def logout_with_http_info(self, x_session_id, **kwargs):  # noqa: E501
        """Log out of system  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.logout_with_http_info(x_session_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_session_id: Session identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logout" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_id' is set
        if ('x_session_id' not in params or
                params['x_session_id'] is None):
            raise ValueError("Missing the required parameter `x_session_id` when calling `logout`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_session_id' in params:
            header_params['X-Session-ID'] = params['x_session_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vksession/rest/session', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
