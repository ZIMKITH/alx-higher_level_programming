#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """Remove all 'c' and 'C' characters from the string"""
    new_string = "".join(char for char in my_string if char.lower() != 'c')
    return new_string
