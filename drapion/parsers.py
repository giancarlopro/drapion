"""
drapion.parsers
~~~~~~~~~~~~~~~

This module implements Drapion core parsers

:copyright: (c) 2018 Giancarlo Rocha
:license: Apache 2.0, see LICENSE for more details.
"""

import json
from typing import Dict, List, Union

from drapion import objects


class BaseParser:
    @classmethod
    def parse(cls, data: str) -> objects.DObject:
        """Creates a DObject with a `content` attribute containing data

        :param data: Data to put inside content attribute
        :return: Instance of DObject
        """
        return objects.DObject(attributes={'content': data})

class JSONParser(BaseParser):
    @classmethod
    def parse(cls, data: Union[str, Dict, List]) -> objects.DObject:
        """Parses a JSON into a DObject instance

        :param data: JSON str or parsed json e.g.: List or Dict
        :return: Instance of DObject
        """
        obj = json.loads(data) if isinstance(data, str) else data

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
        
        return objects.DObject(attributes=attributes, values=values)