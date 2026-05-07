#!/usr/bin/python3
"""Defines a function that checks inheritance."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
