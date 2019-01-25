# coding: utf-8

"""
    TeamCity REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2018.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import
from dohq_teamcity.custom.base_model import TeamCityObject

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dohq_teamcity.models.test import Test  # noqa: F401,E501
from dohq_teamcity.models.tests import Tests  # noqa: F401,E501


class TestApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
    base_name = 'Test'

    def __init__(self, api_client=None):
        self.api_client = api_client

    def get_tests(self, **kwargs):  # noqa: E501
        """get_tests  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tests(async_req=True)
        >>> result = thread.get()

        :param async_req: bool
        :param str locator:
        :param str fields:
        :return: Tests
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_tests_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.__get_tests_with_http_info(**kwargs)  # noqa: E501
            return data

    def serve_instance(self, test_locator, **kwargs):  # noqa: E501
        """serve_instance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serve_instance(test_locator, async_req=True)
        >>> result = thread.get()

        :param async_req: bool
        :param str test_locator: (required)
        :param str fields:
        :return: Test
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__serve_instance_with_http_info(test_locator, **kwargs)  # noqa: E501
        else:
            (data) = self.__serve_instance_with_http_info(test_locator, **kwargs)  # noqa: E501
            return data

    def __get_tests_with_http_info(self, **kwargs):  # noqa: E501
        """get_tests  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.__get_tests_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str locator:
        :param str fields:
        :return: Tests
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['locator', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tests" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'locator' in params:
            query_params.append(('locator', params['locator']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/app/rest/tests', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tests',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def __serve_instance_with_http_info(self, test_locator, **kwargs):  # noqa: E501
        """serve_instance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.__serve_instance_with_http_info(test_locator, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str test_locator: (required)
        :param str fields:
        :return: Test
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['test_locator', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method serve_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'test_locator' is set
        if ('test_locator' not in params or
                params['test_locator'] is None):
            raise ValueError("Missing the required parameter `test_locator` when calling `serve_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'test_locator' in params:
            if isinstance(params['test_locator'], TeamCityObject):
                path_params['testLocator'] = params['test_locator'].locator_id
            else:
                path_params['testLocator'] = params['test_locator']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/app/rest/tests/{testLocator}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Test',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
