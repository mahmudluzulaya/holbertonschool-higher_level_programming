#!/usr/bin/python3
def lookup(obj):
"""
Returns a list of available attributes and methods of an object.

```
Args:
    obj: Any Python object or class.

Returns:
    List of attribute names and method names of the object.
"""
# Use the built-in dir() function to get all attributes and methods
# of the object or class. This includes inherited attributes.
return dir(obj)  # dir() returns a sorted list of strings
```
