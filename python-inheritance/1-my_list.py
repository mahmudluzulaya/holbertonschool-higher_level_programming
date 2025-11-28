#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list.
"""
class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Prints the list in ascending sorted order"""
        print(sorted(self))
