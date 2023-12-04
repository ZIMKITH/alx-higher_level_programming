#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """Return a tuple with string length and first character"""
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return length, first_char
