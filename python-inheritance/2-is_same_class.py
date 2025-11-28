#!/usr/bin/python3
"""
Function that checks if an object is exactly an instance
of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class,
    otherwise False.
    """
    return type(obj) is a_class
