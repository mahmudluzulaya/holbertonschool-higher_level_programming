#!/usr/bin/python3
"""
Module 0-lookup
Defines a function that returns the list of available attributes and methods of an object.
"""

def lookup(obj):
"""
Returns a list of available attributes and methods of an object.

```
Args:
    obj (any): The object or class to inspect.

Returns:
    list: Sorted list of attribute names and method names.
"""
# dir() returns all attributes and methods of the object, including inherited ones
return dir(obj)
```
