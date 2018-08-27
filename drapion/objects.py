"""
drapion.objects
~~~~~~~~~~~~~~~

This module implements the core objects used by drapion

:copyright: (c) 2018 Giancarlo Rocha
:license: MIT, see LICENSE for more details.
"""

from typing import Union, List, Dict
import requests

from drapion.wrappers import api_call


class GenericObject:
    """Stores attributes and values to access like python objects

    dot-like access lookup inside _attributes dict

    >>> go = GenericObject(attributes={'name': 'Drapion'})
    >>> go.name
    'Drapion'

    Dict-like access also lookup inside _attributes dict

    >>> go['name']
    'Drapion'

    List-like access lookup inside _values list

    >>> go = GenericObject(values=['Drapion', 'Library'])
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
    
    @classmethod
    def parse(cls, obj: Union[List, Dict]):
        """Parses a python-like object into a GenericObject instance

        :param cls: Class wich parse was called
        :param obj: Dictionary or List, representation of the API response
            in the form of python objects, eg. dicts and list
        :return: Instance of cls class
        """

        attributes: Dict = {}
        values: List = []

        if isinstance(obj, List):
            for item in obj:
                if isinstance(item, List) or isinstance(item, Dict):
                    values.append(cls.parse(item))
                else:
                    values.append(item)
        elif isinstance(obj, Dict):
            for key in obj.keys():
                if isinstance(obj[key], List) or isinstance(obj[key], Dict):
                    attributes[key] = cls.parse(obj[key])
                else:
                    attributes[key] = obj[key]
        
        return cls(attributes, values)

class Drapion:
    """Sends a request to the API, with an endpoint
    
    :param base_url: API base url
    :param parser: Parser class used to parse the API Responde into a object
    """

    def __init__(self, base_url: str, parser = GenericObject):
        self.base_url = base_url
        self.parser = parser
    
    def __getattr__(self, name):
        return api_call(self.base_url + name, self.parser)
