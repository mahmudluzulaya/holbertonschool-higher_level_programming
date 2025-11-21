#!/usr/bin/python3
"""
Module: 0-print_list_integer
Prints all integers in a list, one per line, using str.format()
Raises TypeError if a non-integer is found
"""


def print_list_integer(my_list=[]):
    """
    Prints all integers in my_list using str.format()

    Args:
        my_list (list): List of integers
    Raises:
        TypeError: if any element in the list is not an integer
    """
    for i in my_list:
        if not isinstance(i, int):
            raise TypeError("All elements must be integers")
        print("{}".format(i))
