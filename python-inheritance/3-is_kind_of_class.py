#!/usr/bin/python3
"""Defines a function that checks instance inheritance."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or inherited."""
    return isinstance(obj, a_class)
