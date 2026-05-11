#!/usr/bin/python3
"""Defines a function that inserts text after lines containing a string"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string

    Args:
        filename (str): file name
        search_string (str): string to search for
        new_string (str): string to insert after matching lines
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
