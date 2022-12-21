#!/usr/bin/python3
"""This module contains a non-empty class."""

class Square:
    """A class defining a square by its size."""
    def __init__(self, size=0):
        """A function initializing an instance of the class.
        
        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size #: Private instance attribute
