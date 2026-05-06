#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        print()
        return True
    except ValueError:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
    return False
