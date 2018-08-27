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
:license: MIT, see LICENSE for more details.
"""

from drapion.objects import GenericObject, Drapion


__version__ = '0.1.0-dev'
__all__ = ['GenericObject', 'Drapion']
