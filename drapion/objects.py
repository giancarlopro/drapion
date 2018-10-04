"""
drapion.objects
~~~~~~~~~~~~~~~

This module implements the core objects used by drapion

:copyright: (c) 2018 Giancarlo Rocha
:license: Apache 2.0, see LICENSE for more details.
"""

from typing import Union, List, Dict
import requests

from drapion import parsers


class DObject:
    """Stores attributes and values to access like python objects

    dot-like access lookup inside _attributes dict

        >>> go = DObject(attributes={'name': 'Drapion'})
        >>> go.name
        'Drapion'

    Dict-like access also lookup inside _attributes dict

        >>> go['name']
        'Drapion'

    List-like access lookup inside _values list

        >>> go = DObject(values=['Drapion', 'Library'])
        >>> go[0]
        'Drapion'

    It's possible to iterate over the instance values,
    the values of _attributes.values() and _values are summed up

        >>> for item in go:
        >>>     print(item)
        'Drapion'
        'Library'
    """

    def __init__(self, attributes: Dict = {}, values: List = []):
        self._attributes: Dict = attributes
        self._values: List = values

    def __getattr__(self, name):
        if name in self._attributes:
            return self._attributes[name]
        raise AttributeError
    
    def __getitem__(self, key):
        if isinstance(key, str):
            return self._attributes[key]
        return self._values[key]
    
    def __iter__(self):
        iterator = list(self._attributes.values()) + self._values
        return iter(iterator)

class Drapion:
    """Sends a request to the API, with an endpoint
    
    :param endpoint: API endpoint
    :param parser: Parser class used to parse the API Responde into a object
    """

    def __init__(self, endpoint: str, parser = parsers.JSONParser):
        self.endpoint = endpoint[:-1] if endpoint[-1] is '/' else endpoint
        self.parser = parser
    
    def __getattr__(self, name):
        return Drapion(self.endpoint + '/' + name, parser=self.parser)

    def __call__(self, _method: str = 'get', *args, **kwargs):
        """Connects to API and parse its response

        :param _method: Method to be used with requests
        :param rkwargs: (Optional) Dictionary, Optional kwargs to send with requests,
            any kwarg available for requests library
        :return: The result from parser.parse
        """

        if _method in ('get', 'options', 'head', 'post', 'put', 'patch', 'delete'):
            func = getattr(requests, _method)
        else:
            raise Exception('Unknown method {}'.format(_method))
        
        rkwargs = kwargs.pop('rkwargs', {})

        if _method is 'get':
            params = '?'
            for key in kwargs:
                params += key + '=' + kwargs[key] + '&'

            resource = func(self.endpoint + params, **rkwargs).text
        else:
            resource = func(self.endpoint, data=kwargs, **rkwargs).text

        return self.parser.parse(resource)