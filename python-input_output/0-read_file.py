#!/usr/bin/python3
"""Define a read_file function"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout

    Args:
        filename (str): The name of the text file to read

    Returns:
        None
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        pass
