#!/usr/bin/python3
"""
This function will messeage area() is not implemented.
"""
class BaseGeometry:
    """
    This class represents a base geometry.
    """

    def area(self):
        """
        Calculates the area.

        Raises:
            Exception: with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")