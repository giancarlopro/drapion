import json
from typing import Dict, List

from drapion import objects


class BaseParser:
    @classmethod
    def parse(cls, data):
        return objects.DObject(attributes={'content': data})

class JSONParser(BaseParser):
    @classmethod
    def parse(cls, data):
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