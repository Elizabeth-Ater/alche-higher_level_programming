#!/usr/bin/python3
"""
Log parsing module.
Reads stdin line by line and computes metrics.
"""

import sys


def print_stats(total_size, status_codes):
    """
    Prints accumulated statistics.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


def main():
    total_size = 0
    line_count = 0

    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    try:
        for line in sys.stdin:
            parts = line.split()

            if len(parts) < 2:
                continue

            try:
                status = parts[-2]
                size = int(parts[-1])
            except (ValueError, IndexError):
                continue

            if status in status_codes:
                status_codes[status] += 1

            total_size += size
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
