#!/usr/bin/python3
"""This module contains a non-empty class and imports the math module"""
import math


class MagicClass:
    """A class defining a circle by its radius and calculating its area and circumference."""
    def __init__(self, radius):
        """A function initializing an instance of the class.
        
        Args:
            radius: The radius of the circle.

        Raises:
            TypeError: If `radius` is not a number

        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self, radius):
        """A function calculating the area of the circle.

        Returns: The area of the circle.

        """
        return self.__radius ** 2 * math.pi

    def circumference(self, radius):
        """A function calculating the circumference of the circle.

        Returns: The circumference of the circle.
 
        """
        return 2 * math.pi * self.__radius
