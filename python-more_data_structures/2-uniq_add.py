#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    uniq_numbers = set()
    for i in my_list:
        if i not in uniq_numbers:
            result += i
            uniq_numbers.add(i)
    return result
