#!/usr/bin/python3
import sys
import signal
from collections import defaultdict

def print_statistics(total_size, status_counts):
    print(f'Total file size: {total_size}')
    for status_code in sorted(status_counts):
        print(f'{status_code}: {status_counts[status_code]}')

def process_input_line(line, total_size, status_counts):
    try:
        _, _, _, _, status_code_str, file_size_str = line.split()[-5:]
        status_code = int(status_code_str)
        file_size = int(file_size_str)
        total_size += file_size
        status_counts[status_code] += 1
    except (ValueError, IndexError):
        pass  # Ignore lines that don't match the expected format

    return total_size, status_counts

def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            total_size, status_counts = process_input_line(line, total_size, status_counts)

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
