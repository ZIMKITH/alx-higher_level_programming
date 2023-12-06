#!/usr/bin/python3
# 9-multiply_by_2.py

def multiply_by_2(a_dictionary):
    """Return new dictionary with all values multiplied by 2."""
    return {key: value * 2 for key, value in a_dictionary.items()}
