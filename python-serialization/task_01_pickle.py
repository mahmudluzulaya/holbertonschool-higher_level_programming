#!/usr/bin/python3
"""Pickling CustomObject class"""

import pickle


class CustomObject:
    """Custom object with name, age, and is_student attributes"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file using pickle"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file using pickle"""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except (FileNotFoundError, pickle.PickleError, EOFError):
            return None
