#!/usr/bin/python3
"""
Write a class Square that defines a square based on 1-square.py
   using a private instance attribute :size
   and another public instance method def area (self):
"""
class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a square object.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
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

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size