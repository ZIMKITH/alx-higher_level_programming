#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Return set of elements that are unique to each set."""
    return set_1.symmetric_difference(set_2)
