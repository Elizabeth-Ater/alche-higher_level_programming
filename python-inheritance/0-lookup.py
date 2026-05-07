#!/usr/bin/python3
"""Define an object atributes"""


def lookup(obj):
    """Use the dir() function to get the list of attributes and methods"""
    attr_and_methods = dir(obj)
    return (attr_and_methods)
