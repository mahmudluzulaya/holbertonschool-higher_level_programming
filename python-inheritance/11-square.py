#!/usr/bin/python3
"""Square class that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize the square with size validated"""
        self.integer_validator("size", size)
        self.__size = size
        # Call Rectangle constructor with width and height as size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return the square description for print() and str()"""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)        
