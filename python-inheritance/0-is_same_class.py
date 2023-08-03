#!/usr/bin/python3
"""
This function returns true if the object is exactly an instance of the specified class ; otherwise False.
"""
def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.

    Args:
        obj: Any object to be checked.
        a_class: The class to check against.

    Returns:
        bool: True if the object is exactly an instance of the specified class; otherwise False.
    """
    return type(obj) is a_class