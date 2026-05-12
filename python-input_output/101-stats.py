#!/usr/bin/python3
"""Log parsing and statistics computation from stdin."""

import sys


def print_stats(total_size, status_codes):
    """Print accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code]:
            print(f"{code}: {status_codes[code]}")


def main():
    """Process log lines from stdin and compute metrics."""
    total_size = 0
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

    count = 0

    try:
        for line in sys.stdin:
            parts = line.split()

            if len(parts) < 2:
                continue

            try:
                status = parts[-2]
                file_size = int(parts[-1])
            except (ValueError, IndexError):
                continue

            if status in status_codes:
                status_codes[status] += 1

            total_size += file_size
            count += 1

            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
