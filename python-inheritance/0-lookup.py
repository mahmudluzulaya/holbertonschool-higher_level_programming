#!/usr/bin/python3
"""
Module 0-lookup
This module contains a function lookup that returns the list
of available attributes and methods of an object.
"""

def lookup(obj):
"""
Returns a list of available attributes and methods of an object.
"""
return dir(obj)
