#!/usr/bin/python3

"""
inherits_from Module
Creates a function that returns true
if object is an instance of a class that inherited
(directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Function that checks if obj is an instance of a class
    inherited from a_class (directly or indirectly).
    
    Args:
        obj: object
        a_class: class
    
    Notes:
        Use type() to get specific class
        Use isinstance() to get class and any parent classes too
        Use issubclass() to get what object is a subclass of
    
    Return: True or False
    """
    return not type(obj) == a_class and issubclass(type(obj), a_class)
