#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """Replace element at a specific position in the original list"""
    new_list = my_list[:]
    if 0 <= idx < len(my_list):
        new_list[idx] = element
    return new_list
