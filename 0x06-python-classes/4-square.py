#!/usr/bin/python3
"""This module contains a non-empty class."""

class Square:
    """A class defining a square by its size and calculating its area."""
    def __init__(self, size=0):
         """A function initializing an instance of the class.
        
        Args:
            size (int): The size of the square. Defaults to 0.

        """
        self.__size = size

    # Property
    @property
    def size(self):
        """int: The size of the square."""
        return self.__size

    # Setter modifies
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """A function calculating the area of the square.

        Returns:
            int: The area of the square. 

        """
        return self.__size ** 2
