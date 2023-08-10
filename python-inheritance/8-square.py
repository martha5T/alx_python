"""
This module defines the Square class.

The Square class inherits from the Rectangle class.
It has one private attribute: size.

The Square class has an area() method that calculates its area.
"""


class DefinitionOverrideMetaClass(type):
    """def __new__(cls, name, bases, attrs):
        # Customize the class creation process here
        return super().__new__(cls, name, bases, attrs)"""

    def __dir__(cls):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in
                super().__dir__() if attribute != '__init_subclass__']

Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """
    This class defines a rectangle.

    Attributes:
        _width (int): The width of the rectangle.
        _height (int): The height of the rectangle.

    Methods:
        area(): Calculates the area of the rectangle.

    Raises:
        AttributeError: If the attribute width or height is accessed.
        TypeError: If the value of size width or height is not an integer.
        ValueError: If the value of size is less than or equal to 0.
    """

    def __init__(self, size):
        """
        Initializes a new square.

        Args:
            size (int): The size of the square

        Raises:
            TypeError: If the value of size is not an integer.
            ValueError: If the value of size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self._size = size

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self._size * self._size

    def __str__(self):
        """
        Returns the square description.

        Returns:
            str: The description in the format [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self._size, self._size)

    def __dir__(cls):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in
            super().__dir__() if attribute != '__init_subclass__']