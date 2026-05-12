#!/usr/bin/python3
import sys

def print_stats(total_size, status_counts):
    """
    Prints accumulated statistics.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] != 0:
            print("{}: {}".format(code, status_counts[code]))

# Initialize variables
total_size = 0
status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
status_counts = {code: 0 for code in status_codes}

line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()

        try:
            status = parts[-2]
            file_size = int(parts[-1])
        except (IndexError, ValueError):
            continue

        total_size += file_size

        if status in status_counts:
            status_counts[status] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise
