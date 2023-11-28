#!/usr/bin/python3
# 6-print_comb3.py

"""Prints all possible different combinations of two digits"""
for i in range(10):
    for j in range(i + 1, 10):
        print(f"{i}{j}", end="")
        if i == 8 and j == 9:
            break
        print(", ", end="")
print("")
