#!/usr/bin/python3
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    """Compute square value of all integers in matrix."""
    return [[x**2 for x in row] for row in matrix]
