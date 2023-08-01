#!/usr/bin/python3
"""
Write a calss square that defines a square by:
    Private instance Attribute: size
    Instantiation with size(no type/value verification)
    And no imported Module
"""
class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a square object.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
    
    def get_size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size
    
    def set_size(self, size):
        """
        Sets the size of the square.

        Args:
            size (int): The new size of the square.
        """
        self.__size = size
    
    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size