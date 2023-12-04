#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """Print all integers in the list in reverse order."""
    if my_list:
        reversed_list = list(reversed(my_list))
        for item in reversed_list:
            print("{:d}".format(item))
