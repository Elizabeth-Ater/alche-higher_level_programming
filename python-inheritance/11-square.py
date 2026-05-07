#!/usr/bin/python3
"""Defines Square class with string representation."""

Square = __import__('10-square').Square


class Square(Square):
    """Square class."""

    def __str__(self):
        """String representation of square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
