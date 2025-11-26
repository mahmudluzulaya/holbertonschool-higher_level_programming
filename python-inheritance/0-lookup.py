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
return dir(obj)
```
