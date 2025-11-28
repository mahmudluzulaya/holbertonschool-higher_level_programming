#!/usr/bin/python3
"""
Module that defines BaseGeometry class with area method
and integer validator method.
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.

        Args:
            name (str): The name of the parameter
            value (int): The value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        # Reject non-int types and bool
        if type(value) is not int or type(value) is bool:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
