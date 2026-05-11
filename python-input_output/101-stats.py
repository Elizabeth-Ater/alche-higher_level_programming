#!/usr/bin/python3
"""Log parsing script"""

import sys


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code]:
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

    count = 0

    try:
        for line in sys.stdin:
            parts = line.split()

            try:
                status = int(parts[-2])
                size = int(parts[-1])
            except:
                continue

            total_size += size

            if status in status_codes:
                status_codes[status] += 1

            count += 1

            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
