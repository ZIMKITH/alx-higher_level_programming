#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in the list"""
    multiples_2 = [item % 2 == 0 for item in my_list]
    return multiples_2
