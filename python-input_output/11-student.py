#!/usr/bin/python3
"""Student class with JSON serialization and deserialization"""

class Student:
    """Represents a student with public attributes"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the Student instance.
        If attrs is a list of strings, only include those attributes.
        """
        if attrs is None:
            return self.__dict__.copy()
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with json dict"""
        for key, value in json.items():
            setattr(self, key, value)
