# coding: utf-8

"""
    ASR documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.dev
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloud_client.cloud_api_client import CloudApiClient


class PackagesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = CloudApiClient()
        self.api_client = api_client

    def get_available_packages(self, x_session_id, **kwargs):  # noqa: E501
        """Get all available packages  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_available_packages(x_session_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_session_id: Session identifier (required)
        :return: list[PackageDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_available_packages_with_http_info(x_session_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_available_packages_with_http_info(x_session_id, **kwargs)  # noqa: E501
            return data

    def get_available_packages_with_http_info(self, x_session_id, **kwargs):  # noqa: E501
        """Get all available packages  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_available_packages_with_http_info(x_session_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_session_id: Session identifier (required)
        :return: list[PackageDto]
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
                    " to method get_available_packages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_id' is set
        if ('x_session_id' not in params or
                params['x_session_id'] is None):
            raise ValueError("Missing the required parameter `x_session_id` when calling `get_available_packages`")  # noqa: E501

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
            '/v1/packages/available', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PackageDto]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def load(self, x_session_id, package_id, **kwargs):  # noqa: E501
        """Load package  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.load(x_session_id, package_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_session_id: Session identifier (required)
        :param str package_id: Package name (required)
        :return: StatusDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.load_with_http_info(x_session_id, package_id, **kwargs)  # noqa: E501
        else:
            (data) = self.load_with_http_info(x_session_id, package_id, **kwargs)  # noqa: E501
            return data

    def load_with_http_info(self, x_session_id, package_id, **kwargs):  # noqa: E501
        """Load package  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.load_with_http_info(x_session_id, package_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_session_id: Session identifier (required)
        :param str package_id: Package name (required)
        :return: StatusDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_id', 'package_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method load" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_id' is set
        if ('x_session_id' not in params or
                params['x_session_id'] is None):
            raise ValueError("Missing the required parameter `x_session_id` when calling `load`")  # noqa: E501
        # verify the required parameter 'package_id' is set
        if ('package_id' not in params or
                params['package_id'] is None):
            raise ValueError("Missing the required parameter `package_id` when calling `load`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'package_id' in params:
            path_params['packageId'] = params['package_id']  # noqa: E501

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
            '/v1/packages/{packageId}/load', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusDto',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unload(self, x_session_id, package_id, **kwargs):  # noqa: E501
        """Unload package  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.unload(x_session_id, package_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_session_id: Session identifier (required)
        :param str package_id: Package name (required)
        :return: StatusDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.unload_with_http_info(x_session_id, package_id, **kwargs)  # noqa: E501
        else:
            (data) = self.unload_with_http_info(x_session_id, package_id, **kwargs)  # noqa: E501
            return data

    def unload_with_http_info(self, x_session_id, package_id, **kwargs):  # noqa: E501
        """Unload package  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.unload_with_http_info(x_session_id, package_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_session_id: Session identifier (required)
        :param str package_id: Package name (required)
        :return: StatusDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_session_id', 'package_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unload" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_session_id' is set
        if ('x_session_id' not in params or
                params['x_session_id'] is None):
            raise ValueError("Missing the required parameter `x_session_id` when calling `unload`")  # noqa: E501
        # verify the required parameter 'package_id' is set
        if ('package_id' not in params or
                params['package_id'] is None):
            raise ValueError("Missing the required parameter `package_id` when calling `unload`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'package_id' in params:
            path_params['packageId'] = params['package_id']  # noqa: E501

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
            '/v1/packages/{packageId}/unload', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusDto',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
