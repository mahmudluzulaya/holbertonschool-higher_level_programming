#!/usr/bin/python3
"""
Student module with filtered JSON representation
"""


class Student:
    """Defines a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes in this list are included.
        Otherwise, all attributes are included.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {
                a: getattr(self, a)
                for a in attrs
                if hasattr(self, a)
            }
        return self.__dict__.copy()
