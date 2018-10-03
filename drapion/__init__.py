"""
Drapion API's Library
~~~~~~~~~~~~~~~~~~~~~

Drapion is an library that facilitates consuming web API's
Example usage:

    >>> from drapion import Drapion
    >>> bot = Drapion('https://jsonplaceholder.typicode.com/')
    >>> r = bot.users() # Will connect to https://jsonplaceholder.typicode.com/users endpoint
    >>> r[0].name
    'Leanne Graham'

The purpose of this project is just fun.

:copyright: (c) 2018 Giancarlo Rocha
:license: Apache 2.0, see LICENSE for more details.
"""

from drapion.objects import DObject, Drapion


__version__ = '0.1.0-dev'
__all__ = ['DObject', 'Drapion']