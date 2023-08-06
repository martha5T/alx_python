"""
This module defines the BaseGeometry class.

The BaseGeometry class is an abstract class that cannot be instantiated. It is used as a base class for other classes that will implement the area() method.

The area() method is not implemented because the class BaseGeometry is an abstract class.
"""


class definitionOverrideMetaClass(type):
    def __new__(cls, name, bases, attrs):
        # Customize the class creation process here
        return super().__new__(cls, name, bases, attrs)

    def __dir__(cls):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(definitionOverrideMetaClass('BaseGeometry', (), {})):
    """
    This class defines a public instance method called area() that raises an Exception exception with the message area() is not implemented.
    """

    def area(self):
        """
        The area() method is not implemented because the class BaseGeometry is an abstract class. 
        """

        raise Exception("area() is not implemented")
        """
        Raises:
        Exception: The message area() is not implemented
        """
    
    def __dir__(cls):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']