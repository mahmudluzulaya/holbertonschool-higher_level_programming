#!/usr/bin/python3
"""
Module that defines the MyList class.
"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        Does not modify the original list.
        """
        print(sorted(self))
