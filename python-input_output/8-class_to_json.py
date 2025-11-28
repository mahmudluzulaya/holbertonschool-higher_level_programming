#!/usr/bin/python3
"""
Function that returns the dictionary description
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of a class
    instance with only serializable attributes (list,
    dict, str, int, bool).
    """
    return obj.__dict__.copy()
