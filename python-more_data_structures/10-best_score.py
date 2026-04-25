#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    the_max_score = float('-inf')
    best_key = None

    for key, value in a_dictionary.items():
        if value > the_max_score:
            the_max_score = value
            best_key = key

    return best_key
