#!/usr/bin/python3
"""
Module: 0-print_list_integer
Prints all integers in a list, one per line, using str.format()
"""
def print_list_integer(my_list=[]):
    """
    Prints all integers in my_list using str.format() with {:d}
    Args:
        my_list (list): List of integers
    """
    for i in my_list:
        print("{:d}".format(i))
