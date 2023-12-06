#!/usr/bin/python3
# 6-print_sorted_dictionary.py

def print_sorted_dictionary(a_dictionary):
    """Print dictionary by ordered keys."""
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")`
