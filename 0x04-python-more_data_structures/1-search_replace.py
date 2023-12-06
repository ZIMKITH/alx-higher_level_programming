#!/usr/bin/python3
# 1-search_replace.py

def search_replace(my_list, search, replace):
    """Replaces all occurrences of element by another in new list"""
    return [replace if x == search else x for x in my_list]
