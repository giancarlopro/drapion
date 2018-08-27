"""
drapion.wrappers
~~~~~~~~~~~~~~~~

This module implements wrappers functions used by drapion module

:copyright: (c) 2018 Giancarlo Rocha
:license: MIT, see LICENSE for more details.
"""

import requests
from typing import Any


def api_call(url: str, parser: Any):
    """Returns a wrapper function that parses API's response
    
    :param url: API Endpoint to call
    :param parser: Class that is used for parsing the response inside
        the wrapper method
    :return: A wrapper function
    """

    def wrapper(method: str = 'get', *args, **kwargs):
        """Connects to API and parse its response

        :param method: Method to be used with requests
        :param rkwargs: (Optional) Dictionary, Optional kwargs to send with requests,
            any kwarg available for requests library
        :return: The result from parser.parse
        """

        if method in ('get', 'options', 'head', 'post', 'put', 'patch', 'delete'):
            func = getattr(requests, method)
        else:
            func = requests.get # TODO: Maybe raise an exception
        
        params = '?'
        for key in kwargs:
            params += key + '=' + kwargs[key] + '&'
        
        rkwargs = kwargs.pop('rkwargs', {})

        resource = func(url + params, **rkwargs).json()
        return parser.parse(resource)
    return wrapper
