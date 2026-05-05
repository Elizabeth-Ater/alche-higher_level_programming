#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    printed_elts = 0

    try:
        for v in my_list:
            try:
                int_value = int(v)
                print("{:d}".format(int_value), end="")
                printed_elts += 1
                if printed_elts >= x:
                    break
            except ValueError:
                continue
    except TypeError:
        pass
    print()
    return (printed_elts)
