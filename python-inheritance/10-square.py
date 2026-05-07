#!/usr/bin/python3
"""Defines Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size):
        """Initializes square with size."""
        self.integer_validator("size", size)
        self._Rectangle__width = size
        self._Rectangle__height = size
