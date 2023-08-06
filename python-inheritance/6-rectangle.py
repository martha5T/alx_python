"""
This module defines the Rectangle class.

The Rectangle class inherits from the BaseGeometry class. It has two private attributes: width and height. These attributes are validated by the integer_validator() method from the BaseGeometry class.

The Rectangle class has an area() method that calculates the area of the rectangle.
"""

class definitionOverrideMetaClass(type):
    """def __new__(cls, name, bases, attrs):
        # Customize the class creation process here
        return super().__new__(cls, name, bases, attrs)"""

    def __dir__(cls):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    This class defines a rectangle.

    Attributes:
        _width (int): The width of the rectangle.
        _height (int): The height of the rectangle.

    Methods:
        area(): Calculates the area of the rectangle.

    Raises:
        AttributeError: If the attribute width or height is accessed.
        TypeError: If the value of the attribute width or height is not an integer.
        ValueError: If the value of the attribute width or height is less than or equal to 0.
    """

    def __init__(self, width, height):
        """
        Initializes a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If the value of the attribute width or height is not an integer.
            ValueError: If the value of the attribute width or height is less than or equal to 0.
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self._width * self._height

    # Prevents the attributes width and height from being accessed directly.
    def __getattribute__(self, name):
        if name in ["_width", "_height"]:
            raise AttributeError("'Rectangle' object has no attribute '{}'".format(name))
        elif name == "height" and not isinstance(object.__getattribute__(self, "_height"), int):
            raise TypeError("height must be an integer")
        return super().__getattribute__(name)

    def __dir__(cls):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']