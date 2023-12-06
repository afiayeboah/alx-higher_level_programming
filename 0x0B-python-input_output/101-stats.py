#!/usr/bin/python3
"""
Reads from standard input and computes metrics.

Prints the following statistics:
    - Total file size.
    - Count of each status code.

Terminates on keyboard interruption (CTRL + C).
"""


def print_metrics(accumulated_size, status_code_counts):
    """Print accumulated metrics.

    Args:
        accumulated_size (int): The total accumulated file size.
        status_code_counts (dict): The count of each status code.
    """
    print(f"File size: {accumulated_size}")
    for code, count in sorted(status_code_counts.items()):
        print(f"{code}: {count}")


if __name__ == "__main__":
    import sys

    accumulated_size = 0
    status_code_counts = {}
    valid_status_codes =
    {'200', '301', '400', '401', '403', '404', '405', '500'}
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_metrics(accumulated_size, status_code_counts)
                line_count = 1
            else:
                line_count += 1

            parts = line.split()

            try:
                file_size = int(parts[-1])
                accumulated_size += file_size
            except (IndexError, ValueError):
                pass

            try:
                status_code = parts[-2]
                if status_code in valid_status_codes:
                    status_code_counts[status_code] =
                    status_code_counts.get(status_code, 0) + 1
            except IndexError:
                pass

        print_metrics(accumulated_size, status_code_counts)

    except KeyboardInterrupt:
        print_metrics(accumulated_size, status_code_counts)
        raise
