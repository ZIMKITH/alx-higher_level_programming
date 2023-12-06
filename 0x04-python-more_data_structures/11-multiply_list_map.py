#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """Multiply each element in the list by the specified number."""
    return list(map(lambda i: i * number, my_list))
