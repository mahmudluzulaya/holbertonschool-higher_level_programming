#!/usr/bin/python3
"""
Function that checks if an object is an instance of a subclass
(inherited directly or indirectly) of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    from a_class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
