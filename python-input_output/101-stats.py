#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""

import sys


def print_stats(total_size, status_codes):
    """Print stats"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()

            try:
                status = int(parts[-2])
                size = int(parts[-1])
            except (IndexError, ValueError):
                continue

            total_size += size

            if status in status_codes:
                status_codes[status] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    # 🔥 IMPORTANT FIX: always print at end
    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
