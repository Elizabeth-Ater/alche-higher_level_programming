#!/usr/bin/python3
import sys


def print_stats(total_size, status_counts):
    """Print accumulated metrics"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        count = status_counts[code]
        if count:
            print(f"{code}: {count}")


def main():
    total_size = 0
    status_counts = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()

            try:
                status = parts[-2]
                size = int(parts[-1])
            except (IndexError, ValueError):
                continue

            if status in status_counts:
                status_counts[status] += 1

            total_size += size
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
