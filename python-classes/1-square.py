#!/usr/bin/python3


"""Module that defines a Square class."""


class Square:
    """Square class with a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: size of the square (no type checking required)
        """
        self.__size = size

