#!/usr/bin/python3
"""Defines Rectangle class with area and string representation."""

Rectangle = __import__('8-rectangle').Rectangle


class Rectangle(Rectangle):
    """Rectangle class."""

    def area(self):
        """Returns area of rectangle."""
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """String representation of rectangle."""
        return "[Rectangle] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
